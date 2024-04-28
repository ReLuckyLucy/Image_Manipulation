#!/usr/bin/python3
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import tensorflow as tf


save_path = "./img/minst" # 输出图片保存路径

(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()

def decode(images,labels,path):
    for index, vec in enumerate(images):
        image = vec.reshape([28,28])    #遍历图片
        label = labels[index]  #图片对应标签
        classes_path = os.path.join(path,str(label)) #图片分类到每个文件夹,得到文件夹地址
        if not os.path.exists(classes_path) : os.makedirs(classes_path) #不存在就创建
        image_path = os.path.join(classes_path, str(index)+".jpg") #图片地址
        matplotlib.image.imsave(image_path, image, cmap="binary")#保存图片

decode(x_train, y_train, os.path.join(save_path,"train"))
print("finish")
decode(x_test,y_test,os.path.join(save_path,"test"))
print("finish")

