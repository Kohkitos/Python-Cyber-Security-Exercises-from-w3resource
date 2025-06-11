"""
1. SHA-256 Hasher
    Write a Python program tha defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.
"""

import  hashlib

def password_hasher_sha256(password):
    # Create new hash object with sha256 algorithm
    hasher = hashlib.sha256(password.encode())
    # Save hashed password on a new string and return it
    hashed_pass = hasher.hexdigest()
    return hashed_pass

def main():
    password = input("Enter something to hash: ")
    hashed_pass = password_hasher_sha256(password)
    print(f"Your hashed password: {hashed_pass}")

if __name__ == "__main__":
    main()