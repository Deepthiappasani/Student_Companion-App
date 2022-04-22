from libraries import *

class defineFrames:
    def __init__(self,root):
        self.root = root
        self.start = None
        self.menu = None
        self.regFrame = None
        self.userFrame = None
        self.createevent = None
        self.subjectFrame = None
        self.frameList = None
        self.activitiesFrame = None
        
    def startFrames(self):
        self.start = tk.Frame(self.root)
        self.menu = tk.Frame(self.root)
        self.regFrame = tk.Frame(self.root)
        self.userFrame = tk.Frame(self.root)
        self.createevent = tk.Frame(self.root)
        self.subjectFrame = tk.Frame(self.root)
        self.activitiesFrame = tk.Frame(self.root)
        self.frameList=[self.start, self.menu,self.regFrame,self.userFrame,self.createevent,self.subjectFrame,self.activitiesFrame]

        for frame in self.frameList:
            frame.grid(row=0,column=0, sticky='news')
            frame.configure(bg='lightblue')
