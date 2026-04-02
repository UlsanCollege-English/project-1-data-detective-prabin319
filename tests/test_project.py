import os
import tempfile

from src.project import (
    count_words,
    extra_insight,
    load_text,
    normalize_text,
    tokenize,
    top_n_words,
)


# --- normalize_text ---

def test_normalize_text_lowercases_text() -> None:
    assert normalize_text("Hello WORLD") == "hello world"


def test_normalize_text_removes_punctuation() -> None:
    assert normalize_text("Hello, world!") == "hello world"


def test_normalize_text_collapses_whitespace() -> None:
    assert normalize_text("one  two   three") == "one two three"


# --- tokenize ---

def test_tokenize_splits_words() -> None:
    assert tokenize("one two three") == ["one", "two", "three"]


def test_tokenize_empty_string_returns_empty_list() -> None:
    assert tokenize("") == []


# --- count_words ---

def test_count_words_counts_repeated_words() -> None:
    words = ["red", "blue", "red"]
    assert count_words(words) == {"red": 2, "blue": 1}


def test_count_words_empty_list() -> None:
    assert count_words([]) == {}


def test_count_words_all_unique() -> None:
    words = ["a", "b", "c"]
    assert count_words(words) == {"a": 1, "b": 1, "c": 1}


# --- top_n_words ---

def test_top_n_words_returns_most_common_items() -> None:
    counts = {"apple": 3, "banana": 1, "carrot": 2}
    assert top_n_words(counts, 2) == [("apple", 3), ("carrot", 2)]


def test_top_n_words_with_non_positive_n_returns_empty_list() -> None:
    counts = {"apple": 3}
    assert top_n_words(counts, 0) == []


def test_top_n_words_negative_n_returns_empty_list() -> None:
    counts = {"apple": 3}
    assert top_n_words(counts, -5) == []


def test_top_n_words_ties_broken_alphabetically() -> None:
    counts = {"banana": 2, "apple": 2}
    assert top_n_words(counts, 2) == [("apple", 2), ("banana", 2)]


def test_top_n_words_n_larger_than_vocab() -> None:
    counts = {"a": 1, "b": 2}
    result = top_n_words(counts, 100)
    assert len(result) == 2


# --- extra_insight ---

def test_extra_insight_returns_longest_unique_word() -> None:
    words = ["cat", "elephant", "cat", "dog"]
    counts = count_words(words)
    # "elephant" and "dog" each appear once; elephant is longer
    assert extra_insight(words, counts) == "elephant"


def test_extra_insight_no_unique_words_returns_empty_string() -> None:
    words = ["cat", "cat", "dog", "dog"]
    counts = count_words(words)
    assert extra_insight(words, counts) == ""


# --- load_text ---

def test_load_text_reads_file_content() -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", encoding="utf-8", delete=False
    ) as f:
        f.write("hello world")
        tmp_path = f.name
    try:
        assert load_text(tmp_path) == "hello world"
    finally:
        os.unlink(tmp_path)


def test_load_text_empty_file_returns_empty_string() -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", encoding="utf-8", delete=False
    ) as f:
        f.write("")
        tmp_path = f.name
    try:
        assert load_text(tmp_path) == ""
    finally:
        os.unlink(tmp_path)