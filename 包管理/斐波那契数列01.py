a,b = 0,1
c = 0
while True:

    c = a + b
    if c >1000:
        break
    print(c, end=",")
    a = b
    b = c
def nano():
    pass