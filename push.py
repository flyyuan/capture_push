#coding=utf-8
import os
import time,datetime
from time import strftime,gmtime

def __push__():
	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	newtime = strftime("%H-%M", gmtime())
	newtime = str("time"+newtime)
	os.system("ffmpeg -re -i "+today+newtime+".avi -f flv rtmp://119.29.92.121:1395/mylive/rtmpstream ")
	print("push()exec")

__push__()
