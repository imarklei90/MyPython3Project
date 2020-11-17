# coding: utf-8

import re

# 在起始位置匹配: (0,3)
print(re.match('www', 'www.baidu.com').span())

# <re.Match object; span=(0, 3), match='www'>
print(re.match('www', 'www.baidu.com'))

# 不在起始位置匹配 ： None
print(re.match('mmm', 'www.baidu.com'))