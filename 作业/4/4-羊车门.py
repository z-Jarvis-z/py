import random

# 初始化三扇门
doors = ['goat', 'goat', 'goat']

# 随机放置汽车
car_index = random.randint(0, 2)
doors[car_index] = 'car'

# 参赛者随机选择一扇门
player_choice = random.randint(0, 2)
print("你选择了门", player_choice + 1)

# 主持人开启一扇有山羊的门
# 主持人不能开启参赛者选择的门和有汽车的门
opened_door_indices = [i for i in range(3) if i != player_choice and i != car_index]
goat_index = random.choice(opened_door_indices)
print("主持人打开了门", goat_index + 1, "，里面是一只山羊")

# 参赛者是否更换选择
change_choice = input("你想要更换选择吗？（y/n）").lower().startswith('y')
if change_choice:
    player_choice = [i for i in range(3) if i != player_choice and i != goat_index][0]
    print("你更换了选择，现在选择的是门", player_choice + 1)

# 输出结果
if doors[player_choice] == 'car':
    print("恭喜你猜中了汽车！")
else:
    print("很遗憾，你猜错了，汽车在门", car_index + 1, "后面")
