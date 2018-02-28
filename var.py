# coding=utf-8
# 多变量赋值
# a, b, c = 1, 2, 'Hello,world'

# 标准数据类型

# Number数字
"""
num1 = 1
num2 = 2
num1 = 3
print num1, num2
del num2
print num1, num2
"""
# String字符串
"""
a = "Hello,world!"
b = "DoyleafPHP"
print b[3:7]
print a * 2
print a[0]  # 取单个字节
print a[3:]  # 取从3开始，未设置上限的字符串
print a + b  # 拼接

c = (a + b) * 2
print c
"""

# List列表（复合数据类型）索引数组
"""
a = [
    "aaa", [
        "ccc", 2
    ]
]
b = a + ['ddd']
c = b * 2
print a
print b
print c
c = c * 99
a[1] = c
print c[2:]
print b[1:9999]
print a[1]
"""

# Tuple元组(只读数组)
"""
a = ("aaa", 1, ["bbb"])
print a[2]
'''a[2] = "bbb"'''
"""

# Dictionary字典（关联数组）
"""
dictionary = {
    "key": "value"
}
"""

# 数据类型转换，直接将类型名作为函数（int/long/float/complex/str/repr/eval/tuple/list/set/dict/frozenset/chr/unichr/ord/hex/oct）