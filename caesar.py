import string

def alphabet_position(letter):

        return string.ascii_lowercase.find(letter.lower())


def rotate_character(char, rot):
    if char.isupper():
        return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    elif char.islower():
        return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]
    else:
        return char


def encrypt(text, rot):
    encrypted_string = ""
    for achar in text:
        encrypted_string += rotate_character(achar, rot)
    return encrypted_string
