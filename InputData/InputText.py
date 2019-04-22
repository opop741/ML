# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

import os
import chardet

class InputText:
    def __init__(self,path,free_memory_of_GB=2,lines_n=5,newline_str=None):
        # 设置文件路径
        self.path = path

        # 设置可以用内存
        self.free_memory = int(free_memory_of_GB / 1.2) # 用于处理数据的空闲内存数量，单位GB

        # 每次读取的行数
        self.lines_n = lines_n

        # 分割符
        self.newline_str = newline_str

        # 检查可用内存量
        self.txt_size = os.path.getsize(self.path) # 读取文件大小，单位Bytes/比特/字节，比位大比KB小
        self.file_size_of_GB = self.txt_size / 1024 / 1024 / 1024

        # 检查编码，取1MB的文本内容来检查编码，不足1MB就全部检查
        with open(self.path,'rb') as f:
            if self.txt_size < 1024 * 1024:
                sample = f.read()
            else:
                sample = f.read(1024 * 1024)
            if chardet.detect(sample)['confidence'] > 0.9:
                self.chart = chardet.detect(sample)['encoding']

        # 临时属性用于存放读取文件流
        self.file_temp = 0

        # 停止读取属性
        self.stop = 'sStToOpP12343 2s4d3 aa352f1vb-_s315w.2g343bwgw98587^%^*&*^&(*(*^*jljv hisgsg12g1789456f6m65ffn5fn284n68f4f5t.././.,[];\'234)^%^&%2'

    #一次读取所有数据并返回
    def return_all_dall(self):
        # 文件大小 > 可用内存时抛出错误！
        if self.file_size_of_GB > self.free_memory:
            raise Exception("内存不足，不可返回所有数据，请使用其他方法！", RuntimeError)

        #一次读取所有数据并返回
        with open(self.path, 'rb') as f:
            content = f.read()
            content = content.decode(self.chart)
            return content

    #分开读取数据，每次返回n条数据
    def return_next_N_line(self,lines_n=None):
        #第一次调用时候初始化数据生成器
        if not self.file_temp:
            print("开始读取！")
            self.file_temp = open(self.path, 'rb')

        #实例化时候有一个行数设定，每次调用都可以更改输出行数
        if lines_n:
            self.lines_n = lines_n 

        #返回结果列表
        cache_list = []
        try:
            for i in range(self.lines_n):
                # 读取下一行文本
                cache = next(self.file_temp).decode(self.chart)

                # 去除换行符
                if self.newline_str:
                    str_len = len(cache) - len(self.newline_str)
                    cache = cache[:str_len]
                # 将本行添加都本次返回的list中
                cache_list.append(cache)
            return cache_list
        except Exception as e:
            self.file_temp.close()
            if cache_list != []:
                print('已读取至结尾！')
                return cache_list
            else:
                return

    #分开读取数据，每次返回1条数据
    def return_next_1_line(self):
        return self.return_next_N_line(1)