from dbmsfunctions import getSubjects, insertResources
from libraries import *

class subjectUtils:

    def __init__(self,subjectFrame):
        self.subjectFrame = subjectFrame

    def entry_addition(self,l_entry):
        title = l_entry[0].get()
        topic = l_entry[1].get()
        description = l_entry[2].get()
        location = l_entry[3].get()
        subject = l_entry[4].get()
        table = l_entry[5]
        sidemenu = l_entry[6]
        
        insertResources(title,topic,description,location,subject)
        table.insert(parent='',index='end',text='',values=(title,topic,description,location,subject))
        
        for item in sidemenu.get_children():
            sidemenu.delete(item)
        subjects = getSubjects()
        for subject in subjects:
            sidemenu.insert(parent='',index='end',text='',values=(subject))
        for i in range(5):
            l_entry[i].set("")