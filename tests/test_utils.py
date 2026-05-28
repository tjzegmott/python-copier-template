import pytest
import yaml
from pathlib import Path
from tests.utils import is_valid_yaml

def test_is_valid_yaml_valid(tmp_path: Path):
    """Test is_valid_yaml with a valid YAML file."""
    yaml_file = tmp_path / "valid.yml"
    yaml_file.write_text("key: value\nlist:\n  - item1\n  - item2\n")
    assert is_valid_yaml(yaml_file) is True

def test_is_valid_yaml_invalid(tmp_path: Path):
    """Test is_valid_yaml with an invalid YAML file."""
    yaml_file = tmp_path / "invalid.yml"
    # Invalid indentation
    yaml_file.write_text("key: value\n  invalid: indentation\n")
    assert is_valid_yaml(yaml_file) is False

def test_is_valid_yaml_not_found(tmp_path: Path):
    """Test is_valid_yaml with a non-existent file."""
    yaml_file = tmp_path / "non_existent.yml"
    assert is_valid_yaml(yaml_file) is False

def test_is_valid_yaml_os_error(tmp_path: Path):
    """Test is_valid_yaml with an OSError (e.g., passing a directory)."""
    # tmp_path is a directory
    assert is_valid_yaml(tmp_path) is False
