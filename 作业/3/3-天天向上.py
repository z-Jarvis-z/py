ability = 1  # 初始能力值为1
consecutive_days = 0  # 连续学习天数
current_day = 1  # 当前周期的天数

for i in range(365):
    consecutive_days += 1
    current_day += 1

    # 每7天为一个周期
    if current_day > 7:
        current_day = 1

    # 如果中断学习，重置连续学习天数
    if current_day == 1:
        consecutive_days = 0

    # 如果连续学习天数小于等于3，能力值不变
    if consecutive_days <= 3:
        ability = ability
    # 如果连续学习天数大于3，每天能力增长为前一天的1%
    else:
        ability *= 1.01

    # 每个周期的最后一天也需要计算
    if current_day == 7:
        consecutive_days = 0
        ability *= 1.01

print("365天后的能力值为：", round(ability, 2))
