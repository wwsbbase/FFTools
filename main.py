#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from Tkconstants import *
from tkFileDialog import *

class ToolApp(object):
    """docstring for ToolApp"""
    def __init__(self, arg):
        super(ToolApp, self).__init__()
        self.arg = arg
        frame = Frame(arg)
        frame.pack()
        self.button = Button(frame, text="start", command=self.start)
        self.button.pack(side=LEFT)

        self.selectSourceButton = Button(frame, text="选择源文件", command=self.selectSourceFile)
        self.selectSourceButton.pack(side=LEFT)
    def start(self):
        """docstring for start"""
        print("begin to start")

    def selectSourceFile(self):
        """docstring for selectSourceFile"""
        self.openfilename = askopenfilename()
        
        

def createUI():
    """docstring for createUI"""
    win = Tk()
    win.title("FFTools")
    win.geometry("400x200")
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
