from libraries import *

class menuFrame:
    def __init__(self,frames,l,userUtil,frameUtil,loggedInLabel):
        self.frames = frames
        self.name = l[0]
        self.username = l[1]
        self.password = l[2]
        self.userUtil = userUtil
        self.frameUtil = frameUtil
        self.loggedInLabel = loggedInLabel

    def startMenuFrame(self):
        tk.Label(self.frames.menu,textvariable = self.loggedInLabel,font=("Courier", 44),bg='lightblue',fg="blue").grid(row=1,column=1,columnspan=5)

        goToCalendar = tk.Button(self.frames.menu,font=("Courier", 22),bg='cyan',text="Calendar",command = self.frameUtil.moveToUser).grid(row = 4, column = 3)

        goToPapers = tk.Button(self.frames.menu,font=("Courier", 22),bg='cyan',text="Books and Papers",command = self.frameUtil.moveToSubject).grid(row = 4, column = 4)

        goToActivities = tk.Button(self.frames.menu,font=("Courier", 22),bg='cyan',text="Activities",command = self.frameUtil.moveToActivities).grid(row = 4, column = 5)

        logOut_partial = partial(self.userUtil.logOut,[self.name,self.username,self.password])
        menuLogOut = tk.Button(self.frames.menu,font=("Courier", 22),bg='cyan', text = "Log Out",command = logOut_partial).grid(row = 6, column = 0)

        sep1 = ttk.Separator(self.frames.menu).grid(row = 2,column = 0,columnspan = 6)        
