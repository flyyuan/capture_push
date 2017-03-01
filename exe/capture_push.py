from tkinter import *
import tkinter.messagebox as messagebox
import subprocess
import time
import os

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		#pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
		self.pack()
		#在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.***()使程序退出。
		self.createWidgets()

	def createWidgets(self):
		#"开始直播"按钮
		self.beginButton = Button(self, text='直播开始',command=self.begin)
		self.beginButton.pack()
		#"直播结束"按钮
		self.endButton = Button(self,text='直播结束',command=self.end)
		self.endButton.pack()

	def begin(self):
		subprocess.Popen('D:\capture_push\capture_desktop.exe')
		time.sleep(5)
		subprocess.Popen('D:\capture_push\push.exe')

	def end(self):
		os.system('taskkill /F /im ffmpeg.exe')
		quit()


app = Application()
app.master.title('直播')
app.mainloop()