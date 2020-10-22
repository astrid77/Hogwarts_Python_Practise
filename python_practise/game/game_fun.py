import random


def fight(enemy_hp, enemy_power):
    # 初始化变量
    my_hp, my_power = 1000, 200

    print("敌人血量为{}，攻击值为{}".format(enemy_hp, enemy_power))

    # 加入循环
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        if my_hp <= 0 or enemy_hp <= 0:
            # 判断输赢
            result = "恭喜你赢了！" if my_hp > enemy_hp else "game over~"
            print("{}\n你的剩余血量为{}，敌人剩余血量为{}".format(result, my_hp, enemy_hp))
            break


if __name__ == '__main__':
    # 列表推导式生成hp和power
    hp = [x for x in range(990, 1010)]
    enemy_power = [x for x in range(190, 210)]

    # 随机赋予敌人血量和攻击值
    enemy_hp, enemy_power = random.choice(hp), random.choice(enemy_power)

    # 调用战斗方法
    fight(enemy_hp, enemy_power)
