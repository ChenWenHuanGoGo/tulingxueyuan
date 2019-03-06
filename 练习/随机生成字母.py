# 随机生成字母 方法1
import random
import string
# 大小写
a = string.ascii_letters
# 仅小写
b = string.ascii_lowercase
# 仅大写
c = string.ascii_uppercase
print(a)
print(b)
print(c)
print(random.choice(a))

print("*"*20)


#随机生成字母 方法2
# 小写字母的ascii码为97-122，大写字母的ASCII码为65-90
a = random.randint(97,122)
# chr 将ASCII码转变为字符
print(chr(a))

# ord 将字符转化为ascii码
print(ord("C"))