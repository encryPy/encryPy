# Author: Prosper Chuks
# License: MIT

import base64
import pandas as pd
import numpy as np

class base:

    def __init__(self) -> None:

        try:
            self.encoded_lst = []
            self.encoded_arr = []
        except: 
            raise NotImplementedError

    def encode(self, path: str=None, dataframe: pd.DataFrame=None) -> pd.DataFrame:

        if not path==None:

            self.bin =  pd.read_csv(path)
            for r in range(len(self.bin)):
                row = self.bin.loc[r]

                for k, v in enumerate(row.T):
                    code = base64.b64encode(bytes(str(v).encode('ascii')))
                    self.encoded_lst.append(code)

                    if len(self.encoded_lst) == len(self.bin.columns):
                        store = {
                            (int(n_row) for n_row in range(k)): np.array([a for a in self.encoded_lst])
                            }
                        self.encoded_arr.append(pd.DataFrame(store).T)
                        self.encoded_lst = []
            encoded_arr_np = np.concatenate(self.encoded_arr)
            return pd.DataFrame(encoded_arr_np)
            
        elif not dataframe.empty :
            
            self.bin =  pd.DataFrame(dataframe)
            for n_row in range(len(self.bin)):
                row = self.bin.loc[n_row]

                for k, v in enumerate(row.T):
                    code = base64.b64encode(bytes(str(v).encode('ascii')))
                    self.encoded_lst.append(code)

                    if len(self.encoded_lst) == len(self.bin.columns):
                        store = {
                            (int(n_row) for n_row in range(k)): np.array([a for a in self.encoded_lst])
                            }
                        self.encoded_arr.append(pd.DataFrame(store).T)
                        self.encoded_lst = []
            encoded_arr_np = np.concatenate(self.encoded_arr)
            return pd.DataFrame(encoded_arr_np)
            
        self.bin = pd.read_csv(path)
        for n_row in range(len(self.bin)):
            row = self.bin.loc[n_row]

            for k, v in enumerate(row.T):
                code = base64.b64encode(bytes(str(v).encode('ascii')))
                self.encode_lst.append(code)

                if len(self.encode_lst) == len(self.bin.columns):
                    store = {
                        (int(n_row) for n_row in range(k)): np.array([a for a in self.encode_lst])
                        }
                    self.encoded_arr.append(pd.DataFrame(store).T)
                    self.encode_lst = []
        encoded_arr_np = np.concatenate(self.encoded_arr)

        return pd.DataFrame(encoded_arr_np, columns=self.bin.columns)
