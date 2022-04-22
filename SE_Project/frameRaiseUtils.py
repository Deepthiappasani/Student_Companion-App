from libraries import *

class frameRaiseUtils:

        def __init__(self,l):
                self.regFrame = l[2]
                self.start = l[0]
                self.createevent = l[4]
                self.userFrame = l[3]
                self.subjectFrame = l[5]
                self.menu = l[1]
                self.activitiesFrame = l[6]
                
        def raiseFrame(self,frame):
                frame.tkraise()
        def moveToReg(self):
                self.raiseFrame(self.regFrame)
        def moveToLogin(self):
                self.raiseFrame(self.start)
        def moveToevent(self):
                self.raiseFrame(self.createevent)
        def moveToUser(self):
                self.raiseFrame(self.userFrame)
        def moveToSubject(self):
                self.raiseFrame(self.subjectFrame)
        def moveToMenu(self):
                self.raiseFrame(self.menu)
        def moveToActivities(self):
                self.raiseFrame(self.activitiesFrame)
