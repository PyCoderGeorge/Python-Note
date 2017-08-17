# Author: Junting

# 输入密码，不以明文显示

# import getpass
#
# _username = "Twitch"
# _password= "abc123"
#
# username = input("username: ")
# password = getpass.getpass("password: ")
#
# if _username == username and _password == password:
#     print("Welcome user {username}".format(username=username))
# else:
#     print("Invalid username or password")

old_boy_age = 50;
guess_age = int(input("guess age: "))

if old_boy_age == guess_age:
    print("your guess it")
elif old_boy_age > guess_age:
    print("think limiter")
else:
    print("thinks lagger")