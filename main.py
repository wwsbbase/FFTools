#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from Tkconstants import *
from tkFileDialog import *
import os
import subprocess

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

class ToolApp(object):
    """docstring for ToolApp"""
    def __init__(self, arg):
        super(ToolApp, self).__init__()
        self.arg = arg
        root = Frame(arg)
        Label(root, text="FFTools", font=("Arial", 17)).pack()

        frm = Frame(root)

        frm_source = Frame(frm, pady=5)
        frm_dest = Frame(frm, pady=5)
        frm_formate = Frame(frm, pady=5)
        frm_control = Frame(frm, pady=5)
        self.frm_cutPoints = Frame(frm, pady=5)

        self.cutPoints_objects = []
        self.cutPoints_start_values = []
        self.cutPoints_end_values = []

        frm_B = Frame(root)
        # 源文件
        sourceFileLabel = Label(frm_source, text="源文件：")
        sourceFileLabel.pack(side=LEFT)

        self.sourceFileName = StringVar()
        sourceFileEntry = Entry(frm_source,  textvariable=self.sourceFileName, width=40)
        self.sourceFileName.set("请选择源文件")
        sourceFileEntry.pack(side=LEFT, padx=25)

        selectSourceButton = Button(frm_source, text="选择源文件", command=self.selectSourceFile)
        selectSourceButton.pack(side=LEFT, padx=10)
        # 目标文件
        desFileLabel = Label(frm_dest, text="目标文件名：")
        desFileLabel.pack(side=LEFT)
        
        self.desFileName = StringVar()
        desFileEntry = Entry(frm_dest, textvariable=self.desFileName, width=40)
        desFileEntry.pack(side=LEFT, padx=1)
        # 格式选择
        formateLabel= Label(frm_formate, text="格式：")
        formateLabel.pack(side=LEFT)
        
        self.formateStr= StringVar()
        formateCombobox = ttk.Combobox(frm_formate, textvariable=self.formateStr)
        formateCombobox['value'] = ('mp4','mov','avi','mpeg')
        formateCombobox.pack(side=LEFT, padx=36)

        # 添加剪切点按钮
        addButton = Button(frm_control, text=" + ", command=self.addCutPoint, width=10)
        addButton.pack(side=LEFT)
        # 移出剪切点按钮
        cutButton = Button(frm_control, text=" - ", command=self.removeCutPoint, width=10)
        cutButton.pack(side=RIGHT)

        # 起始位置
        self.addCutPoint()

        #开始按钮
        startButton = Button(frm_B, text="Start~", command=self.start, width=20)
        startButton.pack(side=BOTTOM, anchor=S)

        frm_source.pack(side=TOP, anchor=W)
        frm_dest.pack(side=TOP, anchor=W)
        frm_formate.pack(side=TOP, anchor=W)
        frm_control.pack(side=TOP)

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
            sourceFilePath = self.sourceFileName.get()
            sourceFilePath = "\"" + sourceFilePath + "\""
            sourceFilePath = sourceFilePath.encode('gbk')

            
            FileTimeName = self.GetFileTimeName(index)

            desFilePath = self.desFileName.get()
            desFilePath = desFilePath + FileTimeName
            desFilePath = desFilePath.encode('gbk')
            #unicode(sourceFilePath, 'UTF-8')

            exePath = exePath + " -i " + sourceFilePath 
            exePath = exePath + " -c copy"
            exePath = exePath + " -ss " + self.cutPoints_start_values[index].get()
            exePath = exePath + " -to " + self.cutPoints_end_values[index].get()
            exePath = exePath + " -f " + self.formateStr.get()
            #if index == 0:
                #exePath = exePath + " " + "\"" + desFilePath + "." + self.formateStr.get() + "\""
            #else:
                #exePath = exePath + " " + "\"" + desFilePath + "_" + str(index) + "." + self.formateStr.get() + "\""

            exePath = exePath + " " + "\"" + desFilePath + "." + self.formateStr.get() + "\""
            print(exePath)
            
            self.subpro = subprocess.Popen(exePath, shell=True)
            self.subpro.wait()

    def GetFileTimeName(self, index):
        startTimeName = self.cutPoints_start_values[index].get()
        startTimeName = startTimeName.replace(":", "h", 1)
        startTimeName = startTimeName.replace(":", "m", 1)
        startTimeName = startTimeName.replace(".", "s", 1)

        endTimeName = self.cutPoints_start_values[index].get()
        endTimeName = endTimeName.replace(":", "h", 1)
        endTimeName = endTimeName.replace(":", "m", 1)
        endTimeName = endTimeName.replace(".", "s", 1)

        FileTimeName = "(" + startTimeName + "~" + endTimeName + ")"
        return FileTimeName
        #return ""
    def GetFileTimeNameTest(self):
        index = 0

        startTimeName = self.cutPoints_start_values[index].get()
        startTimeName = startTimeName.replace(":", "h", 1)
        startTimeName = startTimeName.replace(":", "m", 1)
        startTimeName = startTimeName.replace(".", "s", 1)

        endTimeName = self.cutPoints_start_values[index].get()
        endTimeName = endTimeName.replace(":", "h", 1)
        endTimeName = endTimeName.replace(":", "m", 1)
        endTimeName = endTimeName.replace(".", "s", 1)

        FileTimeName = "(" + startTimeName + "~" + endTimeName + ")"

        print FileTimeName
        #return FileTimeName
        return ""


    def selectSourceFile(self):
        """docstring for selectSourceFile"""
        filePath = askopenfilename()
        self.sourceFileName.set(filePath)

        filename = os.path.splitext(filePath)[0]
        self.desFileName.set(filename)
        

def createUI():
    """docstring for createUI"""
    win = Tk()
    win.title("FFTools")
    win.geometry("600x350")
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
