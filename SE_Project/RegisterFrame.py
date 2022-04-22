from libraries import *

class registerFrame:
    def __init__(self,frames,l,userUtil,frameUtil,loggedInLabel):
        self.frames = frames
        self.name = l[0]
        self.username = l[1]
        self.password = l[2]
        self.userUtil = userUtil
        self.frameUtil = frameUtil
        self.loggedInLabel = loggedInLabel

    def startRegFrame(self):
        tk.Label(self.frames.regFrame,text="Register",font=("Courier", 44),bg='lightblue').grid(row=1,column=1,columnspan=5)
        tk.Label(self.frames.regFrame,text="Name: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
        tk.Label(self.frames.regFrame,text="Username: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
        tk.Label(self.frames.regFrame,text="Password: ",font=("Courier", 22),bg='lightblue').grid(row=4,column=1)

        tk.Entry(self.frames.regFrame,textvariable=self.name,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
        tk.Entry(self.frames.regFrame,textvariable=self.username,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)
        tk.Entry(self.frames.regFrame,textvariable=self.password,font=("Courier", 22),bg='lightblue').grid(row=4,column=2)

        register_partial = partial(self.userUtil.register,[self.name,self.username,self.password,self.loggedInLabel])
        tk.Button(self.frames.regFrame,font=("Courier", 22),bg='cyan',text="Register",command=register_partial).grid(row=5,column=2)
        tk.Button(self.frames.regFrame,font=("Courier", 22),bg='cyan',text="Back",command=self.frameUtil.moveToLogin).grid(row=5,column=1)
        
