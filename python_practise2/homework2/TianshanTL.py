"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""
import random


class TongLao:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
        print(f"你的血量{hp},你的武力值{power}")

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print(name)

    def fight_zms(self, hp_en, power_en):
        print(f"敌人血量为{hp_en}，武力值为{power_en}")
        self.hp = self.hp / 2
        self.power = self.power * 10
        print(f"释放天山折梅手，我的血量缩减为{self.hp}，我的武力值提升至{self.power}")
        self.hp -= power_en
        hp_en -= self.power
        result = '你赢了' if self.hp > hp_en else "你输了"
        print(result)


if __name__ == '__main__':
    tl = TongLao(100, random.randint(20, 40))
    names = ["WYZ","李秋水","丁春秋"]
    tl.see_people(random.choice(names))
    tl.fight_zms(100, random.randint(20, 40))
