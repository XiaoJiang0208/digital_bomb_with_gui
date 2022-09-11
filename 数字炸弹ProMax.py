'''
made by xiaojiang (21计算机2江济民)
python编程复习(毕生所学doge)
'''


#导入gui库
from operator import le
from tkinter import *


#create the mainWindow
mainWindow = Tk()


#全局变量
Min = 0
Max = 100
LEDtext = "enter the password(" + str(Min) + "~" + str(Max) + ")"
ans = [0]

def initMainWindow():
    '''init the mainWindow'''
    mainWindow.title("数字炸弹ProMax")
    mainWindow.geometry("1200x800")
    mainWindow.resizable(0,0)

def setLEDtestSize(min, max, ans):
    '''设置LDE数字范围'''
    LEDtext = "(" + str(min) + "~" + str(max) + "):" + str(ans)
    LED.configure(text=LEDtext)
    mainWindow.after(1000, setLEDtestSize)


#button event-----
#tool
def addNum(num):
    ans.append(num)
    ans[0]=0
    for i in range(1,len(ans)):
        if ans[len(ans)-i] == 0:
            ans[0]*10
        ans[0]+=ans[len(ans)-i]*(10**i)
    ans[0]=ans[0]//10
    setLEDtestSize(Min, Max, ans[0])
#events
def num1():
    addNum(1)
def num2():
    addNum(2)
def num3():
    addNum(3)
def num4():
    addNum(4)
def num5():
    addNum(5)
def num6():
    addNum(6)
def num7():
    addNum(7)
def num8():
    addNum(8)
def num9():
    addNum(9)
def num0():
    addNum(0)
    
def drawMainWindow():
    '''draw the window'''
    global photo
    photo = PhotoImage(file="c4.gif")
    global photoLabel
    photoLabel = Label(mainWindow, image=photo).place(x=0, y=0)
    
    #LED
    global LED
    LED = Label(mainWindow, text=LEDtext, bg="#edd605")
    LED.pack(pady=(160,0), padx=(30,0))
    
    #add number keyBoark
    global keyBoard
    keyBoard = Frame(photoLabel, bg="#141c0c").pack(pady=(156,0))
    #1,2,3
    global key123
    key123 = Frame(keyBoard, bg="#141c0c")
    key123.pack()
    global but1
    but1 = Button(key123, text="1", bg="#b99f7d", command=num1)
    but1.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but2
    but2 = Button(key123, text="2", bg="#b99f7d", command=num2)
    but2.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but3
    but3 = Button(key123, text="3", bg="#b99f7d", command=num3)
    but3.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    #4,5,6
    global key456
    key456 = Frame(keyBoard, bg="#141c0c")
    key456.pack()
    global but4
    but4 = Button(key456, text="4", bg="#b99f7d", command=num4)
    but4.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but5
    but5 = Button(key456, text="5", bg="#b99f7d", command=num5)
    but5.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but6
    but6 = Button(key456, text="6", bg="#b99f7d", command=num6)
    but6.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    #7,8,9
    global key789
    key789 = Frame(keyBoard, bg="#141c0c")
    key789.pack()
    global but7
    but7 = Button(key789, text="4", bg="#b99f7d", command=num7)
    but7.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but8
    but8 = Button(key789, text="5", bg="#b99f7d", command=num8)
    but8.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but9
    but9 = Button(key789, text="6", bg="#b99f7d", command=num6)
    but9.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    #del,0,ok
    global keyD0O
    keyD0O = Frame(keyBoard, bg="#141c0c")
    keyD0O.pack()
    global butDel
    butDel = Button(keyD0O, text="*", bg="#b99f7d")
    butDel.pack(side=LEFT, padx=5, pady=5, ipadx=6)
    global but0
    but0 = Button(keyD0O, text="0", bg="#b99f7d", command=num0)
    but0.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global butOK
    butOK = Button(keyD0O, text="#", bg="#b99f7d")
    butOK.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    
    #Title
    global title1
    title1 = Label(mainWindow, text="数字炸弹ProMax", font=("", 80), fg="#7cdcfe").pack(side=BOTTOM)


if __name__ == "__main__":
    initMainWindow()
    drawMainWindow()
    mainWindow.mainloop()