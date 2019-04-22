'''
# import InputData.InputText as IIT 
# iit = IIT.InputText(path=r"Y:/python_project/ML/InputData/test.txt",free_memory_of_GB=2,lines_n=5)
# print(iit.return_all_dall())

from InputData import InputText as IIT
iit = IIT.InputText(path=r"Y:/python_project/ML/InputData/test.txt",free_memory_of_GB=2,lines_n=10)

import random
while 1:
	cache = iit.return_next_N_line(random.randint(0,10))
	if not cache:
		break
	else:
		print(cache)
'''

print('return result is dict.')

import pandas as pd
from InputData import check_data
pd_data = pd.read_excel(r"D:\py_projects\ML\data\test.xlsx",header=0,index_col=0)
result = check_data.check_NaN(pd_data)
for i in result.keys():
	print(i,'\n',result[i],'\n')