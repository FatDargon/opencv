# -*- coding:utf-8 -*-  
'''
Created on 2018年1月9日

@author: Administrator
'''
#!/usr/bin/env python  
# encoding: utf-8  
import cv2  
import numpy as np 

img = cv2.imread("1.png", 0)  
  
img2 = cv2.GaussianBlur(img,(3,3),0)  
edges = cv2.Canny(img2, 50, 150, apertureSize = 3)  

#(函数参数3和参数4) 通过步长为1的半径和步长为π/180的角来搜索所有可能的直线
#118 --是经过某一点曲线的数量的阈值
lines = cv2.HoughLines(edges,1,np.pi/180,280)  #这里对最后一个参数使用了经验型的值 
result = img2.copy()  
# print lines[1]
for item in lines:
    for line in item: 
        rho = line[0] #第一个元素是距离rho  
        theta= line[1] #第二个元素是角度theta  
        print rho  
        print theta  
        if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线  
                    #该直线与第一行的交点  
            pt1 = (int(rho/np.cos(theta)),0)  
            #该直线与最后一行的焦点  
            pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),result.shape[0])  
            #绘制一条白线  
            cv2.line( result, pt1, pt2, (0,255,0), 2)  
        else: #水平直线  
            # 该直线与第一列的交点  
            pt1 = (0,int(rho/np.sin(theta)))  
            #该直线与最后一列的交点  
            pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))  
            #绘制一条直线  
            cv2.line(result, pt1, pt2, (0,255,0), 2)  
# cv2.line(result, (0,0), (500,100), (0,0,255), 1)  
cv2.imshow('img', img )  
cv2.imshow('Result', result)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
