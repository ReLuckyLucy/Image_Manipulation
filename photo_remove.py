#!/usr/bin/python3
import os

b = 0#定义一个数文件数量的变量
for root, dirs, files in os.walk('/code'):#D:\\masked\\Annotations可以改成自己想要的路径
    for name in files:#for循环删除文件
        if name.endswith(".jpg"):#.jpg可以换成另一种你想删除的文件后缀名
            b += 1
            os.remove(os.path.join(root, name))#删除后缀为.jpg的文件
            print("Delete File: " + os.path.join(root, name))#告诉你你删除的每个文件文件名都是什么
print(b)#告诉你总共删除了多少个文件

