from tkinter import ttk
from tkinter import *
import calendar
from datetime import date
class MyCalendar:
    def __init__(self,root):
        self.root = root
        self.date = date.today()
        self.monthVar = self.date.month
        self.yearVar = self.date.year
        self.dateVar = 1
        self.num_days = calendar.monthrange(self.yearVar, self.monthVar)[1]
        
        self.heading = ttk.Label(root,text = "My Calendar")
        self.heading.grid(row = 0,column = 3)
        self.prevbutton = ttk.Button(root,text = "<",command = self.prevMonth)
        self.prevbutton.grid(row = 1,column = 2)
        self.heading2 = ttk.Label(root,text=f"{calendar.month_name[self.monthVar]} {self.yearVar}")
        self.heading2.grid(row = 1,column = 3)
        self.nextbutton = ttk.Button(root,text=">",command=self.nextMonth)
        self.nextbutton.grid(row = 1,column = 4)
        
        ttk.Button(root,text="Mon",state = DISABLED).grid(row = 2,column = 0)
        ttk.Button(root,text="Tue",state = DISABLED).grid(row = 2,column = 1)
        ttk.Button(root,text="Wed",state = DISABLED).grid(row = 2,column = 2)
        ttk.Button(root,text="Thu",state = DISABLED).grid(row = 2,column = 3)
        ttk.Button(root,text="Fri",state = DISABLED).grid(row = 2,column = 4)
        ttk.Button(root,text="Sat",state = DISABLED).grid(row = 2,column = 5)
        ttk.Button(root,text="Sun",state = DISABLED).grid(row = 2,column = 6)
        self.addbuttons()
        
    def addbuttons(self):
        rowNo = 3
        columnNo = calendar.monthrange(self.yearVar,self.monthVar)[0]
        self.num_days = calendar.monthrange(self.yearVar, self.monthVar)[1]
        self.heading2.config(text=f"{calendar.month_name[self.monthVar]} {self.yearVar}")
        self.dateVar = 1
        while self.dateVar <= self.num_days:
            ttk.Button(self.root,text=f"{self.dateVar}").grid(row = rowNo,column=columnNo)
            self.dateVar += 1
            if columnNo == 6:
                columnNo = 0
                rowNo += 1
            else:
                columnNo += 1
        
                
    def prevMonth(self):
        self.deletewidgets()
        if self.monthVar == 1:
            self.monthVar = 12
            self.yearVar -= 1
        else:
            self.monthVar -= 1
        self.addbuttons()
    def nextMonth(self):
        self.deletewidgets()
        if self.monthVar == 12:
            self.monthVar = 1
            self.yearVar += 1
        else:
            self.monthVar += 1
        self.addbuttons()
    def deletewidgets(self):
        for i in range(3,10):
            for widget in self.root.grid_slaves(row = i):
                widget.destroy()
