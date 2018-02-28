# -*- coding:utf-8 -*-  
'''
Created on 2018年1月30日

@author: Administrator
'''
import cv2
import numpy as np
import PIL.Image as image
def load_data(file_path):
    f = open(file_path,'rb') #二进制打开
    data = []
    img = image.open(f) #以列表形式返回图片像素值
    m,n = img.size #活的图片大小
    print (img.mode)# P
    img_RGB = img.convert("RGB")
    print (img_RGB.mode)
    print (img_RGB.size)
    return np.atleast_2d(img).astype('float')
img_data = load_data('10.gif')
    
#     for i in range(m):
#         for j in range(n):  #将每个像素点RGB颜色处理到0-1范围内并存放data
#             #print (img_RGB.getpixel((i,j)))
#             x,y,z = img_RGB.getpixel((i,j))
#             data.append([x/256.0,y/256.0,z/256.0])
#     f.close()
#     return np.mat(data),m,n #以矩阵型式返回data，图片大小
# img_data,row,col = load_data('10.gif')

img = cv2.imread('E:\\eclipse_python\\opencv\\test\\10.gif')
cv2.namedWindow("Image")
# cv2.imshow('Image', img)
cv2.imshow('Image', img_data)
cv2.waitKey(0) 