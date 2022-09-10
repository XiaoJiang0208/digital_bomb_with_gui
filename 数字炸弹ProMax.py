'''
made by xiaojiang (21计算机2江济民)
python编程复习(毕生所学doge)
'''

#导入gui库
from cProfile import label
from socket import BTPROTO_RFCOMM
from tkinter import *

#create the mainWindow
mainWindow = Tk()

def initMainWindow():
    '''init the mainWindow'''
    mainWindow.title("数字炸弹ProMax")
    mainWindow.geometry("1200x800")
    mainWindow.resizable(0,0)
    
#button event
def num1():
    pass
    
def drawMainWindow():
    '''draw mainWindow'''
    lb1 = Label(mainWindow, text="数字炸弹ProMax",font=("",50), justify=CENTER)
    lb1.pack(side=TOP)
    
    #add img
    global photo
    photo = PhotoImage(file="c4.gif")
    imgLb1 = Label(mainWindow,image=photo)
    imgLb1.pack(expand=True, fill=BOTH, side=BOTTOM)
    
    #add number button
    btMun1 = Button(imgLb1,text="1", command=num1).pack(pady=(375,0), ipadx=4)
    
    
if __name__ == "__main__":
    initMainWindow()
    drawMainWindow()
    mainWindow.mainloop()
