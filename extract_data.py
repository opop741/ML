'''
# 读取文本，实例化时限定可使用内存数量和每次的读取行数
# import InputData.InputText as IIT 
# iit = IIT.InputText(path=r"Y:/python_project/ML/InputData/test.txt",free_memory_of_GB=2,lines_n=5)
# print(iit.return_all_dall())

from InputData import InputText as IIT
path = r"Y:/python_project/GitHub/ML/data/test.txt"
# iit = IIT.InputText(path=path,free_memory_of_GB=2,lines_n=5,newline_str='\r\n') #split_str指定换行符，不输入默认不处理换行符
iit = IIT.InputText(path=path,free_memory_of_GB=2,lines_n=5) #split_str指定换行符，不输入默认为None不处理换行符
import time
start_time = time.time()
import random

while True:
    cache = iit.return_next_N_line(random.randint(0,10))
    if cache:
        print(cache)
    else:
        break
print(time.time() - start_time)
'''

'''
# 存入DataFrame，返回dict，例的数据类型与有缺失的列，有缺失的行的index，有缺失的列的名称，有缺失的单元格坐标。
import pandas as pd
from InputData import check_data
path = r"Y:/python_project/GitHub/ML/data/test.xlsx"
pd_data = pd.read_excel(path,header=0,index_col=0)
result = check_data.check_NaN(pd_data)
for i in result.keys():
	print(i,'\n',result[i],'\n')
'''

'''
from InputData import DataProcess
import pandas as pd
path = r"Y:/python_project/GitHub/ML/data/test.xlsx"
pd_data = pd.read_excel(path,header=0,index_col=0)

dummy_variable_dict,pd_data = DataProcess.dummy_variable(pd_data, '数字分类')

print(dummy_variable_dict,'\n')
print(pd_data)
'''