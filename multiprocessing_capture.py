#conding=utf-8
import subprocess
import os
from multiprocessing import Process
import time,datetime
from time import strftime,gmtime


def __capturedesktop__():
	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	newtime = strftime("%H-%M", gmtime())
	newtime = str("time"+newtime)
	subprocess.Popen("ffmpeg -f dshow -i video=\"screen-capture-recorder\" "+today+newtime+".avi", shell=True)



def __push__():
	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	newtime = strftime("%H-%M", gmtime())
	newtime = str("time"+newtime)
	os.system("ffmpeg -re -i "+today+newtime+".avi -f flv rtmp://119.29.92.121:1395/mylive/rtmpstream ")
	print("push()exec")



if __name__=='__main__':
	capturedesktop = Process(target=__capturedesktop__)
	push = Process(target=__push__)
	capturedesktop.start()
	push.start()
	print('Child process end.')








