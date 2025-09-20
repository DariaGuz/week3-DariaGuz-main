"""
Задача 12. FileSystem

Реализуйте класс FileSystem, поддерживающий работу с виртуальной файловой системой:
- mkdir(path): создать директорию по пути (например, "/a/b/c"). Все промежуточные директории должны быть созданы.
- addContentToFile(filePath, content): добавить content в файл filePath. Если файл не существует — создать.
- readContentFromFile(filePath): вернуть содержимое файла.
- ls(path): если path — файл, вернуть [имя файла], если директория — вернуть отсортированный список файлов и директорий внутри.

Пример:
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
assert fs.ls("/") == ["a"]
assert fs.ls("/a/b/c") == ["d"]
assert fs.readContentFromFile("/a/b/c/d") == "hello"
"""


class FileSystem:
    def __init__(self):
        pass

    def ls(self, path: str) -> list[str]:
        pass

    def mkdir(self, path: str) -> None:
        pass

    def addContentToFile(self, filePath: str, content: str) -> None:
        pass

    def readContentFromFile(self, filePath: str) -> str:
        pass
