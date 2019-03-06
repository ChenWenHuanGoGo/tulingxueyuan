import random
import string
# input输入的是字符类型，需要强制转换
'''
如果输入的数字比程序随机数大，分别输出个、十、百
如果刚好相等，输出：中奖啦
如果小于随机数，讲120个字符输入到文本文件中，每行12个字符，前4个为字母，后8个为数字
'''
a = input("请输入一个三位数：")
def save(num):
        # isdigit不能用于int类型的变量，因为每次循环后num为int类型，所以需要将num转换为str类型
        num = str(num)
        # 判断是否是纯数字
        if num.isdigit() and 100 <= int(num) <= 999:
             num_random = random.randint(100,999)
             num = int(num)
             if num > num_random:
                 # //表示除以一个数后取整数部分，%表示取余数
                 hundreds_place = num // 100
                 tens_place = num // 10 % 10
                 ones_place = num % 10
                 print("百：{0} 十：{1} 个：{2}".format(hundreds_place,tens_place,ones_place))
             elif num == num_random:
                 print("恭喜你中奖啦")
             else:
                 print("{0}<{1}".format(num,num_random))
                 file_f = word()
                 with open("练习.txt","a") as f:
                     f.write(file_f)
        else:
            print("请按规定输入")

def word():
    # 创建一个空字符
    w_line = ""
    for i in range(10):
        # 四个随机字母
        for m in range(4):
            # string.ascii_letters返回所有大小写字母
            w = random.choice(string.ascii_letters)
            w_line += w
        # 8个随机数字
        for n in range(8):
            w_num = random.randint(1,9)
            w_line += str(w_num)
        # 换行
        w_line += "\n"
    return w_line

if "__main__" == __name__:
    save(a)
