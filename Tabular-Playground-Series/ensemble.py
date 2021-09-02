#!/usr/bin/python3

import glob
import numpy as np
import pandas as pd

def majority(dir_path, target_col, high, id_col='id'):
    merged_output = pd.DataFrame()

    for fname in glob.glob(dir_path+'/*.csv'):
        output = pd.read_csv(fname, index_col=id_col)
        merged_output[fname] = output[target_col]

    mode = merged_output.mode(axis=1)

    merged_output[target_col] = np.where(mode.isna().any(1), mode[0], merged_output[high])

    return merged_output[target_col].reset_index()

if __name__ == '__main__':
    majority('./Sep-2021', 'claim', './Sep-2021/output_xgb.csv').to_csv('output.csv', index=False)