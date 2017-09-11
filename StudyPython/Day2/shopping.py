# shopping.py

# 1、定义商品列表、购物车、用户
# 2、程序执行，用户输入可用余额
# 3、显示商品列表，等待用户输入商品编号
# 4、获取商品的价格与用户余额进行对比，大，输出"您的余额不足，请充值。"；小，继续打印商品列表，等待用户输入
# 5、除了输入商品id，还可以输入 end，结束购物
# 6、打印用户购买的东西

shopList = [
    ["iphone8", 8888],
    ["iphone7", 6888],
    ["iphone6s", 5888],
    ["iphone6", 4888],
]

car = []

user = int(input("请用户输入可用余额："))

while True:
    print("商品列表：");
    for i in range(len(shopList)):
        str = '''
            {_i}、 {_name} {_price} 
        '''.format(_i=i, _name=shopList[i][0], _price=shopList[i][1])
        print(str)

    selected = int(input("Your have smoeting?"))

    if user > shopList[selected][1] or user == shopList[selected][1]:
        car.append(shopList[selected])
        user = user - shopList[i][1]
        continue
    else:
        end = input('余额不足,你是结束购物（yes／no）：')
        if end == 'yes':
            print("购物清单：", car)
            break

