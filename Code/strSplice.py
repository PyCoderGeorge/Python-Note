## 字符串拼接
# str1 = input("请输入一个人的名字：")
# str2 = input("请输入一个国家名字：")
# print("世界这么大，{}想去{}看看。".format(str1, str2))

## 整数序列求和。用户输入一个正整数N，计算从1和N想家之后的结果
# n = input("请输入正整数N：")
# sum = 0
# for i in range(int (n)):
#    sum += i + 1
#print("1到N求和结果：", sum)

## 九九乘法表输出，工整打印输出常用九九乘法，格式不变
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={:2} ".format(j, i, i * j), end='')
#     print('')    

## 阶乘计算。计算 1+2!+3!+...+10!的结果
# sum, tmp = 0, 1
# for i in range(1, 11):
#    tmp *= i
#    sum += tmp
# print("运算结果是:{}".format(sum))

## 猴子吃桃问题
# n = 1
# for i in range(5, 0, -1):
#    n = (n+1) << 1
# print(n)    

## 健康食谱搭配
# diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
# for x in range(0, 5):
#    for y in range(0, 5):
#        if not(x == y):
#            print('{} {}'.format(diet[x], diet[y]))

## 画个五角星
# from turtle import *
# fillcolor("red")
# begin_fill()
# while True:
#    forward(300)
#    right(144)
#    if abs(pos()) < 1:
#        break
# end_fill()

