import base64

from cryptography.fernet import Fernet
from Utils.FileUtils import *


# יצירת מפתח חדש ושמירה בקובץ
def encpsulate_key():
    key = Fernet.generate_key()  # מפתח חדש
    writeExistTextFile(content=key.decode('utf-8'), file_name="gary.txt")  # שמירה כטקסט (במקום bytes)

def f():
    key = readTextFile("gary.txt").encode('utf-8')
    return Fernet(key)

def fix_padding(encoded_str):
    missing_padding = len(encoded_str) % 4
    if missing_padding:
        encoded_str += "=" * (4 - missing_padding)
    return encoded_str


def encrypt_message(message):
    return f.encrypt(bytes(message, 'utf-8'))


def decrypt_message(message):
    return f().decrypt(message.encode('utf-8'))


def encrypt_file(file_name, directory="."):
    file_path = os.path.join(directory, file_name)

    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return False

    if not os.path.isfile(file_path):
        print(f"File '{file_name}' not found in directory '{directory}'.")
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        encrypted_content = content[::-1]
        encrypted_file_path = file_path
        print(encrypted_content)
        with open(encrypted_file_path, "w", encoding="utf-8") as enc_file:
            enc_file.write(encrypted_content)

        print("File encrypted successfully.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


