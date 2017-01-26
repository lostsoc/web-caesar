import string

def encrypt(letter, rot):
    encrypted = ""
    for char in letter:

        if char in string.ascii_lowercase:
            char_index = int(string.ascii_lowercase.index(char))
            newchar_index = char_index + rot
            encrypted = encrypted + string.ascii_lowercase[newchar_index % 26]

        if char in string.ascii_uppercase:
            Char_Index = int(string.ascii_uppercase.index(char))
            NewChar_Index = Char_Index + rot
            encrypted = encrypted + string.ascii_uppercase[NewChar_Index % 26]

        elif char not in string.ascii_lowercase and string.ascii_uppercase:
            encrypted = encrypted + char
    return encrypted
