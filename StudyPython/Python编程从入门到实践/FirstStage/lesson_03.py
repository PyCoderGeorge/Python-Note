# 第三章 列表

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

## 原样返回内容
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-2:]) # 读取顺序是从左向右的

## 练习

names = ['廖伟凯', '衷敬强', '肖洋', '许洋', '陈俊安', '郭婷', '郭芸']

for i in range(len(names)):
    message = names[i] + ', 希望你永远快快乐乐的，前行的道路会有坎坷，并不会成为你停止前行的阻碍！'
    print(names[i])
    print(message)

## 列表操作方法练习

names= ['廖伟凯', '衷敬强', '肖洋']


noName = names.pop(1)
print(noName + ',无法参加该宴会')
names.insert(1, '陈俊安')
print(names)
names.append('衷敬强') # append() 只能单个添加
print(names)
names.append('许洋')
names.append('郭婷')
names.append('郭芸')
print(names)
print('#######################')
removeName = []
i = len(names)
while i > 1:
    str = names.pop()
    removeName.append(str)
    i = len(names) - 1
print(names)
print("移除：")
print(removeName)


## 排序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print(sorted(cars))  # 临时改变
print('临时改变')
print(sorted(cars, reverse=True)) # 临时改变

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

## 获取长度

num = len(cars)
print(num)


## 练习

friends = ['廖伟凯', '衷敬强', '肖洋', '许洋', '陈俊安', '郭婷', '郭芸']

print("原始数据：")
print(friends)
print("stored()临时改变排序")
print(sorted(friends))
print("验证数据")
print(friends)
print("反转列表")
friends.reverse()
print(friends)
print(len(friends))

print(friends[8])

