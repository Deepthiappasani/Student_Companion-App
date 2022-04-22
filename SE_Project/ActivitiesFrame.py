from pyparsing import anyCloseTag
from requests import delete
from dbmsfunctions import getActivity,deleteActivity, updateActivity
from libraries import *


class activitiesFrame:
    def __init__(self,frames,actUtil,frameUtil):
        self.frames = frames
        self.actUtil = actUtil
        self.frameUtil = frameUtil

        
    def startActivitiesFrame(self):
        
        tk.Button(self.frames.activitiesFrame,font=("Courier", 22),bg='cyan',text="Home",command = self.frameUtil.moveToMenu).grid(row=0,column = 0)
        label1 = ttk.Label(self.frames.activitiesFrame,text="My Planned Activities").grid(row = 0,column = 1,columnspan = 2)

        yscroll1 = ttk.Scrollbar(self.frames.activitiesFrame)
        yscroll2 = ttk.Scrollbar(self.frames.activitiesFrame)
        xscroll1 = ttk.Scrollbar(self.frames.activitiesFrame,orient = tk.HORIZONTAL)

        table = ttk.Treeview(self.frames.activitiesFrame,columns = ('ID','Name','Date','Start Time','End Time','Description'),yscrollcommand = yscroll2.set(0,0),xscrollcommand = xscroll1.set(0,0))
        table.grid(row=1,column = 1,columnspan = 6)

        table.column("#0", width=0)
        table.column("ID",anchor=CENTER, width=150,stretch=True)
        table.column("Name",anchor=CENTER,width=150,stretch=True)
        table.column("Date",anchor=CENTER,width=150,stretch=True)
        table.column("Start Time",anchor=CENTER,width=150,stretch=True)
        table.column("End Time",anchor=CENTER,width=150,stretch=True)
        table.column("Description",anchor=CENTER,width=350,stretch=True)

        table.heading("#0",text="",anchor=CENTER)
        table.heading("ID",text="ID",anchor=CENTER)
        table.heading("Name",text="Name",anchor=CENTER)
        table.heading("Date",text='Date',anchor = CENTER)
        table.heading("Start Time",text="Start Time",anchor=CENTER)
        table.heading("End Time",text="End Time",anchor=CENTER)
        table.heading("Description",text="Description",anchor=CENTER)

        activities = getActivity()
        for activity in activities:
            table.insert(parent='',index='end',text='',values=(activity[0],activity[1],activity[2],activity[3],activity[4],activity[5]))
        '''with open("Activities.txt",'r') as ActivityFile:
                reader = csv.reader(ActivityFile)
                for row in reader:
                        table.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4]))
        '''
        ID_entry = tk.StringVar()
        ID = ttk.Entry(self.frames.activitiesFrame,textvariable = ID_entry)
        ID.grid(row =2,column = 1)

        Name_entry = tk.StringVar()
        Name = ttk.Entry(self.frames.activitiesFrame,textvariable = Name_entry)
        Name.grid(row=2,column = 2)
        
        Date_Entry = tk.StringVar()
        Date = ttk.Entry(self.frames.activitiesFrame,textvariable = Date_Entry)
        Date.grid(row = 2,column = 3)

        ST_entry = tk.StringVar()
        ST = ttk.Entry(self.frames.activitiesFrame,textvariable = ST_entry)
        ST.grid(row = 2,column = 4)

        ET_entry = tk.StringVar()
        ET = ttk.Entry(self.frames.activitiesFrame,textvariable = ET_entry)
        ET.grid(row = 2,column = 5)

        Des_entry = tk.StringVar()
        Des = ttk.Entry(self.frames.activitiesFrame,textvariable = Des_entry)
        Des.grid(row = 2,column = 6)

        add_entry = partial(self.actUtil.activity_addition,[ID_entry,Name_entry,Date_Entry,ST_entry,ET_entry,Des_entry,table])
        addentrybutton = ttk.Button(self.frames.activitiesFrame,text="Add Entry",command = add_entry)
        addentrybutton.grid(row=2,column = 0)
        
        ttk.Label(self.frames.activitiesFrame,text="To modify or Delete, Enter ID").grid(row = 3,column = 0,columnspan = 3)
        Modify_entry = tk.StringVar()
        Modify = ttk.Entry(self.frames.activitiesFrame,textvariable = Modify_entry)
        Modify.grid(row = 3,column = 3)
        
        tk.Button(self.frames.activitiesFrame,text="Delete",command = partial(deleteActivity,Modify_entry)).grid(row=3,column = 4)
        tk.Button(self.frames.activitiesFrame,text="Modify",command = partial(updateActivity,ID_entry,Name_entry,Date_Entry,ST_entry,ET_entry,Des_entry)).grid(row=3,column = 5)