
class Animal:

    def __init__(self):
        print("动物")

    def eat(self):
        print("能吃")

    def sleep(self):
        print("能睡")


class Panda(Animal):

    def __init__(self, name):
        print(f"我是{name}")

    def eat(self):
        super()
        print("我喜欢吃竹子")



if __name__ == '__main__':
    an = Animal()
    an.eat()
    an.sleep()

    pd = Panda("大熊猫")
    pd.eat()
    pd.sleep()