# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import numpy as np
import pandas as pd

random_seed = 666

data1 = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
data2 = np.ones((5,5))
assert isinstance(data1,(pd.DataFrame,np.ndarray)),\
    "Only accept pandas dataframe，numpy array must trun to dataframe."
print(data1.sample(2),'\n')


start_row = None
end_row = None
row_interval = None
start_col = None
end_col = None
col_interval = None

pd_data.loc[start_row:end_row:row_interval,start_col:end_col:col_interval]



train_x = 0.8
train_y = 0.8
test_x = 0.2
test_y = 0.2
verify_x = 0
verify_y = 0

