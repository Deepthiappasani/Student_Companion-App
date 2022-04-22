from dbmsfunctions import connectToDBMS, newActivity
from libraries import *

class activitiesUtils:
    def __init__(self,activitiesFrame):
        self.activitiesFrame = activitiesFrame

    def activity_addition(self,l_entry):
        activity_ID = l_entry[0].get()
        activity_Title = l_entry[1].get()
        activity_DATE = l_entry[2].get()
        activity_ST = l_entry[3].get()
        activity_ET = l_entry[4].get()
        activity_Des = l_entry[5].get()
        table = l_entry[6]
        connectToDBMS()
        newActivity(activity_ID,activity_Title,activity_DATE,activity_ST,activity_ET,activity_Des)
        table.insert(parent='',index='end',text='',values=(activity_ID, activity_Title, activity_DATE,activity_ST, activity_ET,activity_Des))
'''        with open ("Activities.txt",'a',newline="") as ActivityFile:
                writer = csv.writer(ActivityFile)
                writeList = [activity_ID, activity_Title, activity_ST, activity_ET,activity_Des]
                writer.writerow(writeList)
                ActivityFile.close()'''
                