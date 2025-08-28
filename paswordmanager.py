from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

def write_key():
    key = os.urandom(16)   # random salt
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        write_key()   # auto create if not present
    with open("key.key", "rb") as key_file:
        return key_file.read()

master_pwd = input("What is the master password? ")

salt = load_key()
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
fer = Fernet(key)

def view():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet.")
        return
    with open('password.txt', 'r') as r:
        for line in r.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print("Password saved successfully.")

def update():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet.")
        return
    account = input("Enter the account name to update: ")
    lines = []
    found = False
    with open("password.txt", "r") as f:
        lines = f.readlines()
    with open("password.txt", "w") as f:
        for line in lines:
            user, passw = line.strip().split("|")
            if user == account:
                new_pwd = input("Enter new password: ")
                f.write(user + "|" + fer.encrypt(new_pwd.encode()).decode() + "\n")
                found = True
                print("Password updated successfully.")
            else:
                f.write(line)
    if not found:
        print("Account not found.")

def delete():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet.")
        return
    account = input("Enter the account name to delete: ")
    lines = []
    found = False
    with open("password.txt", "r") as f:
        lines = f.readlines()
    with open("password.txt", "w") as f:
        for line in lines:
            user, passw = line.strip().split("|")
            if user == account:
                found = True
                print("Password deleted successfully.")
                continue
            f.write(line)
    if not found:
        print("Account not found.")

def search():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet.")
        return
    account = input("Enter the account name to search: ")
    found = False
    with open("password.txt", "r") as f:
        for line in f.readlines():
            user, passw = line.strip().split("|")
            if user == account:
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
                found = True
                break
    if not found:
        print("Account not found.")

while True:
    mode = input("\nChoose an option: add, view, update, delete, search, q (quit): ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "update":
        update()
    elif mode == "delete":
        delete()
    elif mode == "search":
        search()
    else:
        print("INVALID option.")
