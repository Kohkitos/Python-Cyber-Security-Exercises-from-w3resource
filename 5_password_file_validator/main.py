"""
5. Password File Validator
Write a Python program that reads a file containing a list of passwords, one per line. It checks each password to see if it meets certain requirements (e.g. at least 8 characters, contains both uppercase and lowercase letters, and at least one number and one special character). Passwords that satisfy the requirements should be printed by the program.
"""

import  string
import  os

def is_valid_password(password):
    """Checks if a password fulfills the following criteria:
        - At least 8 characters long.
        - Contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, or &).

    Args:
        password (str): the password to check.

    Returns:
        int: 1 if valid, 0 if not.
    """

    length_flag = len(password) >= 8
    upper_flag = lower_flag = digit_flag = special_flag = 0
    special_characters = "!@#$%&"

    for c in password:
        if not upper_flag and c in string.ascii_uppercase:
            upper_flag = 1
        elif not lower_flag and c in string.ascii_lowercase:
            lower_flag = 1
        elif not digit_flag and c in string.digits:
            digit_flag = 1
        elif not special_flag and c in special_characters:
            special_flag = 1

        # Early exit if all flags are True
        if all([upper_flag, lower_flag, digit_flag, special_flag]):
            break

    if all([length_flag, upper_flag, lower_flag, digit_flag, special_flag]):
        return 1
    else:
        return 0
    
def password_file_validator(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    passwords = content.split()

    valid_passwords = []
    for password in passwords:
        if is_valid_password(password):
            valid_passwords.append(password)

    print(valid_passwords)

def main():
    filepath = "./passwords.txt"
    filepath = os.path.expanduser(filepath)
    password_file_validator(filepath)

if __name__ == "__main__":
    main()