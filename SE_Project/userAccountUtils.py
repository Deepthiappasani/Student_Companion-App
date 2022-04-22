from libraries import *
from Calendar import *
from dbmsfunctions import connectToDBMS, newUser, verifyUser
class userAccountUtils:

        def __init__(self,l):
                self.regFrame = l[2]
                self.start = l[0]
                self.createevent = l[4]
                self.userFrame = l[3]
                self.subjectFrame = l[5]
                self.menu = l[1]
                self.calendarViewFrame = None
        
        def register(self,l):
                entries = []
                connectToDBMS()
                newUser(name = l[0].get(),username = l[1].get(), password = l[2].get())
                #Clear entry boxes
                l[0].set("")
                l[1].set("")
                self.start.tkraise()

        def login(self,l):        
                '''with open("users.txt",'r') as userFile:
                        reader = csv.reader(userFile)
                        for row in reader:
                                #removes empty list from loop
                                if len(row)>0:
                                        if l[0].get()==row[1] and l[1].get()==row[2]:
                                                print(row[0]+" has logged in!")
                                                '''
                connectToDBMS()
                if verifyUser(l[0].get(),l[1].get()):
                        # Calendar View
                        global calendarViewFrame
                        calendarViewFrame = tk.Frame(self.userFrame, borderwidth=5, bg="lightblue")
                        calendarViewFrame.grid(row=2, column=1, columnspan=5)
                        self.calendarViewFrame = calendarViewFrame
                        viewCalendar = CalendarView(self.calendarViewFrame, {l[0].get()})
                        #Set welcome message
                        l[2].set("Welcome, "+l[0].get())
                        l[3].set(l[0].get())
                        self.menu.tkraise()

        def logOut(self,l):
                #Clear Entry boxes
                l[0].set("")
                l[1].set("")
                l[2].set("")
                self.start.tkraise()
        
        def getCalendarViewFrame(self):
                return self.calendarViewFrame