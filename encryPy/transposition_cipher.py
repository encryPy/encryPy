# Author: Prosper Chuks
# License: MIT

import string
from typing import List


def split_len(seq, length) -> List:
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(self, key, plaintext) -> string:
    
    self.order = {
        int(val): num for num, val in enumerate(key)
    }
    self.ciphertext = ''

    for index in sorted(self.order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                self.ciphertext += part[self.order[index]]
            except IndexError:
                continue
    return self.ciphertext

def encrypt(self, key, message) -> string:

    self.ciphertext = [''] * key
    for col in range(key):
        self.position = col
        while self.position < len(message):
            self.ciphertext[col] += message[self.position]
            self.position += key
    return ''.join(self.ciphertext)

def decrypt(self, message):
    pass
