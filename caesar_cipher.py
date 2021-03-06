import string


def caesar_enc(msg, shift=1):
    """ Encrypts a text using Caesar cipher.
    :param msg: A text to be encrypted as a string.
    :param shift: A number of alphabet shifts as an integer (default = 1).
    :return: Encrypted string.
    """
    if not isinstance(msg, str):
        raise Exception("Can't encrypt a non-string message")
    enc = ''
    for char in msg:
        if char.islower():
            char_idx = string.ascii_lowercase.find(char)
            enc += string.ascii_lowercase[(char_idx + shift) % 26]
        elif char.isupper():
            char_idx = string.ascii_uppercase.find(char)
            enc += string.ascii_uppercase[(char_idx + shift) % 26]
        else:
            enc += char
    return enc



def caesar_dec(msg, shift=1):
    """ Decrypts an encrypted text using Caesar cipher.
    :param msg: An encrypted text to be decrypted (as a string).
    :param shift: A number of alphabet shifts (as an integer ,default = 1).
    :return: Decrypted string.
    """
    if not isinstance(msg, str):
        raise Exception("Can't encrypt a non-string message")
    dec = ''
    for char in msg:
        if char.islower():
            char_idx = string.ascii_lowercase.find(char)
            dec += string.ascii_lowercase[(char_idx - shift) % 26]
        elif char.isupper():
            char_idx = string.ascii_uppercase.find(char)
            dec += string.ascii_uppercase[(char_idx - shift) % 26]
        else:
            dec += char
    return dec


if __name__ == '__main__':
    txt = input("Enter the message that you want to encrypt / decrypt: ")
    encrypted = caesar_enc(txt, 3)
    print('Encrypted text:', encrypted)
    print('Decrypted text:', caesar_dec(encrypted, 3))
