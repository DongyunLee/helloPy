# coding=utf-8
# 运算符

# 算数运算符
"""
a = 9 % 2
b = 9 // 2
c = 3 ** 3
d = 1 / 2
e = 1 / float(2)
print a
print b
print c
print d
print e
"""

# 比较（关系）运算符

# 赋值运算符
"""
a = 9
# a //= 2
a **= 2
print a
"""

# 逻辑运算符
# and or not

# 位运算符(二进制，按位)
"""
a = 0100100011001
b = 0101100010100
c = a & b           # 按位与
d = a | b           # 按位或
e = a ^ b           # 按位异或
f = ~ e             # 按位取反
g = a << 2          # 左移动
h = a >> 2          # 右移动
print a
print b
print c
print d
print e
print f
print g
print h
"""

# 成员运算符(在指定的序列中找到值)
# in    not in

# 身份运算符(用于比较两个对象的存储单元)
# is    is not
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
"""
a = 10
b = 20
c = 10
x = a is b
y = a is not b
z = a is c
print x
print y
print z
"""

# 运算符优先级
# ** 指数 （最高优先级）=> 正负 => 乘除 => 加减 => 左右移动 => 位 => 比较 => 赋值 => 身份 => 成员 => 逻辑
a = 20
b = 10
c = 15
d = 5
e = 0

x = (a + b) * c / d  # ( 30 * 15 ) / 5
print "(a + b) * c / d 运算结果为：", x

y = ((a + b) * c) / d  # (30 * 15 ) / 5
print "((a + b) * c) / d 运算结果为：", y

z = (a + b) * (c / d)  # (30) * (15/5)
print "(a + b) * (c / d) 运算结果为：", z

xyz = a + (b * c) / d  # 20 + (150/5)
print "a + (b * c) / d 运算结果为：", xyz
