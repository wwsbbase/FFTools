#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from Tkconstants import *
from tkFileDialog import *
import os
import subprocess

win_width = 29
combox_width = 27
# win_height= 80

class ToolApp(object):
    """docstring for ToolApp"""
    def __init__(self, arg):
        super(ToolApp, self).__init__()
        self.arg = arg
        frm = self.arg
        Label(frm, text="FFTools", font=("Arial", 17)).grid(row=0, sticky=E)


        # 源文件
        self.sourceFileLabel = Label(frm, text="源文件：")
        self.sourceFileLabel.grid(row=1, column=0, sticky=E)

        self.sourceFileName = StringVar()
        self.sourceFileEntry = Entry(frm, width=win_width, textvariable=self.sourceFileName)
        self.sourceFileName.set("请选择源文件")
        self.sourceFileEntry.grid(row=1, column=1, sticky=E)

        self.selectSourceButton = Button(frm, text="选择源文件", command=self.selectSourceFile)
        self.selectSourceButton.grid(row=1, column=2, sticky=E)
        # 目标文件
        self.desFileLabel = Label(frm, text="目标文件：")
        self.desFileLabel.grid(row=2, column=0, sticky=E)
        
        self.desFileName = StringVar()
        self.desFileEntry = Entry(frm, width=win_width, textvariable=self.desFileName)
        self.desFileEntry.grid(row=2, column=1, sticky=E)

        # 起始位置
        self.startPosLabel= Label(frm, text="开始位置：")
        self.startPosLabel.grid(row=3, column=0, sticky=E)
        
        self.startPosStr= StringVar()
        self.startPosEntry= Entry(frm, width=win_width, textvariable=self.startPosStr)
        self.startPosEntry.grid(row=3, column=1, sticky=E)

        self.endPosLabel= Label(frm, text="结束位置：")
        self.endPosLabel.grid(row=4, column=0, sticky=E)
        
        self.endPosStr= StringVar()
        self.endPosEntry= Entry(frm, width=win_width, textvariable=self.endPosStr)
        self.endPosEntry.grid(row=4, column=1, sticky=E)

        self.formateLabel= Label(frm, text="格式：")
        self.formateLabel.grid(row=5, column=0, sticky=E)
        
        self.formateStr= StringVar()
        # self.formateEntry = Entry(frm, textvariable=self.formateStr)
        # self.formateEntry.grid()
        self.formateCombobox = ttk.Combobox(frm, width=combox_width, textvariable=self.formateStr)
        self.formateCombobox['value'] = ('mp4','mov','avi','mpeg')
        self.formateCombobox.grid(row=5, column=1, sticky=E)


        self.button = Button(frm, text="Start~", command=self.start)
        self.button.grid(row=6, column=1, sticky=E)
        
        testProgress = Scale(frm, from_=0, to=100, orient=HORIZONTAL)
        testProgress.grid(row=6, column=0, sticky=E)


        
    def start(self):
        """docstring for start"""
        # print("begin to start", self.desFileName.get())
        # os.system("./ffmpeg/bin/ffmpeg.exe")
        # exePath = "D:/GitHub/FFTools/ffmpeg/bin/ffmpeg.exe"
        exePath = "D:/Project/GitHub/FFTools/ffmpeg/bin/ffmpeg.exe"
        exePath = exePath + " -i " + "\"" + self.sourceFileName.get() + "\""
        exePath = exePath + " -c copy"
        exePath = exePath + " -ss " + self.startPosStr.get()
        exePath = exePath + " -to " + self.endPosStr.get()
        exePath = exePath + " -f " + self.formateStr.get()
        exePath = exePath + " " + self.desFileName.get() + "." + self.formateStr.get()
        print(exePath)
        self.subpro = subprocess.Popen(exePath, shell=True)
        self.subpro.wait()

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
