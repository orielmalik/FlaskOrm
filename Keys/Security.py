import os
from cryptography.fernet import Fernet

from Utils.const import key


# פונקציות להצפנה ופענוח
def f():
    return Fernet(key)

def encrypt_message(message):
    print(message)
    return f().encrypt(message.encode('utf-8'))

def decrypt_message(message):
    return f().decrypt(message).decode('utf-8')

def readTextFile(file_path):
    # קריאת תוכן הקובץ כ- string אחרי Decode
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"Reading from: {file_path}")
        return file.read()  # מחזיר מחרוזת רגילה

def write_key_from_file(encrypted_message, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        print(f"Writing to: {file_path}")
        print(encrypted_message.decode('utf-8'))  # הדפסת המידע המפוענח
        file.write(encrypted_message.decode('utf-8'))  # כותב את המידע כ- string

# תיקיית הפרויקט
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
queries_directory = os.path.join(project_dir, "Queries")






#for _file in os.listdir(queries_directory):
        #if _file.lower().endswith(".txt"):
            #write_key_from_file(encrypt_message(readTextFile(os.path.join(queries_directory, _file))),
                                #os.path.join(queries_directory, _file))



