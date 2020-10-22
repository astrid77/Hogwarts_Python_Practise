def fight():
    # 初始化变量
    my_hp, my_power = 1000, 200
    enemy_hp, enemy_power = 1000, 200

    # 加入循环
    while True:
        # 战斗消耗血量计算
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        # print(my_hp, enemy_hp)
        # 判断输赢
        if my_hp <= 0 or enemy_hp <= 0:
            result = "恭喜你赢了！" if my_hp > enemy_hp else "game over~"
            print(result)
            break


if __name__ == '__main__':
    fight()
