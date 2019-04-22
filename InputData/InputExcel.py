# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import pandas as pd
import numpy as np
header = 0
index_col = 0

pd_data = pd.read_excel(r"D:\py_projects\ML\data\test.xlsx",header=header,index_col=index_col)

columns_info_list = []
isNaN_columns_dict = dict(pd_data.isna().any(0)) # isnull与isna是一样的，前者都用后者
for i in pd_data.columns:
    columns_info_list.append([i,pd_data[i].dtype,isNaN_columns_dict[i]])
data_info = pd.DataFrame(columns_info_list,columns=('columns','dtype','NaN_column'))

# 空行
NaN_row_list = pd_data.index[pd_data.isna().any(1) == True].tolist()

# 空列
NaN_column_list = data_info['columns'][data_info['NaN_column']].tolist()

# 有空列的空行
NaN_rows_dict = {}
for i in NaN_column_list:
    NaN_rows_dict[i] = pd_data.index[pd_data[i].isna() == True].tolist()


print(data_info)
print(NaN_row_list)
print(NaN_column_list)
print(NaN_rows_dict)




