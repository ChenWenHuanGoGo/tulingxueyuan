import math
import random

# input输入的是字符类型，需要强制转换
a = input("请输入一个三位数：")

def haha(num):
    # 判断是否是纯数字
    if num.isdigit() and 100 <= int(num) <= 999:
         num_random = random.randint(100,999)
         num = int(num)
         if num > num_random:
             print("{0}比{1}大".format(num,num_random))
         else:
             print("{0}比{1}小".format(num, num_random))
    else:
        print("请按规定输入")


for i in range(5):
    haha(a)
