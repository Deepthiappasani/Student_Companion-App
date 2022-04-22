from libraries import *

class createEventFrame:
    def __init__(self,frames,calUtil,frameUtil,calendarViewFrame):
        self.frames = frames
        self.calUtil = calUtil
        self.frameUtil = frameUtil
        self.calendarViewFrame = calendarViewFrame

    def startCreateEventFrame(self):
        tk.Label(self.frames.createevent,text="Create an Event",font=("Courier", 44),bg='lightblue').grid(row=1,column=1,columnspan=5)
        tk.Label(self.frames.createevent,text="Select a Date: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
        tk.Label(self.frames.createevent,text="Select a Time: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
                                                
        tk.Button(self.frames.createevent,font=("Courier", 22),bg='cyan',text="Create Event",command=lambda :self.calUtil.createEvent(self.calendarViewFrame)).grid(row=5,column=2)
        tk.Button(self.frames.createevent,font=("Courier", 22),bg='cyan',text="Back",command=self.frameUtil.moveToUser).grid(row=5,column=1)        
