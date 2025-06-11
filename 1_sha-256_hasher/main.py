"""
1. SHA-256 Hasher
    Write a Python program tha defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.
"""

import  hashlib

def password_hasher_sha256(password):
    """Hashes a plaintext password using SHA-256.

    Args:
        password (str): The plaintext password to hash.

    Raises:
        TypeError: if the input is not a string.

    Returns:
        str: the SHA-256 hashed password represented as a hexadecimal string.
    """

    if not isinstance(password, str):
        raise TypeError("Input must be a string")

    hasher = hashlib.sha256(password.encode())
    hashed_pass = hasher.hexdigest()
    return hashed_pass

def main():
    password = input("Enter something to hash: ")
    hashed_pass = password_hasher_sha256(password)
    print(f"Your hashed password: {hashed_pass}")

if __name__ == "__main__":
    main()