import random

# random.random()获取0-1之间的随机小数，[0,1)
for i in range(10):
    print(random.random())

# random.randint(x,y),返回[x,y]之间的随机整数
print(random.randint(1,10))

# random.randrange(start, stop[, step=1]),取[x,y),步进默认为1，可修改，整数
print(random.randrange(1,10,step=5))

# random.choice() 随机获取序列中的值,一定是一个序列
print(random.choice((0,5,6,8)))

# random.shuffle()随机打乱序列,返回None
list1 = [1,2,3,4,5]
print(random.shuffle(list1))
print(list1)

# random.uniform()随机获取指定范围内的值，包括小数
for i in range(5):
    print(random.uniform(1,2))