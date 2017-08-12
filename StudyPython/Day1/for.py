# Author: Junting

# age_of_oldMan = 56
# guess_num = 0
#
# for i in range(3):
#     guess_age = int(input("Guess age: "))
#     if age_of_oldMan == guess_age:
#         print("Yes, you got it!")
#         break
#     elif age_of_oldMan < guess_age:
#         print("Think bigger")
#     else:
#         print("Think smaller")
#     guess_num += 1
# else:
#     print('Yout have tried too many times...fuck off')


# 隔一个数输出（区分奇偶变的更简单了）
# for i in range(0, 10, 2):
#     print("loop: ", i)

# 对数字竞猜，进行进一步的改造，错误3次后，询问玩家是否继续竞猜，只要输入了'N'，就是结束游戏，不然就继续游戏

# result_number = 88
# count = 0
#
# while count < 3:
#     guess_num = int(input("guess number: "))
#     if result_number == guess_num:
#         print("Yes, you got it!")
#         break
#     elif result_number > guess_num:
#         print("Think smaller")
#     else:
#         print("Think bigger")
#     count += 1
#     if count == 3:
#         continue_confirm = input("Do you want to guessing?")
#         if continue_confirm != 'n':
#             count = 0

# continue 特性

# for i in range(10):
#     if i < 3:
#         print("loop: ", i)
#     else:
#         continue
#     print("hehe...")


for i in range(10):
    print("------------- {i} ------------".format(i=i))
    for j in range(10):
        print(j)
        if j > 5:
            break
