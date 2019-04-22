# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import pandas as pd
import bisect
import numpy as np

# pd_data = pd.read_excel(r"D:\py_projects\ML\data\test.xlsx",header=None,index_col=0)
def dummy_variable(pd_data=None,process_columns=None,dummy_variable_dict={}):
    if pd_data is None or not isinstance(pd_data,pd.DataFrame):
        raise ValueError("传入数据必须是pandas的DataFrame！")
    if process_columns is None or not isinstance(process_columns,(str,int)):
        raise ValueError("必须指定哑变量列名，且只能是str或int数据类型！")
    if  pd_data.isnull().any()[process_columns]:
        raise ValueError("指定的列不可有缺失值！")

    # 先将值去重
    values_set = set(pd_data[process_columns])

    # 去重后排序
    values_list = []
    for i in values_set:
        bisect.insort(values_list,i)

    # 去重后的长度
    values_list_len = len(values_list)

    # 用户不存入映射字典，则自动创建分类变量旧值与哑变量的映射字典
    if dummy_variable_dict == {}:
        dummy_variable_dict[values_list[0]] = [0 for i in range(values_list_len - 1)]
        for i,v in enumerate(values_list[1:]):
            dummy_variable_dict[v] = [1 if ii == i else 0 for ii in range(values_list_len - 1)]

    # 生成哑变量的列名称
    dummy_variable_columns = ['{}_dummy_variable_{}'.format(process_columns,iii + 1) for iii in range(values_list_len - 1)]

    # 生成哑变量数据
    array_data = np.array([dummy_variable_dict[v] for v in pd_data[process_columns]])

    # 将哑变量数据添加到传入的原数据(DataFrame)中
    for i,c in enumerate(dummy_variable_columns):
        pd_data[c] = array_data[:,i]


    return dummy_variable_dict,pd_data