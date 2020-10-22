"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""


def fight():
    # 初始化变量
    my_hp, my_power = 1000, 200
    enemy_hp, enemy_power = 1000, 200

    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢第一种方式
    # if my_final_hp > enemy_final_hp:
    #     print("恭喜你赢了！")
    # elif my_final_hp < enemy_final_hp:
    #     print("game over~")
    # else:
    #     print("平局")

    # 判断输赢第二种方式
    result = "恭喜你赢了！" if my_final_hp > enemy_final_hp else "game over~"
    print(result)


if __name__ == '__main__':
    fight()
