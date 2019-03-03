

__all__ = ["p01"]
def init():
    print("i am in init package02")

    #定义了 __all__, 使用from pkg02 import * 时,只会调用模块p01
    #不会调用init()函数