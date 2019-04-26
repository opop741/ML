# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

from InputData.check_data import check_null
import pandas
from inspect import isfunction

class DataProcedure():
    '''
        1、先用io_add_raw_***()读取原数据，方法自动将原数据的文件位置与读取的dataframe保存到实例对象属性data_file_path和raw_dataframe中
        2、本类的实例对象主要用于数据进入模型前的数据处理的流程管理
        3、通过自定义处理dataframe的函数传入流程中来明确处理步骤/顺序
        4、自定义处理dataframe的函数的形参格式必须要function必须要是函数，处理函数的参数必须使用tuple/dict包起来，execute_function_and_return必须是0/1/Boolean
        5、本类的实例化的对象的register(注册)函数用于将自定义的数据处理函数注册到all_procedure数组中，注册顺序必须要与数据处理步骤顺序一致
        6、execute_procedure()通过指定输入数据dataframe和数据处理步骤来自定义起、始点，all_procedure[0]是最早注册的数据处理步骤
        7、print_procedure()用于打印各数据处理步骤的信息
    '''

    # print(实例化对象)输出的字符串
    def __str__(self):
        summary = '''
            本实例对象的父类DataProcedure有以下特点
                1、先用io_add_raw_***()读取原数据，方法自动将原数据的文件位置与读取的dataframe保存到实例对象属性data_file_path和raw_dataframe中
                2、本类的实例对象主要用于数据进入模型前的数据处理的流程管理
                3、通过自定义处理dataframe的函数传入流程中来明确处理步骤/顺序
                4、自定义处理dataframe的函数的形参格式必须要function必须要是函数，处理函数的参数必须使用tuple/dict包起来，execute_function_and_return必须是0/1/Boolean
                5、本类的实例化的对象的register(注册)函数用于将自定义的数据处理函数注册到all_procedure数组中，注册顺序必须要与数据处理步骤顺序一致
                6、execute_procedure()通过指定输入数据dataframe和数据处理步骤来自定义起、始点，all_procedure[0]是最早注册的数据处理步骤
                7、print_procedure()用于打印各数据处理步骤的信息
        '''
        return summary

    # 直接以实例化对象的名称作为代码时输出的字符串，以下两种方法是相同效果的，都是把__repr__等同于__str__，都是可调用对象(方法)
    # __repr__ = __str__
    def __repr__(self):
        return self.__str__()


    # 重写__getattr__后会没有了实例化对象.__name__这个属性，有两个方法解决：1、在def __getattr__(self,item)的return返回，2、增加def __name__(self):
    # print(实例化对象),help(实例化对象)都要涉及实例化对象.__name__
    def __name__(self):
        return self.__name__()

    data_file_path = ""

    # 利用属性来返回读取DataFrame方法
    _get_data_method = {"read_csv":pandas.read_csv,
                       "read_excel":pandas.read_excel,
                       "read_json":pandas.read_json,
                       "read_pickle":pandas.read_pickle,
                       "read_html":pandas.read_html,
                       "read_sql":pandas.read_sql}
    def __getattr__(self, item): # 实例没有此属性item这个属性时才调用__getattr__方法，但此方法会使得实例化对象没有__name__
        return self._get_data_method[item]

    # 装饰器：读取原数据DataFrame和的文件路径的方法的装饰器
    def io_add_raw_dataframe(func):
        def inner_function(self,*param,**params):
            # 保存原数据的文件位置
            if isinstance(param,tuple) and param != ():
                if isinstance(param[0],str):
                    raw_data_file_path = param[0]
            elif isinstance(params,dict):
                file_path = params['io']
            self.raw_data_file_path = raw_data_file_path

            # 保存原数据的dataframe
            key = func.__name__.replace('_raw','')
            pd_data = self._get_data_method[key](*param,**params)
            self.raw_dataframe = pd_data
        return inner_function

    @io_add_raw_dataframe
    def read_raw_csv(self):
        pass
    @io_add_raw_dataframe
    def read_raw_excel(self):
        pass
    @io_add_raw_dataframe
    def read_raw_json(self):
        pass
    @io_add_raw_dataframe
    def read_raw_pickle(self):
        pass
    @io_add_raw_dataframe
    def read_raw_html(self):
        pass
    @io_add_raw_dataframe
    def read_raw_sql(self):
        pass

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
        if not self.all_procedure:
            print('No procedure!')
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

        # 获取处理步骤的区间
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

if __name__ == '__main__':
    DataProcedure_instance1 = DataProcedure()
    # DataProcedure_instance1.read_raw_excel(r".\data\test.xlsx",header=0,index_col=0)
    # print(DataProcedure_instance1.raw_data_file_path)

    # dataframe = DataProcedure_instance1.raw_dataframe
    # print('\n','*'*50,dataframe,'*'*50,'\n')
    # print(check_null(dataframe))

    # print(DataProcedure_instance1.__name__)
    # print(DataProcedure_instance1.__dict__)
    # print(DataProcedure_instance1)
    # print(help(DataProcedure))
    # print(help(DataProcedure_instance1))
    # DataProcedure_instance1