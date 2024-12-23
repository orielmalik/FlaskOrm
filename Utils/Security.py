from cryptography.fernet import Fernet
from Utils.FileUtils import *

key = Fernet.generate_key()
f = Fernet(key)


def encrypt_message(message):
    return f.encrypt(bytes(message, 'utf-8'))

def decrypt_message(message):
    return f.decrypt(message)

def encrypt_file(file_name, directory="Queries"):
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
        encrypted_file_path = file_path + ".enc"

        with open(encrypted_file_path, "w", encoding="utf-8") as enc_file:
            enc_file.write(encrypted_content)

        print("File encrypted successfully.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    result = encrypt_file('Create.txt',"Queries")
    if result:
        print("File encrypted successfully.")
    else:
        print("File encryption failed.")