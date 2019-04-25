# ML
###自己用python将经典的机器学习算法实现一遍，顺便会把一些常用的数据导入，数据清洗再封装，让接口使用起来更方便。

DataManager.py中的DataProcedure是模拟SPSS Modeler的处理管道，试图将每一步处理都串联起来，输入的起点只接受pandas.DataFrame的数据表，经过的每一个处理函数都会记录，整个处理过程被装在一个处理步骤类的实例化对象中。
