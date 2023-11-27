def rest_day_interval(n):
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
        if (consecutive_days - 1) % n == 0 and consecutive_days != 1:
            consecutive_days = 0

        # 如果连续学习天数大于等于4并小于等于7，每天能力增长为前一天的1%
        if 7 >= consecutive_days >= 4:
            ability *= 1.01
        # 如果连续学习天数小于等于3，能力值不变
        else:
            pass

    print("固定每{}天休息1次，365天后的能力值为：{:.2f}".format(n, ability))


if __name__ == '__main__':
    rest_day_interval(10)
    rest_day_interval(15)
