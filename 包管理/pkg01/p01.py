class Student():
    def __init__(self,name="NoName", age=18):
        self.age = age
        self.name = name
    def say(self):
        print("my name is {}".format(self.name))
def sayHello():
    print("欢迎来到图灵学院")
if __name__ == "__main__":
    print("我是模块01")