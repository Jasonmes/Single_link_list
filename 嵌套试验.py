#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
import random
off = []
Offices = []


office = int(input("多少个教室:"))

'''第一种生成嵌套列表'''
# 这样会造成深拷贝，不适合这次使用
# Offices *= office
'''第二种生成嵌套列表'''
# 一样是深拷贝，不适合这里使用,off的地址不变，拷贝了好几份存入到office，所以最后每个教室的老师都是相同的
# for i in range(office):
#     Offices.append(off)
#     i += 1

teacher_num = int(input("老师数量:"))

for j in range(teacher_num):
    off.append(input("老师的名字:"))
    Offices.append(off)

print(Offices)