"""Tests for utility functions."""

from pathlib import Path
from unittest.mock import patch

import pytest

from tests.utils import file_contains_text


def test_file_contains_text_found(tmp_path: Path):
    """Test when file exists and contains the text."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World! This is a test.")

    assert file_contains_text(test_file, "World") is True
    assert file_contains_text(test_file, "Hello, World!") is True


def test_file_contains_text_not_found(tmp_path: Path):
    """Test when file exists but does not contain the text."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World! This is a test.")

    assert file_contains_text(test_file, "Missing") is False


def test_file_contains_text_missing_file(tmp_path: Path):
    """Test when file does not exist."""
    missing_file = tmp_path / "missing.txt"

    assert file_contains_text(missing_file, "text") is False


@patch("pathlib.Path.read_text")
def test_file_contains_text_os_error(mock_read_text, tmp_path: Path):
    """Test when an OSError occurs while reading the file."""
    mock_read_text.side_effect = OSError("Permission denied")

    test_file = tmp_path / "test.txt"

    assert file_contains_text(test_file, "text") is False
