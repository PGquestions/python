# -*- coding: utf-8 -*- 
# @Time : 2021年1月10日23:10:35
# @Author : wenhao
# @File : jiujiu.py
#九九乘法表

#version1.0 2021年1月10日23:10:55
for i in range(1,10):
    for j in range(1,i+1):
        result = i * j
        print(f'{i}*{j}={result}',end='\t')
    print()