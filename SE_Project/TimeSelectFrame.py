from libraries import *

class timeSelectFrame:
    def __init__(self,frames,hours,minutes):
        self.frames = frames
        self.hours = hours
        self.minutes = minutes

    def startTimeSelectFrame(self):
        timeSelectFrame = tk.Frame(self.frames.createevent,borderwidth=5,bg="lightblue")
        timeSelectFrame.grid(row=3,column=2)
        tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="lightblue",width=2,textvariable=self.hours).grid(row=1,column=1)
        tk.Label(timeSelectFrame,text=":",bg="lightblue").grid(row=1,column=2)
        tk.Spinbox(timeSelectFrame,width=2,textvariable=self.minutes,values=(0,15,30,45),bg="lightblue").grid(row=1,column=3)        
