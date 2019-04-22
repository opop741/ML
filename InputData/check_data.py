# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import pandas as pd

# 传入的参数pd_data必须是pandas的DataFrame
def check_NaN(pd_data):
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

    return {'data_info':data_info,
            'NaN_row_list':NaN_row_list,
            'NaN_column_list':NaN_column_list,
            'NaN_rows_dict':NaN_rows_dict
            }
