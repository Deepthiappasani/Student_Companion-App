from pandas import array
import psycopg2
def connectToDBMS():
    '''Function to establish a connection to the postgresql database'''
    global conn
    conn = psycopg2.connect(database="postgres", user='postgres', password='rani', host='127.0.0.1', port= '5432')
    conn.autocommit = True
    global cursor
    cursor = conn.cursor()

def insertdata(tablename,columns,values):
    '''Function to insert data into the database'''
    cursor.execute("INSERT INTO "+tablename+"("+columns+") VALUES ("+values+")")
def deletedata(tablename,condition):
    '''Function to delete data from the database'''
    cursor.execute("DELETE FROM "+tablename+" WHERE "+condition)
def selectdata(tablename,columns,condition):
    '''Function to retrieve data from the database'''
    cursor.execute("SELECT "+columns +" FROM "+tablename+" WHERE "+condition)
    result = cursor.fetchall()
    return result
def arrTostr(arr):
    s = "','".join(arr)
    s = "'" + s + "'"
    return s
def getEventbyDate(date):
    '''Function to get Events scheduled on a date'''
    selectdata(tablename="EventDetails",columns = "EventTitle, EventDescription",condition = "EventDate = '"+date+"'")

def getActivity():
    connectToDBMS()
    cursor.execute('SELECT ActivityID,ActivityTitle,DateofCompletion,StartTime,EndTime,ActivityDescription from ActivityDetails;')
    activities = cursor.fetchall()
    return activities

def getActivitybyDate(date):
    '''Function to get activities to be completed'''
    selectdata(tablename="ActivityDetails",columns = "ActivityTitle, ActivityDescription, EndTime",condition = "DateOfCompletion = '"+date+"'")
def newEvent(date,time):
    '''Function to enter the details of a new event into the database'''
    #print ("Event Date:\nEnter in 'YYYY-MM-DD' format")
    insertdata(tablename="EventDetails",columns="EventDate,EventTime",values = arrTostr([date,time]))
def getEvents():
    cursor.execute('SELECT EventDate,EventTime from EventDetails;')
    events = cursor.fetchall()
    return events
def newActivity(id,title,date,starttime,endtime,desc):
    '''Function to enter the details of a new activity into the database'''
    insertdata(tablename="ActivityDetails",columns="ActivityID,ActivityTitle,DateOfCompletion,StartTime,EndTime,ActivityDescription",values = arrTostr([id,title,date,starttime,endtime,desc]))

def deleteActivity(id):
    print("ID = ",id.get())
    query = "DELETE FROM ActivityDetails where ActivityID = "+ id.get() +";"
    cursor.execute(query)
def updateActivity(id,title,date,starttime,endtime,desc):
    deleteActivity(id)
    newActivity(id.get(),title.get(),date.get(),starttime.get(),endtime.get(),desc.get())
def markActivityAsCompleted(title,date):
    '''Function to delete an completed activity from the database'''
    deletedata(tablename="ActivityDetails",condition="ActivityTitle = '"+title+"' AND DateOfCompletion = '"+date+"'")
def markEventAsCompleted(title,date):
    '''Function to delete an event when it is completed'''
    deletedata(tablename="EventDetails",condition="EventTitle = '"+title+"' AND EventDate = '"+date+"'")
def AddSubject(subject):
    '''Function to add a new subject'''
    insertdata(tablename='Subject',columns = 'SubjectName',values="'"+subject+"'")
def getSubjects():
    '''Get the list of all the subjects'''
    cursor.execute("SELECT Subject FROM Subject_Topic")
    result = cursor.fetchall()
    result = set(result)
    result = list(result)
    return result
def getTopics():
    cursor.execute("SELECT Topic from Subject_Topic")
    result = cursor.fetchall()
    result = list(set(result))
    return result
def insertResources(topic,title,description,url,subject):
    '''Function tot insert the details of a new learning resource'''
    if topic not in getTopics():
        cursor.execute("insert into Subject_Topic(Subject,Topic) values('" + subject +"','" + topic + "');")
    cursor.execute("insert into LearningResourceDetails(Title,Topic,Description) values ('"+ title + "','" + topic + "','" + description + "') RETURNING ID;")
    id = cursor.fetchone()
    print(id)
    cursor.execute("insert into LearningResourceURL(URL,LearningResourceID) values('" + url + "'," + str(id[0]) + ");")
def newUser(name,username,password):
    '''Function to save the details of new user'''
    insertdata(tablename='UserDetails',columns = 'Name,Username,password',values = "'" + name + "','" + username + "','" + password + "'")
def getResources():
    cursor.execute("select LearningResourceDetails.title,LearningResourceDetails.Topic,Description,URL,Subject_Topic.Subject from ((LearningResourceDetails inner join Subject_Topic on LearningResourceDetails.Topic = Subject_Topic.Topic) inner join LearningResourceURL on LearningResourceURL.LearningResourceID = LearningResourceDetails.ID);")
    resources = cursor.fetchall()
    return resources

def getLearningResources(subject):
    cursor.execute("select LearningResourceDetails.title,LearningResourceDetails.Topic,Description,URL from ((LearningResourceDetails inner join Subject_Topic on LearningResourceDetails.Topic = Subject_Topic.Topic) inner join LearningResourceURL on LearningResourceURL.LearningResourceID = LearningResourceDetails.ID) where Subject_Topic.Subject = '" + subject + "';")
    resources  = cursor.fetchall()
    print(resources)
    return resources
def verifyUser(username,password):
    '''Function to check if user is a valid one and if the password is correct'''
    cursor.execute("SELECT password from UserDetails where Username = '"+username + "'")
    result = cursor.fetchone()
    if result[0] == password:
        return True
    return False
