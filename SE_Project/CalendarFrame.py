from libraries import *
from Calendar_GUI import Calendar
from CalendarView_GUI import CalendarView

class calendarFrame:
    def __init__(self,frames):
        self.frames = frames
        self.datePickercalendar = None
    
    def startCalendarFrame(self):
        calendarFrame = tk.Frame(self.frames.createevent, borderwidth=5, bg="lightblue")
        calendarFrame.grid(row=2, column=2, columnspan=5)
        datePickercalendar = Calendar(calendarFrame, {})
        self.datePickercalendar = datePickercalendar

    def getDatePicker(self):
        return self.datePickercalendar
