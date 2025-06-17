import os
from cryptography.fernet import Fernet
def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    with open(filename, "wb") as file:
        file.write(key)

def load_key(filename="secret.key"):
    with open(filename, "rb") as file:
        return file.read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)

    # Remove ".enc" from the file name
    if file_path[-4:] == ".enc":
         output_file = file_path[:-4]  # removes '.enc'
    else:
        output_file = file_path + ".dec"

    with open(output_file, "wb") as file:
        file.write(decrypted)

    return output_file