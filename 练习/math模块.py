import math

# 光标放到模块后，按f4，查看math模块的源码
# ctrl+/  把一行变为注释
# 文件命名时，不要与模块名相同，否者会出错

# math.ceil()向上取整数
print(math.ceil(5.1))

# math.floor（）向下取整操作
print(math.floor(5.1))

# 查看系统保留关键字，不可以当做变量名的命名
import keyword
print(keyword.kwlist)

# round()四色五入操作，系统里的函数，不是math中的round()
print(round(5.3))

# math.sqrt() 开平方，返回浮点数
print(math.sqrt(4.4))

# math.pow() 与幂运算差不多，计算一个数的几次方
# 返回浮点数，pow(x,y),表示x的y次方
print(math.pow(2,4))

#幂运算,返回整形
print(2**4)

# math.fabs() 取绝对值，返回浮点数
print(math.fabs(-10))

# abs() 取绝对值，不是math模块中的，而是python内置函数，返回值由本身的类型而定
print(abs(-10))

# math.fsum(序列),求和，math模块中的，对一个序列求和，返回浮点数
print(math.fsum((1,4,5,3,2,4)))

# sum(序列) python 内置函数求和，对序列求和，返回类型由本身决定
print(sum([2,3,5,3]))

# math.modf()  将一个浮点数拆分为整数部分和小数部分,返回一个元祖，小数在前，整数在后
print(math.modf(4.5))

# math.copysign(),将第二个数的符号（正负号）传给第一个数,返回第一个数的浮点数
print(math.copysign(2,-1))
help(math.modf)

# 打印自然对数
print(math.e)

# 打印π
print(math.pi)
