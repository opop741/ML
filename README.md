﻿# ML
##项目目标：1、简化数据处理流程(数据导入，数据清洗，使接口更方便)，2、自己用python将经典的机器学习经典算法实现一遍，在这个过程中将算法原理和编程的基础打稳。

设想：1、将模型前的数据处理做成管道，2、将数据处理的常用工具打包，如t检验等，3、对原始数据进行体检报告，根据体检报告可以明确数据处理的方向

现阶段进度：数据处理的管道：
DataManager.py中的DataProcedure是模拟SPSS Modeler和sklearn的Pipeline的处理管道，试图将每一步处理都串联起来，输入的起点只接受pandas.DataFrame的数据表，通过自定义函数与规定的接口格式，使得每一个处理过程都记录下来，整个处理过程被装在一个处理步骤类的实例化对象中。