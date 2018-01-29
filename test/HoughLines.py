# -*- coding:utf-8 -*-  
'''
Created on 2018年1月9日

@author: Administrator
'''
import cv2
import numpy as np  
import math
import operator

#两个回调函数
def HoughLinesP(minLineLength):
    global minLINELENGTH 
    kh = []#横线
    ks = []#竖线

    minLINELENGTH = minLineLength + 1
    print "minLINELENGTH:",minLineLength + 1
    tempIamge = scr.copy()
    picH = tempIamge.shape[1]
    picS = tempIamge.shape[1]
    lines = cv2.HoughLinesP( edges, 1, np.pi/180,minLINELENGTH, 50)
    for item in lines:
        for x1,y1,x2,y2 in item:
            #这里的点坐标为线的起始点和终点
            L = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
            if L<=1000:
                continue
            #如果线段长度小于10个像素点 舍去
            k = (x1-x2)*(x1-x2)
            #计算斜率
#             print k
            tmp =[x1,y1,x2,y2]
            if k<0.1:
                ks.append(tmp)  
            else:  
                kh.append(tmp)
    #合并横线
    for i in range(len(ks)):
        for j in range(i+1,len(ks)):
                L = (ks[j][0]-ks[i][0])*(ks[j][0]-ks[i][0])
                if (L < 100):
                    ll = ks[i][1],ks[j][1],ks[i][3],ks[j][3]
                    _min = min(ll)
                    _max = max(ll)
                    tmp = [ks[i][0],_min,ks[i][0],_max]
                    ks[i]=[0,0,0,0]
                    ks[j]=tmp  
    #合并竖线
    for i in range(len(kh)):
        for j in range(i+1,len(kh)):
                L = (kh[j][1]-kh[i][1])*(kh[j][1]-kh[i][1])
                if (L < 100):
                    ll = kh[i][0],kh[j][0],kh[i][2],kh[j][2]
                    _min = min(ll)
                    _max = max(ll)
                    tmp = [_min,kh[i][1],_max,kh[i][3]]
                    kh[i]=[0,0,0,0]
                    kh[j]=tmp  
#     sorted(kh,key = operator.itemgetter(0),reverse=True)
    kh.sort(cmp=None, key=operator.itemgetter(1))
#     print kh
    #删除过短的线段
    for x1,y1,x2,y2 in ks:
        L = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
        if L<=(picS/2)*(picS/2)*0.2:
            continue

        cv2.circle(tempIamge,(x1,y1),5,(255,0,0),5)
        cv2.circle(tempIamge,(x2,y2),5,(255,0,0),5)
        cv2.line(tempIamge,(x1,y1),(x2,y2),(255,0,0),5)
    for x1,y1,x2,y2 in kh:
        L = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
        if L<=(picH/2)*(picH/2)*0.1:
            continue
        if x1<picH/4:
            x1=0
        if x2>picH/4*3:
            x2=picH
        if math.fabs(x1-picH/2)<picH/4:
            x1 = picH/2
        if math.fabs(x2-picH/2)<picH/4:
            x2 = picH/2
        cv2.circle(tempIamge,(x1,y1),5,(55,255,155),5)
        cv2.circle(tempIamge,(x2,y2),5,(55,255,155),5)
        cv2.line(tempIamge,(x1,y1),(x2,y2),(0,255,0),5)
        print x1,y1,x2,y2
#         cv2.imshow("zxc",scr[0:y2,0:x2])
#     for i in range(len(kh)):
#         if kh[i+1][0]!=0:
#             midP = [kh[i][2],picH/2]
#             cv2.imshow("zxc",scr[0:y2,0:x2])
#         else:
#             cv2.imshow("zxc",scr[0:y2,0:x2])
    cv2.imshow(window_name,tempIamge)
    

#临时变量
minLineLength = 20

#全局变量
minLINELENGTH = 20
max_value = 30
window_name = "HoughLines"
trackbar_value = "minLineLength"

#读入图片，模式为灰度图，创建窗口
scr = cv2.imread("1.png",cv2.IMREAD_COLOR)
# cv2.imshow("aa",scr)
# gray = cv2.cvtColor(scr,cv2.COLOR_BGR2GRAY)
# scr=cv2.resize(scr,(32,32),interpolation=cv2.INTER_CUBIC)
# img = cv2.GaussianBlur(scr,(3,3),0)
# img = cv2.equalizeHist(scr)
edges = cv2.Canny(scr, 10, 50, apertureSize = 3)
cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)

#创建滑动条
cv2.createTrackbar( trackbar_value, window_name, \
                    minLineLength, max_value, HoughLinesP)

#初始化
HoughLinesP(20)

if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()