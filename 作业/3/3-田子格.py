for i in range(11):
    if i == 0 or i == 10:
        print("+" + "+".center(9, "-") + "+")
    elif i % 5 == 0:
        print("+" + "+".center(9, "-") + "+")
    else:
        print("|" + "|".center(9) + "|")

