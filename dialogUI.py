from tkinter import *
import tkinter.filedialog as tkFileDialog
from GpaCalculator import GpaCalculator

def selectPath():
    path_ = tkFileDialog.askopenfilename()
    path.set(path_)

def calculate():
    try:
        cal=GpaCalculator(path.get())
        gpa.set("你的GPA："+str(cal.computeGPA()))
    except:
        gpa.set("文件内容不符合格式或未选择路径！")


root = Tk()
root.title("SEU-GPA")
path = StringVar()
gpa=StringVar()

Label(root,text = "文件路径:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
Label(root,textvariable=gpa).grid(row=2,column=1)
Button(root,text="计算GPA",command=calculate).grid(row=1,column=1)
root.mainloop()