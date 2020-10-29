# -*- coding:utf-8 -*-
"""
作者：Apple
日期：2020年10月18日
"""
print('hello world')
# 将数据输出到文件中，需注意 1、所指定的盘存在 2、使用file=fp
fp = open('D:/text.txt', 'a+')  # 如果文件不存则创建，如果存在则在文件内容后追加
print('hello world', file=fp)
fp.close()

# 不进行换行输出
print('hello', 'world', '00')
