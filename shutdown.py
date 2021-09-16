# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:47:58 2021

@author: metasequoia
"""

import os
import time

#判定阶段。晚24点-早6点(共7小时)应处于睡眠阶段，6-12点为上午，12-18点为下午，18-23点为晚上。
def todate():
    hour = int(time.strftime("%H",time.localtime()))
    minute = int(time.strftime("%M",time.localtime()))
    if hour<6:
        print("\n  warning：现在应处于睡眠时间！")
        os.system("shutdown -s -t 600")
        input()
        return -1
    elif hour<12:
        if minute==0:
            print("\n  现在距离午饭还有"+str(12-hour)+"小时整")
        else:
            print("\n  现在距离午饭还有"+str(11-hour)+"小时"+str(60-minute)+"分钟")
    elif hour<18:
        if minute==0:
            print("\n  现在距离晚饭还有"+str(18-hour)+"小时整")
        else:
            print("\n  现在距离晚饭还有"+str(17-hour)+"小时"+str(60-minute)+"分钟")
    elif hour<23:
        if minute==0:
            print("\n  现在距离入睡还有"+str(23-hour)+"小时整")
        else:
            print("\n  现在距离入睡还有"+str(22-hour)+"小时"+str(60-minute)+"分钟")
    else:
        print("\n  warning：现在应处于睡眠时间！")
        os.system("shutdown -s -t 600")
        input()
        return -1
        
#显示与修改任务。使用绝对路径文本文件来保存和读取一个短暂任务，一般来说时限为当日或当次开机。
#local：文本文件的绝对地址，用于短暂记录任务(目标)
def task(local):
    print("\n----预定目标----\n")
    fo = open(local,"r")
    for line in fo.readlines():
        print("  "+line,end="")
        fo.close()
    print("\n----------------")

    j = input("\n是否更新（Y/N）：")
    while j!="Y" and j!="y" and j!="yes" and j!="N" and j!="n" and j!="no":
    	j = input("\n是否更新（Y/N）：")
    	pass

    if j=="Y" or j=="y":
        fo = open(local,"w")
        print("\n----新目标----\n")
        n = input("(-1结尾)：")
        while n!="-1":
            fo.write(n+"\n")
            n = input("(-1结尾)：")
            pass
    fo.close()

#设置定时关机。输入秒数自定义本次开机的使用时间，并即刻开始计时。
#remind：一条提示文本，通常用于提供定时关机的参考时间
def shut(remind):
    print("\n----定时关机----\n")
    print(remind)
    t = int(input("\n请输入定时关机の时间:"))
    os.system("shutdown -s -t "+str(t))
    i=0
    while(i<t):
        i = i+1
        time.sleep(1)
        if(i%60==0):
            print(str(int(i/60))+"分钟过去了")
        elif(i%15==0):
            print("----"+str(i)+"----")
        else:
            print("    "+str(i)+"    ")
        pass

#当todate()返回-1时，代表现在应处于睡眠时间，因此无需显示与修改任务，也不能设置定时关机
if todate()!=-1:
    task("C:\\Users\\metasequoia\\Desktop\\目标.txt")
    shut("参考时间    早餐/看番1620    学习/午休3000")












