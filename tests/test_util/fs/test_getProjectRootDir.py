import os
import pytest
from unittest.mock import patch
from namespace.util import getProjectRootDir


@patch("os.path.abspath")
@patch("os.listdir")
def test_project_root_found(mock_listdir, mock_abspath):
    mock_abspath.side_effect = ["/path/to/project/dir", "/path/to/project", "/path/to", "/path"]
    mock_listdir.side_effect = [[], ["src"], ["file1", "pyproject.toml"], ["file2"]]
    result = getProjectRootDir()
    assert result == "/path/to/src"


@patch("os.path.abspath")
@patch("os.listdir")
def test_project_root_not_found(mock_listdir, mock_abspath):
    mock_abspath.side_effect = ["/path/to/dir", "/path/to", "/path"]
    mock_listdir.side_effect = [[], ["file1", "file2"], []]
    with pytest.raises(FileNotFoundError):
        getProjectRootDir()
