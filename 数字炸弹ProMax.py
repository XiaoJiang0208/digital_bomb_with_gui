'''
made by xiaojiang (21计算机2江济民)
python编程复习(毕生所学doge)
'''

#导入gui库
from cProfile import label
from tkinter import *

#create the mainWindow
mainWindow = Tk()

def initMainWindow():
    '''init the mainWindow'''
    mainWindow.title("数字炸弹ProMax")
    mainWindow.geometry("700x400")
    mainWindow.resizable(0,0)
    
def drawMainWindow():
    '''draw mainWindow'''
    lb1 = Label(mainWindow, text="数字炸弹ProMax",font=("",50), justify=CENTER)
    lb1.grid(column=0,row=0)
    lb1.pack(side=TOP)
    
    #add img
    photo = PhotoImage(file="c4.gif")
    imgLb1 = Label(mainWindow,image=photo)
    imgLb1.pack(side=BOTTOM)
    
if __name__ == "__main__":
    initMainWindow()
    drawMainWindow()
    mainWindow.mainloop()
