from libraries import *

class userFrame:
    def __init__(self,frames,loggedInLabel,frameUtil):
        self.frames = frames
        self.loggedInLabel = loggedInLabel
        self.frameUtil = frameUtil

    def startUserFrame(self):
        tk.Label(self.frames.userFrame,textvariable = self.loggedInLabel,font=("Courier", 44),bg='lightblue',fg="blue").grid(row=1,column=1,columnspan=5)
        tk.Button(self.frames.userFrame,font=("Courier", 22),bg='cyan',text="Create Event",command=self.frameUtil.moveToevent).grid(row=3,column=2)
        tk.Button(self.frames.userFrame,font=("Courier", 22),bg='cyan',text="Home",command = self.frameUtil.moveToMenu).grid(row=0,column = 0)        
