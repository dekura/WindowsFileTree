#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import csv
root = "/Users/dekura/Desktop/xunjie/test_tree"
file = "fuck.txt"

all_nums = []
all_names = []

with open(os.path.join(root, file), "r", encoding="utf-8") as f:
    all_lines = f.readlines()
    # print(all_lines)
    all_length = len(all_lines)
    # print(all_length)
    for index, line in enumerate(all_lines):
        # print(index)
        # if index <= 1:
        #     continue
        line = line.strip("\n")
        num = line[:4]
        num = [num]
        all_nums.append(num[0])
        # print(index)
        if index+2 < all_length:
            pre = num[0] + ' ├─'
        else:
            pre = num[0] + ' └─'
            # print(pre)
            # print(line.replace(pre, ''))
        # print(pre)
        name = line.replace(pre, '')
        all_names.append(name)


# print(all_nums)
lnums = len(all_nums)
# print(all_names)
real_nums = []

for index, num in enumerate(all_nums):
    if index + 1 >= lnums:
        break

    real_num = int(all_nums[index+1]) - int(all_nums[index]) - 2
    real_nums.append(real_num)

print(real_nums)
print(all_names)

# for index, real_num in enumerate(real_nums):
#     print(str(index+1)+'. '+all_names[index]+' : '+str(real_num))
