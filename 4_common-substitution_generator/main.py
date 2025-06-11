"""
4. Common Substitution Generator
    Write a Python function that takes a password as input and returns a list of common character substitutions that could be used to create a stronger password. 
"""

import  itertools

def commmon_substitution_generator(password):
    """Generates a list of password suggestions by substituting alphabetical characters with common LEET equivalents, including the original characters.

    Note: For real security, multi-factor authentication (MFA) is recommended.

    Args:
        password (str): The password to check and offer suggestions.
    """

    leet_substitutions = {
        'a': ['4', '@'],
        'b': ['8'],
        'c': ['(', '<'],
        'd': [')'],
        'e': ['3'],
        'f': ['ph'],
        'g': ['6', '9'],
        'h': ['#'],
        'i': ['1', '!', '|'],
        'j': [']'],
        'k': ['|<'],
        'l': ['1', '|', '7'],
        'm': ['^^'],
        'n': ['^/'],
        'o': ['0'],
        'p': ['9'],
        'q': ['0_', '9'],
        'r': ['2'],
        's': ['5', '$'],
        't': ['7', '+'],
        'u': ['(_)'],
        'v': ['\\/'],
        'w': ['\\/\\/', 'vv'],
        'x': ['%', '><'],
        'y': ['`/'],
        'z': ['2']
    }

    chars_options = []
    for c in password:
        if c.lower() in leet_substitutions:
            # Include the original character and all substitutions
            options = [c] + leet_substitutions[c.lower()]
        else:
            options = [c]
        chars_options.append(options)

    all_combinations = itertools.product(*chars_options)

    suggested_passwords = [''.join(combo) for combo in all_combinations]
                
    print (suggested_passwords)

def main():
    while True:
        password = input("Enter a password to check:").split()
        if password:
            break

    commmon_substitution_generator(password[0])

if __name__ == "__main__":
    main()