#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from Tkconstants import *
from tkFileDialog import *
import os
import subprocess

class ToolApp(object):
    """docstring for ToolApp"""
    def __init__(self, arg):
        super(ToolApp, self).__init__()
        self.arg = arg
        frame = Frame(arg)
        frame.pack()
        # 源文件
        self.sourceFileLabel = Label(frame, text="源文件：")
        self.sourceFileLabel.pack()

        self.sourceFileName = StringVar()
        self.sourceFileEntry = Entry(frame,  textvariable=self.sourceFileName)
        self.sourceFileEntry.pack()

        self.selectSourceButton = Button(frame, text="选择源文件", command=self.selectSourceFile)
        self.selectSourceButton.pack(side=LEFT)
        # 目标文件
        self.desFileLabel = Label(frame, text="目标文件：")
        self.desFileLabel.pack()
        
        self.desFileName = StringVar()
        self.desFileEntry = Entry(frame, textvariable=self.desFileName)
        self.desFileEntry.pack()

        # 起始位置
        self.startPosLabel= Label(frame, text="开始位置：")
        self.startPosLabel.pack()
        
        self.startPosStr= StringVar()
        self.startPosEntry= Entry(frame, textvariable=self.startPosStr)
        self.startPosEntry.pack()

        self.endPosLabel= Label(frame, text="结束位置：")
        self.endPosLabel.pack()
        
        self.endPosStr= StringVar()
        self.endPosEntry= Entry(frame, textvariable=self.endPosStr)
        self.endPosEntry.pack()

        self.formateLabel= Label(frame, text="格式：")
        self.formateLabel.pack()
        
        self.formateStr= StringVar()
        self.formateEntry = Entry(frame, textvariable=self.formateStr)
        self.formateEntry.pack()




        self.button = Button(frame, text="Start~", command=self.start)
        self.button.pack(side=LEFT)
    def start(self):
        """docstring for start"""
        # print("begin to start", self.desFileName.get())
        # os.system("./ffmpeg/bin/ffmpeg.exe")
        exePath = "D:/GitHub/FFTools/ffmpeg/bin/ffmpeg.exe"
        exePath = exePath + " -i " + self.sourceFileName.get()
        exePath = exePath + " -c copy"
        exePath = exePath + " -ss " + self.startPosStr.get()
        exePath = exePath + " -to " + self.endPosStr.get()
        exePath = exePath + " -f " + self.formateStr.get()
        exePath = exePath + " " + self.desFileName.get()
        print(exePath)
        # self.subpro = subprocess.Popen(exePath, shell=True)
        # self.subpro.wait()

    def selectSourceFile(self):
        """docstring for selectSourceFile"""
        self.sourceFileName.set( askopenfilename())
        

def createUI():
    """docstring for createUI"""
    win = Tk()
    win.title("FFTools")
    win.geometry("600x300")
    # openfilename = askopenfilename()
    app = ToolApp(win)
    # print(openfilename)
    win.mainloop()
    

def main():
    """docstring for main"""
    createUI()
    print("main done")

    
if __name__ == '__main__':
    main()
