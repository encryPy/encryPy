# Author: Prosper Chuks
# License: MIT

from typing import List
import math


def split_len(seq, length) -> List:
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(self, key, message)->str:
    
    self.order = {
        int(val): num for num, val in enumerate(key)
    }
    self.ciphertext = ''

    for index in sorted(self.order.keys()):
        for part in split_len(message, len(key)):
            try:
                self.ciphertext += part[self.order[index]]
            except IndexError:
                continue
    return self.ciphertext

def encrypt(self, key, message)->str:

    self.ciphertext = [''] * key
    for col in range(key):
        self.position = col
        while self.position < len(message):
            self.ciphertext[col] += message[self.position]
            self.position += key
    return ''.join(self.ciphertext)

def decrypt(self, key, message)->str:

    numOfColumns = math.ceil(len(message) / key)
    numOfShadedBoxes = (numOfColumns * key) - len(message)
    decrypted_message = float() * numOfColumns
    col=0;row=0
    for symbol in message:
        decrypted_message[col] += symbol
        col += 1
        if col == numOfColumns or col == numOfColumns-1 & row >= key - numOfShadedBoxes:
            col = 0
            row += 1
    return ''.join(decrypted_message)
