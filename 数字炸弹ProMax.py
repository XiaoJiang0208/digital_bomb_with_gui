'''
made by xiaojiang (21计算机2江济民)
python编程复习(毕生所学doge)
'''

#导入gui库
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
    global photo
    photo = PhotoImage(file="c4.gif")
    global photoLabel
    photoLabel = Label(mainWindow, image=photo).pack()
    
    #add number keyBoark
    global keyBoard
    keyBoard = Frame(photoLabel).pack()
    #1,2,3
    global key123
    key123 = Frame(keyBoard)
    key123.pack()
    global but1
    but1 = Button(key123, text="1")
    but1.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but2
    but2 = Button(key123, text="2")
    but2.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but3
    but3 = Button(key123, text="3")
    but3.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    #4,5,6
    global key456
    key456 = Frame(keyBoard)
    key456.pack()
    global but4
    but4 = Button(key456, text="4")
    but4.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but5
    but5 = Button(key456, text="5")
    but5.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but6
    but6 = Button(key456, text="6")
    but6.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    #7,8,9
    global key789
    key789 = Frame(keyBoard)
    key789.pack()
    global but7
    but7 = Button(key789, text="4")
    but7.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but8
    but8 = Button(key789, text="5")
    but8.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global but9
    but9 = Button(key789, text="6")
    but9.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    #del,0,ok
    global keyD0O
    keyD0O = Frame(keyBoard)
    keyD0O.pack()
    global butDel
    butDel = Button(keyD0O, text="*")
    butDel.pack(side=LEFT, padx=5, pady=5, ipadx=6)
    global but0
    but0 = Button(keyD0O, text="0")
    but0.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    global butOK
    butOK = Button(keyD0O, text="#")
    butOK.pack(side=LEFT, padx=5, pady=5, ipadx=5)
    
if __name__ == "__main__":
    initMainWindow()
    drawMainWindow()
    mainWindow.mainloop()