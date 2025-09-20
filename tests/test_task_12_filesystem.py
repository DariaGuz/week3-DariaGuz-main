import pytest
from task_12_filesystem import FileSystem


def test_basic_mkdir_and_ls():
    fs = FileSystem()
    fs.mkdir("/a/b/c")
    assert fs.ls("/") == ["a"]
    assert fs.ls("/a") == ["b"]
    assert fs.ls("/a/b") == ["c"]
    assert fs.ls("/a/b/c") == []


def test_add_and_read_file():
    fs = FileSystem()
    fs.addContentToFile("/a/b/c/d", "hello")
    assert fs.readContentFromFile("/a/b/c/d") == "hello"
    fs.addContentToFile("/a/b/c/d", " world")
    assert fs.readContentFromFile("/a/b/c/d") == "hello world"


def test_ls_file_vs_dir():
    fs = FileSystem()
    fs.addContentToFile("/a/b/c/d", "x")
    assert fs.ls("/a/b/c/d") == ["d"]
    assert fs.ls("/a/b/c") == ["d"]
    assert fs.ls("/a/b") == ["c"]
    assert fs.ls("/a") == ["b"]
    assert fs.ls("/") == ["a"]


def test_multiple_files_and_dirs():
    fs = FileSystem()
    fs.mkdir("/a/b")
    fs.addContentToFile("/a/b/file1", "1")
    fs.addContentToFile("/a/b/file2", "2")
    fs.mkdir("/a/b/dir1")
    fs.addContentToFile("/a/b/dir1/file3", "3")
    assert sorted(fs.ls("/a/b")) == ["dir1", "file1", "file2"]
    assert fs.ls("/a/b/dir1") == ["file3"]


def test_file_overwrite_and_read():
    fs = FileSystem()
    fs.addContentToFile("/f", "abc")
    fs.addContentToFile("/f", "def")
    assert fs.readContentFromFile("/f") == "abcdef"


def test_ls_root_empty():
    fs = FileSystem()
    assert fs.ls("/") == []


def test_ls_nonexistent_path():
    fs = FileSystem()
    with pytest.raises(Exception):
        fs.ls("/no/such/path")


def test_read_nonexistent_file():
    fs = FileSystem()
    with pytest.raises(Exception):
        fs.readContentFromFile("/no/file")


def test_add_file_creates_dirs():
    fs = FileSystem()
    fs.addContentToFile("/x/y/z/file", "data")
    assert fs.readContentFromFile("/x/y/z/file") == "data"
    assert fs.ls("/x/y/z") == ["file"]


def test_nested_mkdir():
    fs = FileSystem()
    fs.mkdir("/a/b/c/d/e/f")
    assert fs.ls("/a/b/c/d/e") == ["f"]
    assert fs.ls("/a/b/c/d/e/f") == []
