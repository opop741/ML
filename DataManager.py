# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

from InputData.check_data import check_null
import pandas
from inspect import isfunction

class DataProcedure():
    data_file_path = ""

    # 检查数据哪些字段有缺失值
    check_null = check_null

    # 利用属性来返回读取DataFrame方法
    _get_data_method = {"read_csv":pandas.read_csv,
                       "read_excel":pandas.read_excel,
                       "read_json":pandas.read_json,
                       "read_pickle":pandas.read_pickle,
                       "read_html":pandas.read_html,
                       "read_sql":pandas.read_sql}
    def __getattr__(self, item):
        return self._get_data_method[item]

    # # 读取DataFrame方法的装饰器
    # def io_add(func):
    #     def inner_function(*param, **params):
    #         # import pandas
    #         _get_data_method = {"read_csv": pandas.read_csv,
    #                             "read_excel": pandas.read_excel,
    #                             "read_json": pandas.read_json,
    #                             "read_pickle": pandas.read_pickle,
    #                             "read_html": pandas.read_html,
    #                             "read_sql": pandas.read_sql}
    #         if isinstance(param, tuple):
    #             if isinstance(param[0], str):
    #                 file_path = param[0]
    #         elif isinstance(params, dict):
    #             file_path = params['io']
    #         pd_data = _get_data_method[func.__name__](*param, **params)
    #     return inner_function
    #
    # @io_add
    # def read_csv():
    #     pass
    #
    # @io_add
    # def read_excel():
    #     pass
    #
    # @io_add
    # def read_json():
    #     pass
    #
    # @io_add
    # def read_pickle():
    #     pass
    #
    # @io_add
    # def read_html():
    #     pass
    #
    # @io_add
    # def read_sql():
    #     pass

    # 数据处理流程list
    all_procedure = []

    # 将前一步骤的dataframe和处理函数传入，处理函数将对dataframe处理得到新的数据集合
    def register(self,function,parameter,function_info=None):
        assert isfunction(a),'function必须要是函数'
        assert isinstance(parameter,(tuple,dict)),'处理函数的参数必须使用tuple/dict包起来'
        assert execute_function_and_return in set(1,0,True,False),'必须是0/1/Boolean'
        self.all_procedure[len(self.all_procedure)] =  {'function':function,
                                                'function_name':function.__name__,
                                                'function_info':function_info,
                                                'parameter':parameter,}

    # 将每一个步骤的信息打印出来
    def print_procedure(self):
        for index,procedure_i in enumerate(self.all_procedure):
            print('Step' + index + ':')
            print('\t','function:', procedure_i['function_name'] + '-->' + procedure_i['function'])
            print('\t','parameter:',procedure_i['parameter'])
            print('\t','function_info:',procedure_i['function_info'])
            if 'output_dataframe' in procedure_i:
                print('\t','output_dataframe:',procedure_i['input_dataframe'])

    # 运行某些数据处理步骤，必须连贯区间
    def execute_procedure(self,input_dataframe,start,end):
        assert isinstance(input_dataframe,pandas.DataFrame),'输入数据必须是pandas.DataFrame'
        assert isinstance(start,int) and isinstance(end,int), '步骤的index必须是int数据类型'
        procedure_order = self.all_procedure[start:end]
        for index,procedure_i in enumerate(procedure_order):
            if isinstance(procedure_i['parameter'],tuple):
                parameter_i = procedure_i['parameter']
            if index == 0:
                if isinstance(parameter_i,tuple):
                    out_dataframe = procedure_i['function'](input_dataframe,*parameter_i)
                elif isinstance(parameter_i,dict):
                    out_dataframe = procedure_i['function'](input_dataframe,**parameter_i)
                procedure_i['out_dataframe'] = out_dataframe
            else:
                if isinstance(parameter_i, tuple):
                    out_dataframe = procedure_i['function'](procedure_order[index - 1]['out_dataframe'],parameter_i)
                elif isinstance(parameter_i, dict):
                    out_dataframe = procedure_i['function'](procedure_order[index - 1]['out_dataframe'],parameter_i)
                procedure_i['out_dataframe'] = out_dataframe
        return out_dataframe

    # 运行所有处理步骤
    def execute_procedure_all(self,input_dataframe):
        execute_procedure(self,input_dataframe,0,len(self.all_procedure))

