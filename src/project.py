"""Project 1 starter: Data Detective.

Dataset: The Origin and Development of the Moral Ideas* by Edward Westermarck (Public Domain)
"""

from __future__ import annotations

import string
from pathlib import Path


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    return Path(path).read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    """Return a normalized version of the text.

    - Lowercases everything
    - Removes punctuation
    - Collapses extra whitespace
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Split normalized text into a list of words."""
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word appears.

    Time complexity:  O(n) — one pass through the word list
    Space complexity: O(u) — u is the number of unique words
    """
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top N words as (word, count) tuples.

    - If n <= 0, returns []
    - Sorted by count descending; ties broken alphabetically

    Time complexity:  O(u log u) — sorting u unique words
    Space complexity: O(u) — storing all items before slicing
    """
    if n <= 0:
        return []
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    """Return the longest word that appears only once in the text.

    If no such word exists, returns an empty string.
    """
    unique_words = [word for word, count in counts.items() if count == 1]
    if not unique_words:
        return ""
    return max(unique_words, key=len)


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the full analysis pipeline and return summary data."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    demo_path = Path("data/sample.txt")
    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("No demo file found at data/sample.txt")