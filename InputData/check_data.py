# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import pandas as pd

# 传入的参数pd_data必须是pandas的DataFrame，返回的数据是dict。
def check_null(pd_data):
    columns_info_list = []
    isnull_columns_dict = dict(pd_data.isnull().any(0)) # 有些版本isnull调用isna，有些版本没有isna，所以用isnull
    for i in pd_data.columns:
        columns_info_list.append([i,pd_data[i].dtype,isnull_columns_dict[i]])
    data_info = pd.DataFrame(columns_info_list,columns=('columns','dtype','null_column'))

    # 空行
    NaN_row_list = pd_data.index[pd_data.isnull().any(1) == True].tolist()

    # 空列
    NaN_column_list = data_info['columns'][data_info['null_column']].tolist()

    # 有空列的空行
    NaN_rows_dict = {}
    for i in NaN_column_list:
        NaN_rows_dict[i] = pd_data.index[pd_data[i].isnull() == True].tolist()

    return {'data_info':data_info,
            'null_row_list':NaN_row_list,
            'null_column_list':NaN_column_list,
            'null_rows_dict':NaN_rows_dict
            }
