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

        frm_source = Frame(frm)
        frm_dest = Frame(frm)
        frm_formate = Frame(frm)
        self.frm_cutPoints = Frame(frm)

        self.cutPoints_objects = []
        self.cutPoints_start_values = []
        self.cutPoints_end_values = []

        frm_B = Frame(root)
        # 源文件
        self.sourceFileLabel = Label(frm_source, text="源文件：")
        self.sourceFileLabel.pack(side=LEFT)

        self.sourceFileName = StringVar()
        self.sourceFileEntry = Entry(frm_source,  textvariable=self.sourceFileName)
        self.sourceFileName.set("请选择源文件")
        self.sourceFileEntry.pack(side=LEFT)

        self.selectSourceButton = Button(frm_source, text="选择源文件", command=self.selectSourceFile)
        self.selectSourceButton.pack(side=LEFT)
        # 目标文件
        self.desFileLabel = Label(frm_dest, text="目标文件：")
        self.desFileLabel.pack(side=LEFT)
        
        self.desFileName = StringVar()
        self.desFileEntry = Entry(frm_dest, textvariable=self.desFileName)
        self.desFileEntry.pack(side=LEFT)

        self.formateLabel= Label(frm_formate, text="格式：")
        self.formateLabel.pack(side=LEFT)
        
        self.formateStr= StringVar()
        # self.formateEntry = Entry(frm_M, textvariable=self.formateStr)
        # self.formateEntry.pack()
        self.formateCombobox = ttk.Combobox(frm_formate, textvariable=self.formateStr)
        self.formateCombobox['value'] = ('mp4','mov','avi','mpeg')
        self.formateCombobox.pack(side=LEFT)

        # 起始位置
        self.addCutPoint()

        #开始按钮
        self.button = Button(frm_B, text="add~", command=self.addCutPoint)
        self.button.pack(side=BOTTOM)

        self.button = Button(frm_B, text="remove~", command=self.removeCutPoint)
        self.button.pack(side=BOTTOM)

        self.button = Button(frm_B, text="Start~", command=self.start)
        self.button.pack(side=BOTTOM)


        frm_source.pack(side=TOP, anchor=W)
        frm_dest.pack(side=TOP, anchor=W)
        frm_formate.pack(side=TOP, anchor=W)
        self.frm_cutPoints.pack(side=TOP, anchor=W)


        frm.pack(side=TOP)
        frm_B.pack(side=TOP)
        root.pack()
        print(os.path.abspath(__file__))
        print(sys.path[0])



        
    def addCutPoint(self):
        frm_cutPointNew = Frame(self.frm_cutPoints)
        startPosLabel= Label(frm_cutPointNew, text="开始位置：")
        startPosLabel.pack(side=LEFT)
        
        startPosStr= StringVar()
        startPosEntry= Entry(frm_cutPointNew, textvariable=startPosStr)
        startPosStr.set("00:00:00.00")
        startPosEntry.pack(side=LEFT)

        endPosLabel= Label(frm_cutPointNew, text="结束位置：")
        endPosLabel.pack(side=LEFT)
        
        endPosStr= StringVar()
        endPosEntry= Entry(frm_cutPointNew, textvariable=endPosStr)
        endPosStr.set("00:00:00.00")
        endPosEntry.pack(side=LEFT)
        frm_cutPointNew.pack(side=TOP)

        self.cutPoints_objects.append(frm_cutPointNew)
        self.cutPoints_start_values.append(startPosStr)
        self.cutPoints_end_values.append(endPosStr)

        print(len(self.cutPoints_objects))

        
    def removeCutPoint(self):
        if len(self.cutPoints_objects) < 2:
            print("the last point")
            return
        else:
            lastOne = self.cutPoints_objects[-1]
            lastOne.destroy()
            del self.cutPoints_objects[-1]
            del self.cutPoints_start_values[-1]
            del self.cutPoints_end_values[-1]

            print(len(self.cutPoints_objects))

    def start(self):
        """docstring for start"""
        # print("begin to start", self.desFileName.get())
        # os.system("./ffmpeg/bin/ffmpeg.exe")
        # exePath = "D:/GitHub/FFTools/ffmpeg/bin/ffmpeg.exe"

        #exePath = "D:/Project/GitHub/FFTools/ffmpeg/bin/ffmpeg.exe"
        filePath = sys.path[0] + "/ffmpeg/bin/ffmpeg.exe"

        
        for index in range(0,len(self.cutPoints_objects)):
            exePath = filePath
            exePath = exePath + " -i " + "\"" + self.sourceFileName.get() + "\""
            exePath = exePath + " -c copy"
            exePath = exePath + " -ss " + self.cutPoints_start_values[index].get()
            exePath = exePath + " -to " + self.cutPoints_end_values[index].get()
            exePath = exePath + " -f " + self.formateStr.get()
            if index == 0:
                exePath = exePath + " " + self.desFileName.get() + "." + self.formateStr.get()
            else:
                exePath = exePath + " " + self.desFileName.get() + "_" + str(index) + "." + self.formateStr.get()
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
