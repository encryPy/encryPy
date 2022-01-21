# Author: Prosper Chuks
# License: MIT

from typing import Any
import pyDes
import pandas as pd
import numpy as np


def _generate_key() -> pyDes.des:
    return pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

def _des(data, mode=None, key=_generate_key()) -> Any:
    
    if mode=='e':
        return key.encrypt(data)
    elif mode=='d':
        return key.decrypt(data)

def encrypt_data(path: str=None, dataframe: pd.DataFrame=None) -> pd.DataFrame:

    encrypt_lst = []
    encrypt_arr = []

    if not path==None:

        bin =  pd.read_csv(path)
        bin = bin.astype(str)
        for r in range(len(bin)):
            row = bin.loc[r]

            for k, v in enumerate(row.T):
                code = _des(str(v).encode('utf-8'), mode='e')
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
                code = _des(v)
                encrypt_lst.append(code)

                if len(encrypt_lst) == len(bin.columns):
                    store = {
                        (int(n_row) for n_row in range(k)): np.array([a for a in encrypt_lst])
                        }
                    encrypt_arr.append(pd.DataFrame(store).T)
                    encrypt_lst = []
        encoded_arr_np = np.concatenate(encrypt_arr)
        return pd.DataFrame(encoded_arr_np, columns=bin.columns)

def decrypt_data():
    pass
