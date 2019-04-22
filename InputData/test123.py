# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

# file = open(r'D:\py_projects\ML\InputData\test1.txt','rb')

# for i in range(20):
#     try:
#         print([next(file) for i in range(2)])
#     except StopIteration:
#         print("已经结束")
#         file.close()
#         break


import sys
print(sys.path)

f = open("Y:\\python_project\\ML\\InputData\\test.txt","rb")

# for i in range(16):
# 	print(i)
# 	print(next(f).decode("gbk"))

chart_ = "utf-8"

print(next(f).decode(chart_))
print(next(f).decode(chart_))
for i in f:
	print(i.decode(chart_))
f.close()