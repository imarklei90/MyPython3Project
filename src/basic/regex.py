# coding: utf-8

import regex

# 在起始位置匹配: (0,3)
print(regex.match('www', 'www.baidu.com').span())

# <re.Match object; span=(0, 3), match='www'>
print(regex.match('www', 'www.baidu.com'))

# 不在起始位置匹配 ： None
print(regex.match('mmm', 'www.baidu.com'))