# P1: Data Detective
## Individual Project Brief
## Data Structures, Spring 2026

## Snapshot
- **Format:** Individual project
- **Suggested repo name:** `ds26-p1-data-detective-<student>`
- **Project window:** Weeks 4–5
- **Language:** Python 3.11+
- **Allowed libraries:** Standard library only
- **Graded artifacts:** `.py` files + `pytest` tests
- **Not graded:** notebooks

## Big idea
Build a small text-analysis tool that loads a text file, cleans and tokenizes the text, counts word frequencies, and reports useful results.

This project is about writing clear Python, using functions well, testing your code, and explaining your choices. It is **not** a stack/queue project. Keep the work focused and readable.

## What you will build
Your program should:
1. Load text from a file.
2. Normalize the text.
3. Tokenize the text into words.
4. Count word frequencies with a dictionary.
5. Return the top N most common words.
6. Produce **one** extra insight of your choice.

## Required functions
You must implement these in `src/project.py`:

- `load_text(path: str) -> str`
- `normalize_text(text: str) -> str`
- `tokenize(text: str) -> list[str]`
- `count_words(words: list[str]) -> dict[str, int]`
- `top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]`
- `extra_insight(words: list[str], counts: dict[str, int]) -> object`

You may add helper functions if needed.

## One extra insight (pick one)
Choose **one**:
- words that appear only once
- longest words
- average word length
- most common word lengths
- shortest and longest unique words
- another small idea approved by the instructor

Keep it modest. This is not a giant analytics platform.

## Input rules
- Your input must come from a text file in the repo.
- Use UTF-8 text files.
- Keep the dataset classroom-safe and reasonably sized.
- Public-domain text, your own writing, transcripts, articles, or short corpora are all fine.

## Output expectations
Your project should be able to print or return:
- total word count
- number of unique words
- top N words
- one extra insight

A simple text output is enough. Do not waste time making a fancy UI.

## Required repo structure
```text
src/project.py
tests/test_project.py
README.md
data/sample.txt
.github/workflows/tests.yml
```

## README requirements
Your `README.md` must include:

### 1. Project summary
What dataset you chose and what your tool does.

### 2. Approach
A short bullet list explaining your steps.

### 3. Complexity
Give time/space complexity for:
- `count_words`
- `top_n_words`

Add 1–3 lines of reasoning.

### 4. Edge-case checklist
Check and explain:
- empty file
- punctuation-heavy input
- repeated words
- uppercase/lowercase differences
- `n <= 0` for top-N

### 5. Assistance & sources
Include:
- AI used? (Y/N)
- What it helped with
- Any non-course sources

### 6. Design note
Write **150–250 words** explaining:
- what choices you made
- what was easy/hard
- one improvement you would make next

## Milestones

### Milestone 1 (this week)
- choose a dataset
- create repo
- add `data/sample.txt`
- write a short README summary
- add starter functions in `src/project.py`
- create at least **3 passing tests**

### Milestone 2
- all required functions work
- normal cases pass
- empty/edge cases handled

### Milestone 3
- README finished
- demo output works
- code cleaned up

## Rules
- Use **stdlib only**.
- Write clear functions with type hints.
- Write tests with `pytest`.
- Follow PEP 8.
- Keep your code modular.
- Do not hard-code results that only work for one file.

## Academic integrity
- You may discuss ideas and debugging.
- You may **not** copy code from another student.
- If you use AI, say so in the README.
- Your explanation and code should match what *you* understand.

## What I am grading for
- Correctness
- Clear function design
- Useful tests
- Reasonable complexity explanations
- Edge-case handling
- Readable code
- Honest documentation

## Starter advice
Start small:
1. get `load_text()` working
2. normalize text
3. split into words
4. count words
5. test each step
6. only then add top-N and the extra insight

That is the move. Do not build the whole thing in one giant function.
