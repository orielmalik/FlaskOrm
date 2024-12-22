
import os


def readTextFile(file_name, search_root="."):
    for root, dirs, files in os.walk(search_root):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            # בודקים את סיומת הקובץ
            if file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as file:
                    return file.read()
            else:
                return f"File found but is not a text file: {file_path}"

    return f"File '{file_name}' not found in directory '{search_root}'"


def writeTextFile(file_name, search_root=".",content=""):
    if  not isinstance(content,str):
        return  False

    for root, dirs, files in os.walk(search_root):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            # בודקים את סיומת הקובץ
            if file_path.endswith(".txt"):
                with open(file_path, "w", encoding="utf-8") as file:
                     file.write(content)
                return True
            else:
                return False
