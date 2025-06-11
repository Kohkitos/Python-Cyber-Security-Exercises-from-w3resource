"""
3. Password Criteria Checker
    Write a Python program to check if a password meets the following criteria:
        + At least 8 Character long
        + Contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, or &)
"""

import  string

def password_checker(password):

    length_flag = len(password) >= 8
    upper_flag = lower_flag = digit_flag = special_flag = 0
    special_characters = "!@#$%&"

    for c in password:
        if not upper_flag and c in string.ascii_uppercase:
            upper_flag = 1
        if not lower_flag and c in string.ascii_lowercase:
            lower_flag = 1
        if not digit_flag and c in string.digits:
            digit_flag = 1
        if not special_flag and c in special_characters:
            special_flag = 1

        # Early exit if all flags are True
        if all([upper_flag, lower_flag, digit_flag, special_flag]):
            break

    if all([length_flag, upper_flag, lower_flag, digit_flag, special_flag]):
        return "Is Valid!"
    else:
        return "Not a valid password :("

def main():
    while True:
        password = input("Enter a password to check:").split()
        if password:
            break
    print (password_checker(password[0]))

if __name__ == "__main__":
    main()