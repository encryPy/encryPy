# Author: Prosper Chuks
# License: MIT

from typing import List
import math


def _split_len(seq, length) -> List:
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(self, key, message)->str:
    
    self.order = {
        int(val): num for num, val in enumerate(key)
    }
    self.ciphertext = ''

    for index in sorted(self.order.keys()):
        for part in _split_len(message, len(key)):
            try:
                self.ciphertext += part[self.order[index]]
            except IndexError:
                continue
    return self.ciphertext


def encrypt(self, key, message) -> str:

    '''
    This function encrypts the provided message.

    Example
    -------
    >>> import encrypy.transposition_cipher as tp
    >>> encrypted_data = tp.encrypt(key='TESGIN', message='Encrypt Python')

    key: str, default = ''
    Specifies the order in which to arrange the columns. This parameter 
        cannot take more than 8 chars. Characters must be unique.

    message: str, default = ''
        Data to be encrypted.

    Returns:
        string
    '''
    
    self.cipher = ''
    self.key_index = 0
    self.message_length = float(len(message))
    self.message_list = list(message)
    self.key_list = sorted(list(key))

    self.col = len(key)
    self.row = int(math.ceil(self.message_length / self.col))

    fill_null = int((self.row * self.col) - self.message_length)
    self.message_list.extend('_' * fill_null)

    matrix = [self.message_list[i: i + self.col] 
            for i in range(0, len(self.message_list), self.col)]

    for _ in range(self.col):
        curr_idx = key.index(self.key_list[self.key_index])
        self.cipher += ''.join([self.row[curr_idx] 
                        for self.row in matrix])
        self.key_index += 1

    return self.cipher
        
def decrypt(self, key, cipher) -> str:

    '''
    This function decrypts the provided encrypted message.

    Example
    -------
    >>> import encrypy.transposition_cipher as tp
    >>> text = tp.decrypt(key='TESGIN', message='Encrypt Python')

    key: str, default = ''
    Specifies the order in which to arrange the columns.

    message: str, default = ''
        Data to be decrypted.

    Returns:
        string

    Warnings
    --------
    -  ``decrypt(key)`` parameter must match with ``encrypt(key)``.
    '''
    
    self.message = ''
    self.key_index = 0
    self.message_index = 0
    self.message_length = float(len(cipher))
    self.message_list = list(cipher)

    self.col = len(key)
    self.row = int(math.ceil(self.message_length / self.col))
    self.key_list = sorted(list(key))

    dec_cipher = []
    for _ in range(self.row):
        dec_cipher += [[None] * self.col]

    for _ in range(self.col):
        curr_idx = key.index(self.key_list[self.key_index])

        for j in range(self.row):
            dec_cipher[j][curr_idx] = self.message_list[self.message_index]
            self.message_index += 1
        self.key_index += 1

    try:
        self.message = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = self.message.count('_')

    if null_count > 0:
        return self.message[: -null_count]

    return self.message

