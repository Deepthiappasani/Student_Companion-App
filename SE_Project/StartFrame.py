from libraries import *

class startFrame:
    def __init__(self,frames,l,userUtil,frameUtil,loggedInLabel):
        self.frames = frames
        self.name = l[0]
        self.username = l[1]
        self.password = l[2]
        self.userUtil = userUtil
        self.frameUtil = frameUtil
        self.loggedInLabel = loggedInLabel

    def startStartFrame(self):
        tk.Label(self.frames.start,text="Student Companion App",font=("Courier", 60),bg='lightblue').grid(row=0,column=1,columnspan=5)
        #tk.Label(self.frames.start,image=companionImg,bg='lightblue').grid(row=1,column=1,columnspan=5)
        tk.Label(self.frames.start,text="Username: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
        tk.Label(self.frames.start,text="Password: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
        
        tk.Entry(self.frames.start,textvariable=self.username,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
        tk.Entry(self.frames.start,textvariable=self.password,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)
        
        login_partial = partial(self.userUtil.login,[self.username,self.password,self.loggedInLabel,self.name])
        tk.Button(self.frames.start,font=("Courier", 22),bg='cyan',text="Login",command=login_partial).grid(row=4,column=2)
        tk.Button(self.frames.start,font=("Courier", 22),bg='cyan',text="Register",command=self.frameUtil.moveToReg).grid(row=4,column=1)
