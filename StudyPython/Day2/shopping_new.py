# 购物车

product_list = [
    ('iphone', 8888),
    ('macbook air', 9880),
    ('macbook pro 2016', 22800),
    ('macbook pro 2017', 23800),
    ('iwatch', 3800),
]
shopping_list = []

salary = input("Input your salary:")
# <str>.isdigit() 判断是不是数字，字符串形式的数字，也是返回真
if salary.isdigit():
    salary = int(salary)
    while True:
        # enumerate() 依依列举出每一项，携带着索引
        for index,item in enumerate(product_list):
            # print(product_list.index(item),item)
            print(index,item)
        user_choice= input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shpping cart,your current balance is \033[31;1m%s\033[0m" %(p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线啊\033[0m" %(salary))
            else:
                print("商品不存在，请重新输入 product code [%s] is not exist!" %(user_choice))
        elif user_choice == "q":
            print('--------shopping list----------')
            for index,p in enumerate(shopping_list):
                print(index, p)
            print("Yout cureent balance: %s" %(salary))
            break
        else:
            print("invalid option")

