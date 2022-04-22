from dbmsfunctions import *
from libraries import *

class subjectFrame:
    def __init__(self,frames,subUtil,frameUtil):
        self.frames = frames
        self.subUtil = subUtil
        self.frameUtil = frameUtil

    def startSubjectFrame(self):
        tk.Button(self.frames.subjectFrame,text="Home",command = self.frameUtil.moveToMenu).grid(row=0,column = 0)

        label1 = ttk.Label(self.frames.subjectFrame,text="My Books/Papers Collection").grid(row = 0,column = 1,columnspan = 4)

        yscroll1 = ttk.Scrollbar(self.frames.subjectFrame)
        yscroll2 = ttk.Scrollbar(self.frames.subjectFrame)
        xscroll1 = ttk.Scrollbar(self.frames.subjectFrame,orient = tk.HORIZONTAL)

        sidemenu = ttk.Treeview(self.frames.subjectFrame,columns = ('Subjects'))
        sidemenu.grid(row=1,column = 0)

        sidemenu.column('#0',width=0)
        sidemenu.column("Subjects",anchor=CENTER, width=80,stretch=True)
        sidemenu.heading("#0",text="",anchor=CENTER)
        sidemenu.heading("Subjects",text="Subjects",anchor=CENTER)
        connectToDBMS()
        subjects = getSubjects()
        for subject in subjects:
            sidemenu.insert(parent = '',index = 'end',text = '',values = subject)
        
        sep1 = ttk.Separator(self.frames.subjectFrame).grid(row = 1,column = 1)

        table = ttk.Treeview(self.frames.subjectFrame,columns = ('Title','Topic','Description','URL','Subject'),yscrollcommand = yscroll2.set(0,0),xscrollcommand = xscroll1.set(0,0))
        table.grid(row=1,column = 1,columnspan = 5)

        table.column("#0", width=0)
        table.column("Title",anchor=CENTER, width=150,stretch=True)
        table.column("Topic",anchor=CENTER,width=150,stretch=True)
        table.column("Description",anchor=CENTER,width=150,stretch=True)
        table.column("URL",anchor=CENTER,width=150,stretch=True)
        table.column("Subject",anchor=CENTER,width = 150,stretch=True)

        table.heading("#0",text="",anchor=CENTER)
        table.heading("Title",text="Title",anchor=CENTER)
        table.heading("Topic",text="Topic",anchor=CENTER)
        table.heading("Description",text="Description",anchor=CENTER)
        table.heading("URL",text="Location",anchor=CENTER)
        table.heading("Subject",text = "Subject",anchor = CENTER)
        connectToDBMS()
        resources = getResources()
        for r in resources:
            table.insert(parent='',index='end',text='',values=(r[0],r[1],r[2],r[3],r[4]))
        title_entry = tk.StringVar()
        title = ttk.Entry(self.frames.subjectFrame,textvariable = title_entry)
        title.grid(row =2,column = 1)

        topic_entry = tk.StringVar()
        topic = ttk.Entry(self.frames.subjectFrame,textvariable = topic_entry)
        topic.grid(row=2,column = 2)

        description_entry = tk.StringVar()
        description = ttk.Entry(self.frames.subjectFrame,textvariable = description_entry)
        description.grid(row = 2,column = 3)

        location_entry = tk.StringVar()
        location = ttk.Entry(self.frames.subjectFrame,textvariable = location_entry)
        location.grid(row = 2,column = 4)
        
        subject_entry = tk.StringVar()
        subject = ttk.Entry(self.frames.subjectFrame,textvariable = subject_entry)
        subject.grid(row = 2,column = 5)

        add_entry = partial(self.subUtil.entry_addition,[title_entry,topic_entry,description_entry,location_entry,subject_entry,table,sidemenu])
        addentrybutton = ttk.Button(self.frames.subjectFrame,text="Add Entry",command = add_entry)
        addentrybutton.grid(row=2,column = 0)
        
        ttk.Label(self.frames.subjectFrame,text="To modify or Delete, Enter Title").grid(row = 3,column = 0,columnspan = 3)
        Modify_entry = tk.StringVar()
        Modify = ttk.Entry(self.frames.subjectFrame,textvariable = Modify_entry)
        Modify.grid(row = 3,column = 3)

        tk.Button(self.frames.subjectFrame,text="Delete",command = "").grid(row=3,column = 4)
        tk.Button(self.frames.subjectFrame,text="Modify",command = "").grid(row=3,column = 5)