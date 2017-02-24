#coding=utf-8
import subprocess
import time,datetime
from time import strftime,gmtime


def __capturedesktop__():
	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	newtime = strftime("%H-%M", gmtime())
	newtime = str("time"+newtime)
	subprocess.Popen("ffmpeg -f gdigrab -i desktop "+today+newtime+".avi", shell=True)



__capturedesktop__()