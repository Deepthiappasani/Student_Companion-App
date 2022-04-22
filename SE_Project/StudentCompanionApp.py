from libraries import *
from Frames import *
from FrameUtils import *
from Calendar import *
'''root Frame'''
root = tk.Tk()
root.title("Student Companion App")
root.resizable(True,True)

'''Variables'''
username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()

'''#Define Image'''
companionimage = Image.open("studentcompanion.png")
companionImg = ImageTk.PhotoImage(companionimage )

'''Generating Frames'''
frames = defineFrames(root)
frames.startFrames()

'''frameRaise Utils'''
frameUtil = frameRaiseUtils(frames.frameList)

'''calendar Frame'''
calendarFrame = calendarFrame(frames)
calendarFrame.startCalendarFrame()
datePicker = calendarFrame.getDatePicker()

'''Calendar Utils'''
calUtil = calendarUtils(frames.userFrame,datePicker,minutes,hours,name)

'''userAccountUtils'''
userUtil = userAccountUtils(frames.frameList)
calendarViewFrame = userUtil.getCalendarViewFrame()

'''subject Utils'''
subUtil = subjectUtils(frames.subjectFrame)

'''activites Utils'''
actUtil = activitiesUtils(frames.activitiesFrame)
				
'''Call Setup'''
setupUtil = setupUtils()
setupUtil.setup()

'''Start Frame'''
startFrame = startFrame(frames,[name,username,password],userUtil,frameUtil,loggedInLabel)
startFrame.startStartFrame()

'''Register Frame'''
regFrame = registerFrame(frames,[name,username,password],userUtil,frameUtil,loggedInLabel)
regFrame.startRegFrame()

'''Menu Frame'''
menuFrame = menuFrame(frames,[name,username,password],userUtil,frameUtil,loggedInLabel)
menuFrame.startMenuFrame()

'''Subjects Frame'''
subjectFrame = subjectFrame(frames,subUtil,frameUtil)
subjectFrame.startSubjectFrame()

'''Activities Frame'''
activitiesFrame = activitiesFrame(frames,actUtil,frameUtil)
activitiesFrame.startActivitiesFrame()

'''User Frame'''
userFrame = userFrame(frames,loggedInLabel,frameUtil)
userFrame.startUserFrame()

'''createevent Frame'''
createeventFrame = createEventFrame(frames,calUtil,frameUtil,calendarViewFrame)
createeventFrame.startCreateEventFrame()

'''Time Selector'''
timeSelectFrame = timeSelectFrame(frames,hours,minutes)
timeSelectFrame.startTimeSelectFrame()

'''Raise Initial Frame'''
frameUtil.raiseFrame(frames.start)

root.mainloop()
