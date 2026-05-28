import os
from pathlib import Path

from tests.utils import run_within_dir


def test_run_within_dir(tmp_path: Path):
    """Test that run_within_dir changes and restores the working directory."""
    original_cwd = os.getcwd()
    target_dir = tmp_path / "test_dir"
    target_dir.mkdir()

    with run_within_dir(target_dir):
        # Inside the context, the cwd should be the target directory
        assert os.getcwd() == str(target_dir.resolve())

    # Outside the context, it should be restored
    assert os.getcwd() == original_cwd


def test_run_within_dir_exception(tmp_path: Path):
    """Test that run_within_dir restores the working directory even on exception."""
    original_cwd = os.getcwd()
    target_dir = tmp_path / "test_dir_err"
    target_dir.mkdir()

    try:
        with run_within_dir(target_dir):
            assert os.getcwd() == str(target_dir.resolve())
            raise ValueError("Test error")
    except ValueError:
        pass

    # Still should restore even if an exception occurred
    assert os.getcwd() == original_cwd
