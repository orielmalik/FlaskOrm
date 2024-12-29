import json
import os
from Keys.Security import decrypt_message
from Utils.const import key


def readTextFile(file_name, search_root="."):
    return decrypt_message(readTextFileReg(search_root=search_root, file_name=file_name))


def readTextFileReg(file_name, search_root="."):
    for root, dirs, files in os.walk(search_root):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as file:
                    return file.read()
            else:
                print(f"File found but is not a text file: {file_path}")
                return ""
    print(f"File '{file_name}' not found in directory '{search_root}'")
    return ""


def writeExistTextFile(file_name, search_root=".", content=""):
    """
    Writes content to an existing text file or creates a new one if it doesn't exist.

    Args:
        file_name (str): Name of the file to search and write to.
        search_root (str): Directory to start the search.
        content (str): Content to write into the file.

    Returns:
        bool: True if the operation succeeded, False otherwise.
    """
    if not isinstance(content, str):
        print("Content must be a string.")
        return False

    try:
        # Traverse directories to find the file
        for root, dirs, files in os.walk(search_root):
            if file_name in files:
                file_path = os.path.join(root, file_name)
                if file_path.endswith(".txt"):
                    # Write to the existing file
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(content)
                    print(f"Content written to existing file: {file_path}")
                    return True
                else:
                    print(f"File found but is not a text file: {file_path}")
                    return False

        # If file not found, create it in the search root directory
        new_file_path = os.path.join(search_root, file_name)
        with open(new_file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"New file created and content written: {new_file_path}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


def insertJson(dir_):
    with open(dir_, "r", encoding="utf-8") as file:
        print(dir_)
        return json.load(file)
