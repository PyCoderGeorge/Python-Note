# Author: Junting

import sys, os

# sys.path 环境变量路径列表
# print(sys.path)

# sys.argv 获取执行脚本传递的参数，打印的是一个List列表，argv[0]一般是执行脚本的文件名
# print(sys.argv)

# os.system("dir") 用来运行shell命令，执行后结果不保存，返回的是命令的执行状态码 0 成功 非0失败
# cmd_res = os.system("dir")
# print('---->', cmd_res)

# os.popen("dir") 打开cmd命令的管道，执行的结果保存到一个临时内存里，返回的结果是指向内存的地址。想要提取执行结果需要使用到read()
cmd_res = os.popen("dir").read()

print('---->', cmd_res)

# 创建文件夹
os.mkdir("文件名")
