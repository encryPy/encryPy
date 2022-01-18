# Author: Prosper Chuks
# License: MIT

import pandas as pd
import numpy as np


def xor():
    pass

def _xor_process(data, key):
    ''' '''
    data_len = len(data)
    for c in range(data_len):
        data = (data[:c] +chr(ord(data[c]) ^ ord(key)) + data[c+1:])
    
    return data

def encrypt_data():
    pass

def decrypt_data():
    pass
