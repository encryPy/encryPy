# Author: Prosper Chuks
# License: MIT


def __init__(self) -> None:
    self.KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(self, message, shift=0) -> str:

    '''
    This function encrypts the provided message.

    Example
    -------
    >>> import encrypy.ceasar_cipher as cp
    >>> encrypted_data = cp.encrypt(message, shift)

    message: str, default = ''
        Data to be encrypted.

    shift: int, default = 0
        Determines the length at which each letter of the message is shifted.

    Returns:
        string
    '''

    self.result = ''

    for c in range(len(message)):
        self.char = message[c]

        if self.char.isupper():
            self.result += chr(ord(self.char) + shift - 65 % 26 + 65)
        else:
            self.result += chr(ord(self.char) + shift - 97 % 26 + 97)
    return self.result

def brute_force(self, message) -> None:

    '''
    This function decrypts a ciphered/encrypted message using a brute-force technique.

    Example
    -------
    >>> import encrypy.ceasar_cipher as cp
    >>> encrypted_data = cp.decrypt(message)

    message: str, default = ''
        Encrypted Data.
    '''

    for key in range(len(self.KEY)):
        decrypted_message = ''
        for symbol in message:
            if symbol in self.KEY:
                num = self.KEY.find(symbol)
                num -= key
                if num < 0:
                    num += len(self.KEY)
                decrypted_message += self.KEY[num]
            else:
                decrypted_message += symbol
                print('Brute key #%s: %s' % (key, decrypted_message))
