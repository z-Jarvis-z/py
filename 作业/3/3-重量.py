weight = eval(input('请输入你的体重(kg)：'))
for i in range(10):
    weight_earth = weight + 0.5 * (i + 1)
    weight_moon = weight_earth * 0.165
    print('未来第 {} 年地球体重为 {:.2f} kg,月球体重为 {:.2f} kg'.format(i + 1, weight_earth, weight_moon))
