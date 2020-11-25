#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import csv
root = "/Users/dekura/Desktop/xunjie/test_tree"
file = "tree.txt"

all_nums = []
all_names = []

# with open(os.path.join(root, file), "a+", encoding="utf-8") as f:
#     f.write("      \n")
#     f.write("      --     ")

with open(os.path.join(root, file), "r", encoding="utf-8") as f:
    all_lines = f.readlines()
    all_length = len(all_lines)
    for index, line in enumerate(all_lines):
        line = line.strip("\n")
        if ('--' in line) and ('.zip' not in line):
            all_nums.append(index)
            name = line.replace('├─','').replace('└─', '')
            all_names.append(name)
    all_nums.append(all_length)
    all_names.append('file end')

lnums = len(all_nums)
real_nums = []

for index, num in enumerate(all_nums):
    if index + 1 >= lnums:
        break

    real_num = int(all_nums[index+1]) - int(all_nums[index]) - 4
    real_nums.append(real_num)

print(real_nums)
print(all_names)

# for index, real_num in enumerate(real_nums):
    # print(str(index+1)+'. '+all_names[index]+' : '+str(real_num))
