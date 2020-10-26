"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
from homework.TianshanTL import TongLao


class XuZhu(TongLao):
    """XuZhu类，继承于童姥"""

    def read(self):
        """念经方法"""
        print("罪过罪过")


if __name__ == '__main__':
    # 实例化XuZhu类
    xz = XuZhu(90,30)
    # 调用念经方法
    xz.read()
    # 调用父类方法
    xz.see_people("童姥")