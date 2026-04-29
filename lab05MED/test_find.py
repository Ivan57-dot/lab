import os
import pytest

def find_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                yield os.path.join(root, file)


def test_находит_txt():
    """Проверяет, что все найденные файлы имеют расширение .txt"""
    for file in find_files('.'):
        assert file.endswith('.txt')
        print(f"Найден: {file}")


def test_файлы_существуют():
    """Проверяет, что файлы реально существуют"""
    for file in find_files('.'):
        assert os.path.exists(file)