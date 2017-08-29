#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from Tkconstants import *
from tkFileDialog import *
import os
import subprocess

class ToolApp(object):
    """docstring for ToolApp"""
    def __init__(self, arg):
        super(ToolApp, self).__init__()
        self.arg = arg
        root = Frame(arg)
        Label(root, text="FFTools", font=("Arial", 17)).pack()

        frm = Frame(root)

        frm_L = Frame(frm)
        frm_M = Frame(frm)
        frm_R = Frame(frm)

        frm_B = Frame(root)
        # 源文件
        self.sourceFileLabel = Label(frm_L, text="源文件：")
        self.sourceFileLabel.pack(side=TOP)

        self.sourceFileName = StringVar()
        self.sourceFileEntry = Entry(frm_M,  textvariable=self.sourceFileName)
        self.sourceFileName.set("请选择源文件")
        self.sourceFileEntry.pack()

        self.selectSourceButton = Button(frm_R, text="选择源文件", command=self.selectSourceFile)
        self.selectSourceButton.pack()
        # 目标文件
        self.desFileLabel = Label(frm_L, text="目标文件：")
        self.desFileLabel.pack(side=TOP)
        
        self.desFileName = StringVar()
        self.desFileEntry = Entry(frm_M, textvariable=self.desFileName)
        self.desFileEntry.pack()

        # 起始位置
        self.startPosLabel= Label(frm_L, text="开始位置：")
        self.startPosLabel.pack(side=TOP)
        
        self.startPosStr= StringVar()
        self.startPosEntry= Entry(frm_M, textvariable=self.startPosStr)
        self.startPosEntry.pack()

        self.endPosLabel= Label(frm_L, text="结束位置：")
        self.endPosLabel.pack(side=TOP)
        
        self.endPosStr= StringVar()
        self.endPosEntry= Entry(frm_M, textvariable=self.endPosStr)
        self.endPosEntry.pack()

        self.formateLabel= Label(frm_L, text="格式：")
        self.formateLabel.pack(side=TOP)
        
        self.formateStr= StringVar()
        # self.formateEntry = Entry(frm_M, textvariable=self.formateStr)
        # self.formateEntry.pack()
        self.formateCombobox = ttk.Combobox(frm_M, textvariable=self.formateStr)
        self.formateCombobox['value'] = ('mp4','mov','avi','mpeg')
        self.formateCombobox.pack()


        self.button = Button(frm_B, text="Start~", command=self.start)
        self.button.pack(side=BOTTOM)
        frm_L.pack(side=LEFT)
        frm_M.pack(side=LEFT)
        # frm_M.pack()
        frm_R.pack(side=TOP, anchor=W)
        frm.pack()
        frm_B.pack()
        root.pack()
        
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
