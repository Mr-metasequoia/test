# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:47:58 2021

@author: metasequoia
"""

import os
import time

#这些是用来禁用控制台的关闭按钮的，必要时可以在控制台里结束进程
import win32console, win32gui, win32con
hwnd = win32console.GetConsoleWindow()
if hwnd:
   hMenu = win32gui.GetSystemMenu(hwnd, 0)
   if hMenu:
       win32gui.DeleteMenu(hMenu, win32con.SC_CLOSE, win32con.MF_BYCOMMAND)

#判定阶段。晚24点-早6点(共7小时)应处于睡眠阶段，6-12点为上午，12-18点为下午，18-23点为晚上。次日重置daytime文件。
def todate(day,daytime):
    
    #判断是否过了一日，若为次日则重置daytime文件（当日已用时间）和day文件   
    fo = open(day,"r")
    theday = fo.readline();
    fo.close()
    trueday = time.strftime("%D",time.localtime())
    if theday==trueday:
        pass
    else:
        fo1 = open(daytime,"w")
        fo1.write("0")
        fo1.close()
        fo3 = open(day,"w")
        fo3.write(trueday)
        fo3.close()
    
    #显示累积已用多长时间，ds是累积使用秒数
    fo2 = open(daytime,"r")
    ds = int(fo2.readline())
    fo2.close()
    dh = int(ds/3600)
    dm = int((ds%3600)/60)
    print("\n  今日累积使用计算机约"+str(dh)+"小时"+str(dm)+"分钟")
    
    #判断是否处于可用区间
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
    
    #若没有return -1，则处于可用区间，定时[4分钟]关机供做出决策，纯免费。
    os.system("shutdown -s -t 240")
        
    
#显示与修改任务。使用绝对路径文本文件来保存和读取一个短暂任务，一般来说时限为当日或当次开机。
#local：文本文件的绝对地址，用于短暂记录任务(目标)
def task(localtask):
    print("\n----预定目标----\n")
    fo = open(localtask,"r")
    for line in fo.readlines():
        print("  "+line,end="")
    fo.close()
    print("\n----------------")

    j = input("\n是否更新（Y/N）：")
    while j!="Y" and j!="y" and j!="yes" and j!="N" and j!="n" and j!="no":
    	j = input("\n是否更新（Y/N）：")
    	pass

    if j=="Y" or j=="y":
        fo = open(localtask,"w")
        print("\n----新目标----\n")
        n = input("(-1结束)：")
        while n!="-1":
            fo.write(n+"\n")
            n = input("(-1结束)：")
            pass
        fo.close()

#设置定时关机。输入秒数自定义本次开机的使用时间，并即刻开始计时。
#remind：一条提示文本，通常用于提供定时关机的参考时间
def shut(remind,daytime):
    print("\n----定时关机----\n")
    print(remind)
    
    t = ""
    #判断t是否为数字，如果不是数字(且不是“-1”)则循环要求重新输入
    while t.isdigit() == False and t!="-1":
        t = input("\n请输入定时关机の时间:")
    
    t = int(t)
    #如果输入-1，则每次请求给10分钟额外时间
    if t==-1:
        while 1:
            j = input("\n再给我10分钟(Y/N)：")
            if j=="y" or j=="Y":
                
                #读出已用时间dt，新增10分钟
                foread = open(daytime,"r")
                dt = int(foread.readline())
                dt = dt + 600
                foread.close()
                #把增长10分钟的dt写入daytime文件
                fow = open(daytime,"w")
                fow.write(str(dt))
                fow.close()
                
                os.system("shutdown -a")
                os.system("shutdown -s -t 600")
                
                print("----技能冷却中----")
                time.sleep(480)
    
    
    #读出已用时间dt，加上本次用时t
    foread = open(daytime,"r")
    dt = int(foread.readline())
    dt = dt+t
    foread.close()
    #把增长的dt写入daytime文件
    fow = open(daytime,"w")
    fow.write(str(dt))
    fow.close()
    
    os.system("shutdown -a")
    os.system("shutdown -s -t "+str(t))
    
    i=int(0)
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

day = "C:\\Users\\metasequoia\\Desktop\\制度\\shutdown\\day.txt"
daytime = "C:\\Users\\metasequoia\\Desktop\\制度\\shutdown\\daytime.txt"
localtask = "C:\\Users\\metasequoia\\Desktop\\制度\\shutdown\\task.txt"
remind = "参考时间    临时使用-1    早餐/看番1620    学习/午休3000"

#当todate()返回-1时，代表现在应处于睡眠时间，即不能显示与修改任务，也不能重置定时关机时间
if todate(day,daytime)!=-1:
    task(localtask)
    shut(remind,daytime)












