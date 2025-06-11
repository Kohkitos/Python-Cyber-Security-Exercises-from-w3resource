"""
2. Random Password Generator
    Write a Python program that defines a function to generate random passwords of a specified length. The function takes an optional parameter length, which is set to 8 by default. If no length is specified by the user, the passwork will have 8 characters.
"""
import secrets
import string

def password_generator(length=8):
    try:
        length = int(length)
    except ValueError:
        length = 8
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range (length))
    return password

def main():
    length = input("Input the length of password (leave empty for 8):")
    password = password_generator(length)
    print (password)

if __name__ == "__main__":
    main()