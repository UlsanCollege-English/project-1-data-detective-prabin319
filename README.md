[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cDnlIYNC)
# P1: Data Detective

## Summary
This project loads a text file, normalizes and tokenizes the text, counts word frequencies,
reports the top N most common words, and identifies the longest word that appears only once.

## Dataset
- **File:** `data/sample.txt`
- **Source:** Project Gutenberg — https://www.gutenberg.org/cache/epub/52106/pg52106.txt
- **Why I chose it:** *The Origin and Development of the Moral Ideas* by Edward Westermarck
  (1906) is a public-domain academic work in philosophy and anthropology. It uses
  specialised vocabulary like "retributive", "indignation", "civilisation", and
  "disinterestedness", which makes the word frequency and longest-unique-word analysis
  genuinely interesting — very different from fiction.

## How to run
```bash
python -m pytest -q
python -m src.project
```

## Approach
- Load the raw text from a UTF-8 file using `Path.read_text()`
- Normalize: lowercase everything, strip punctuation, collapse whitespace
- Tokenize: split on spaces into a list of words
- Count frequencies: build a dictionary with one pass through the word list
- Find top N: sort by count descending, break ties alphabetically, slice to N
- Extra insight: find all words that appear exactly once, then return the longest

## Complexity

### `count_words`
- **Time:** O(n) — we make one pass through the word list of length n
- **Space:** O(u) — we store one entry per unique word; u ≤ n
- **Why:** Each word is looked up and updated in the dictionary once. Dictionary
  operations (get, set) are O(1) on average, so the total is O(n).

### `top_n_words`
- **Time:** O(u log u) — sorting u unique words dominates
- **Space:** O(u) — we create a list of all (word, count) pairs before slicing
- **Why:** Python's `sorted()` uses Timsort which is O(u log u). The slice at the
  end is O(n) but n ≤ u so sorting dominates.

## Edge-case checklist
- [x] **Empty file** — `load_text` returns `""`, `tokenize("")` returns `[]`,
  `count_words([])` returns `{}`, `top_n_words({}, n)` returns `[]`.
  `extra_insight` returns `""` when there are no unique words.
- [x] **Punctuation-heavy input** — `normalize_text` strips all punctuation using
  `str.translate` before tokenizing, so `"hello!"` becomes `"hello"`.
- [x] **Repeated words** — `count_words` accumulates counts correctly;
  tested with `["red", "blue", "red"]` → `{"red": 2, "blue": 1}`.
- [x] **Uppercase/lowercase differences** — `normalize_text` lowercases first,
  so `"Alice"` and `"alice"` are counted as the same word.
- [x] **`n <= 0`** — `top_n_words` returns `[]` immediately when `n <= 0`.

## Assistance & sources
- **AI used?** Yes
- **What it helped with:** Explaining project structure, reviewing function logic,
  helping write the README complexity sections
- **Other sources:** Project Gutenberg (https://www.gutenberg.org) for the dataset

## Design note (150–250 words)
I chose *Alice's Adventures in Wonderland* because it is a well-known classic with
a wide range of vocabulary — short common words like "the" and "said" appear
hundreds of times, while unusual words like "chrysalis" or "waistcoat" appear only
once or twice. This contrast makes the frequency analysis genuinely interesting to
look at.

For the design, I kept each function small and focused on one job. `normalize_text`
only cleans; `tokenize` only splits; `count_words` only counts. This made each
function easy to test independently, which the project brief emphasised. The
hardest part was deciding what counts as "normalization." I chose to remove all
punctuation and lowercase everything, which means hyphenated words like "rabbit-hole"
become two tokens ("rabbithole" with `translate` actually joins them — so I verified
this and it is fine for this project's purposes).

The extra insight I chose is the longest word that appears only once. I found this
more interesting than simple averages because it reveals rare, distinctive vocabulary.
For Alice, that word tends to be something like "disappointment" or "encouragingly."

One improvement I would make next is to strip common "stop words" like "the", "a",
"of", "and" from the top-N results, since they dominate the frequency list and are
not very informative. A small stop-word list from the standard library's `re` module
would be enough.