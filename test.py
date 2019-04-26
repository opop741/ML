# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import pandas


class test:
    def io_add(func):
        def inner_function(self,*param,**params):
            # import pandas
            print(self,param,params)
            _get_data_method = {"read_csv": pandas.read_csv,
                                "read_excel": pandas.read_excel,
                                "read_json": pandas.read_json,
                                "read_pickle": pandas.read_pickle,
                                "read_html": pandas.read_html,
                                "read_sql": pandas.read_sql}
            if isinstance(param,tuple) and param != ():
                if isinstance(param[0],str):
                    file_path = param[0]
            elif isinstance(params,dict):
                file_path = params['io']
            pd_data = _get_data_method[func.__name__](*param,**params)
            print('\n',file_path)
            print('\n',pd_data)
        return inner_function


    @io_add
    def read_csv(self):
        pass

    @io_add
    def read_excel(self):
        pass

    @io_add
    def read_json(self):
        pass

    @io_add
    def read_pickle(self):
        pass

    @io_add
    def read_html(self):
        pass

    @io_add
    def read_sql(self):
        pass

test1 = test()
# test.read_excel(r".\data\test.xlsx",header=0,index_col=0) #加了self就变成实例的方法，所以用类.实例方法时不会传入self，所以与装饰器不匹配，会报错
test1.read_excel(r".\data\test.xlsx",header=0,index_col=0) #self加了