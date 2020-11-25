# coding=utf-8
"""
reSplitFile.py
文件分割：
寻找指定路径下所有文本文件中的匹配行
把一个匹配行以下至下一匹配行之前的部分存为单独文件
新文件存在原文件相同的节点上，文件名
"""
import os, re

# 要处理的路径
DIR = "./tree"
# 要处理的文本文件后缀列表
EXT = ['.txt', ".md"]
# 切分标记行（下一文件的首行）正则表达式，请按需设置
# r = re.compile(r'^.{1,30}(卷第?[一二三四五六七八九十百千万零〇]+).{0,20}$')
r = re.compile(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)')
# 是否在正则匹配前删除行中空白字符
DELET_SPACE_BEFORE_MATCH = True

fileNum = 1
for root, __, files in os.walk(DIR):
    # 文件过滤（限定扩展名）
    lesson_cut_file_list = [x for x in files if os.path.splitext(x)[1] in EXT]
    for file in lesson_cut_file_list:
        n = 0
        outLines = []
        chapter = ""
        (fn, ex) = os.path.splitext(file)
        fn += "_" + str(n) + "_" + chapter + ex
        fileName = os.path.join(root, fn)
        # 注意文件编码为utf-8（无签名）
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip("\n")
                # 先删除（忽略）行中空白字符
                if DELET_SPACE_BEFORE_MATCH:
                    clean_line = re.sub(r"\s", "", line)
                    match_line = r.match(clean_line)
                else:
                    match_line = r.match(line)
                if match_line:
                    if outLines:
                        with open(fileName, "w", encoding="utf-8") as outFile:
                            outFile.write("\n".join(outLines))
                    outLines = [line]
                    chapter = match_line.group(1)
                    n += 1
                    (fn, ex) = os.path.splitext(file)
                    fn += "_" + str(n) + "_" + chapter + ex
                    fileName = os.path.join(root, fn)
                else:
                    outLines.append(line)
        if outLines:
            with open(fileName, "w") as outFile:
                outFile.write("\n".join(outLines))
        print(fileNum, "files done.")
        fileNum += 1