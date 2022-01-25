# Author: Prosper Chuks
# License: MIT

from typing import Any
import pandas as pd
import numpy as np


def xor():
    pass

def _xor_process(data, key) -> Any:
    
    '''
    This method is a 2-way processor
    '''
    
    data_len = len(data)
    for c in range(data_len):
        data = (data[:c] +chr(ord(data[c]) ^ ord(key)) + data[c+1:])
    
    return data

def encrypt_data(key, path: str=None, dataframe: pd.DataFrame=None) -> pd.DataFrame:

    '''

    This function encrypts the provided dataset.

    Example
    -------
    >>> from encrypy.or import xor
    >>> encoded_data = base.encrypt_data(path, dataframe)

    path: str, default = None
        Path parameter should hold the path to the dataset.

    or

    dataframe: pd.DataFrame, default = None
        An initialized pandas DataFrame can be passed as an argument.

    Returns:
        DataFrame Object

    '''

    encrypt_lst = []
    encrypt_arr = []

    if not path==None:

        bin =  pd.read_csv(path)
        bin = bin.astype(str)
        for r in range(len(bin)):
            row = bin.loc[r]

            for k, v in enumerate(row.T):
                code = _xor_process(v, key)
                encrypt_lst.append(code)

                if len(encrypt_lst) == len(bin.columns):
                    store = {
                        (int(n_row) for n_row in range(k)): np.array([a for a in encrypt_lst])
                        }
                    encrypt_arr.append(pd.DataFrame(store).T)
                    encrypt_lst = []
        encoded_arr_np = np.concatenate(encrypt_arr)
        return pd.DataFrame(encoded_arr_np, columns=bin.columns)
        
    elif not dataframe.empty :
        
        bin =  pd.DataFrame(dataframe)
        bin = bin.astype(str)
        for n_row in range(len(bin)):
            row = bin.loc[n_row]

            for k, v in enumerate(row.T):
                code = _xor_process(v, key)
                encrypt_lst.append(code)

                if len(encrypt_lst) == len(bin.columns):
                    store = {
                        (int(n_row) for n_row in range(k)): np.array([a for a in encrypt_lst])
                        }
                    encrypt_arr.append(pd.DataFrame(store).T)
                    encrypt_lst = []
        encoded_arr_np = np.concatenate(encrypt_arr)
        return pd.DataFrame(encoded_arr_np, columns=bin.columns)

def decrypt_data(key, dataframe: pd.DataFrame) -> pd.DataFrame:

    '''

    This function decrypts the encrypted dataset.

    Example
    -------
    >>> from encrypy.or import xor
    >>> dataset = base.decrypt_data(dataframe)

    dataframe: pd.DataFrame, default = None
        Initialized pandas DataFrame can be passed as an argument.

    Returns:
        DataFrame Object

    '''

    decrypted_lst = []
    decrypted_arr = []

    bin =  pd.DataFrame(dataframe)
    for n_row in range(len(bin)):
        row = bin.loc[n_row]

        for k, v in enumerate(row.T):
            code = _xor_process(v, key)
            decrypted_lst.append(code)

            if len(decrypted_lst) == len(bin.columns):
                store = {
                    (int(n_row) for n_row in range(k)): np.array([a for a in decrypted_lst])
                    }
                decrypted_arr.append(pd.DataFrame(store).T)
                decrypted_lst = []
    
    decrypted_arr_np = np.concatenate(decrypted_arr)

    return pd.DataFrame(decrypted_arr_np.astype(str), columns=bin.columns)

