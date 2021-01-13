""""Helper Function"""

import numpy as np
import pandas as pd

#df = [0,1,2,0,7,1,4,1,4,3,7,2,2,1,7]
#seed = 101

def null_count(df):
    temp_sum = 0
    for i in range(0, len(df.index)):
        temp_sum += df.iloc[i].isnull().sum()
    return temp_sum

def train_test_split(df, frac): 
    train=df.sample(frac=frac)
    test=df.drop(train.index)
    return train, test

