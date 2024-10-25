from tkinter import *
from tkinter import ttk

"""
ADD
DELETE
UPDATE
"""

highscore = 0.0             
lowscore = 100.0            
students = []              
studentnames = []           
f1 = []


mainwindow = Tk()
mainwindow.title("Student Manager 2.0")
mainwindow.geometry("700x700")
mainwindow.resizable(0,0)
mainwindow.config(bg = "#141211")

# Initializing Variables
options = ['Ascending', 'Descending']

def deleteItems():
    for item in mainwindow.winfo_children():
        item.destroy()


def openFile():             
    
    students.clear()       
    studentnames.clear()   

    with open("studentMarks.txt") as f1:
        data = f1.readlines()[1:]
    
        for line in data:
            studentdata = { 
                           "Name" : "",
                           "ID" : "",
                           "CourseTotal" : "",          
                           "ExamMark" : "",            
                           "PercentTotal" : "",        
                           "Grade" : "",
                           }
        
            j = line.split(",")            
            
            studentdata["Name"] = j[1]
            studentdata["ID"] = j[0]
            studentdata["CourseTotal"] = str(int(j[2]) + int(j[3]) + int(j[4]))
            studentdata["ExamMark"] = j[5]
            
            percenttotal = ((int(studentdata["CourseTotal"]) + int(j[5])) / 160)*100
            
            studentdata["PercentTotal"] = round(percenttotal, ndigits=1) 
            studentdata["Grade"] = gradeSystem(percenttotal)
    
            students.append(studentdata)   


def getValues():                
    
    global highscore, lowscore                     
    
    for studentdata in students:                   
        studentnames.append(studentdata["Name"])   

        if float(studentdata["PercentTotal"]) > highscore:     
            highscore = studentdata["PercentTotal"]            
                                                              
        if float(studentdata["PercentTotal"]) < lowscore:   
            lowscore = studentdata["PercentTotal"]
    
    
def gradeSystem(percentages):       
    
    if percentages >= 70:
        grade = "A"
    
    elif percentages >= 60 and percentages <= 69:
        grade = "B"
    
    elif percentages >= 50 and percentages <= 59:
        grade = "C"
    
    elif percentages >= 40 and percentages <= 49:
        grade = "D"
    
    else:
        grade = "F"
        
    return grade


def allRecords(txtarea):           
    
    txtarea.delete("1.0", "end")   
    count = 0                      
    totalpercentages = 0           
    
    for i in students:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")
            count += 1
            totalpercentages += i["PercentTotal"]
    
    txtarea.insert(END, f"Number of students in class: {count} \n")
    txtarea.insert(END, f"Average percentage of marks: {round((totalpercentages/count), ndigits = 1)}% \n")
    

def oneRecord(txtarea, names):      
    
    txtarea.delete("1.0", "end")
    
    userpick = names.get()          
                                    
    for i in range(len(students)):
        if students[i]["Name"] == userpick:
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)

def highestScore(txtarea):        
    
    txtarea.delete("1.0", "end")
    
    for i in range(len(students)):
        if students[i]["PercentTotal"] == highscore: 
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)

def deleteRecord(names):
    
    userpick = names.get()
    
    for i in range(len(students)):
        if students[i]["Name"] == userpick:
            getid = students[i]["ID"]
            
    count = 0
    
    with open("studentMarks.txt", "r") as f:
        data = f.readlines()
        
    with open("studentMarks.txt", "w") as f:
        for i in data:
            try: 
                if count != getid:
                    f.write(i)
                count += 1
            except:
                f.write(i)
    f.close()
    mainMenu()

"""
    userpick = names.get()
    count = 0
    
    for i in range(len(students)):
        if students[i]["Name"] == userpick:
            linetodel = students[i]["ID"]
    
        
        for i in data:
            j = line.split(",")     
            
            if linetodel ==
"""
    
 

def lowestScore(txtarea):          
    
    txtarea.delete("1.0", "end")
    
    for i in range(len(students)):
        if students[i]["PercentTotal"] == lowscore:
            printLayout(students[i]["Name"], students[i]["ID"], 
                        students[i]["CourseTotal"], students[i]["ExamMark"], 
                        students[i]["PercentTotal"], students[i]["Grade"], txtarea)
         

def sortData(txtarea, options):
    
    txtarea.delete("1.0", "end")
    
    sortoption = options.get() 
    
    if sortoption == "Ascending":
        alist = sorted(students, key = lambda x: x["Name"])
        
        for i in alist:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")
            
        
    elif sortoption == "Descending":
        dlist = sorted(students, key = lambda x: x["Name"], reverse = True)
        
        for i in dlist:
            printLayout(i["Name"], i["ID"], 
                        i["CourseTotal"], i["ExamMark"], 
                        i["PercentTotal"], i["Grade"], txtarea)
            txtarea.insert(END,"\n・ ・ ・ ・ ・\n")


def addStudent():
    deleteItems()
    
    name = StringVar()
    idnum = StringVar()
    mark1 = StringVar()
    mark2 = StringVar()
    mark3 = StringVar()
    exammark = StringVar()
    
    title2 = Label(mainwindow, text = "ADD STUDENT", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title2.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    label = Label(mainwindow, text = "Name:", font = "Corbel 13", bg = "#141211", fg = "white")
    label.place(relx = 0.25, rely = 0.25, anchor = W)
    prompt = Entry(mainwindow, textvariable = name, width = 20, font = "Corbel 13", bd=3)
    prompt.place(relx = 0.6, rely = 0.25, anchor = CENTER)

    label2 = Label(mainwindow, text = "ID:", font = "Corbel 13", bg = "#141211", fg = "white")
    label2.place(relx = 0.25, rely = 0.35, anchor = W)
    prompt2 = Entry(mainwindow, textvariable = idnum, width = 20, font = "Corbel 13", bd=3)
    prompt2.place(relx = 0.6, rely = 0.35, anchor = CENTER)
    
    label3 = Label(mainwindow, text = "Course Marks 1: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label3.place(relx = 0.25, rely = 0.45, anchor = W)
    prompt2 = Entry(mainwindow, textvariable = mark1, width = 20, font = "Corbel 13", bd=3)
    prompt2.place(relx = 0.6, rely = 0.45, anchor = CENTER)
    
    label4 = Label(mainwindow, text = "Course Marks 2: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label4.place(relx = 0.25, rely = 0.55, anchor = W)
    prompt4 = Entry(mainwindow, textvariable = mark2, width = 20, font = "Corbel 13", bd=3)
    prompt4.place(relx = 0.6, rely = 0.55, anchor = CENTER)
    
    label4 = Label(mainwindow, text = "Course Marks 3: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label4.place(relx = 0.25, rely = 0.65, anchor = W)
    prompt4 = Entry(mainwindow, textvariable = mark3, width = 20, font = "Corbel 13", bd=3)
    prompt4.place(relx = 0.6, rely = 0.65, anchor = CENTER)
    
    label4 = Label(mainwindow, text = "Exam Marks: ", font = "Corbel 13", bg = "#141211", fg = "white")
    label4.place(relx = 0.25, rely = 0.75, anchor = W)
    prompt4 = Entry(mainwindow, textvariable = exammark, width = 20, font = "Corbel 13", bd=3)
    prompt4.place(relx = 0.6, rely = 0.75, anchor = CENTER)
    
    submit = Button(mainwindow, text = "Submit", font = "Corbel 15", bg = "#dbc15a", bd = 0,
                    width = 15, command = lambda: addInfo(name,idnum,mark1,mark2,mark3,exammark))
    submit.place(relx = 0.35, rely = 0.875, anchor = CENTER)
    
    back = Button(mainwindow, text = "Back", font = "Corbel 15", bg = "#dbc15a", bd = 0,
                    width = 15, command = lambda: mainMenu())
    back.place(relx = 0.65, rely = 0.875, anchor = CENTER)
        

def addInfo(name,idnum,mark1,mark2,mark3,exammark):
    name = name.get()
    idnum = idnum.get()
    mark1 = mark1.get()
    mark2 = mark2.get()
    mark3 = mark3.get()
    exammark = exammark.get()
    
    name = stringCleanse(name)
    idnum = idCleanse(idnum)
    mark1 = courseMarkCleanse(mark1)
    mark2 = courseMarkCleanse(mark2)
    mark3 = courseMarkCleanse(mark3)
    exammark = examMarkCleanse(exammark)
    
    with open("studentMarks.txt", "a") as f1:
        f1.write(str(idnum) + "," + name + "," + str(mark1) + "," + str(mark2) + "," 
                 + str(mark3) + "," + str(exammark) + "\n")
        
    mainMenu()


def idCleanse(idnum):    
    check = True
    length = len(idnum)
    
    while check == False:

        if length > 4:
            idnum = idnum[:-1]
            length = len(idnum)
            length = "".join(c for c in idnum if length.isdigit())
            
        else:
            check = True
    
    
def stringCleanse(string):
    
    check = False
    length = len(string)

    while check == False:
    
        if length > 25:
            string = string[:-1]
            length = len(string)
            string = "".join(c for c in string if c.isalpha())
           
        else:
           check = True
           
    return string


def courseMarkCleanse(integer):
    
    integer = list(filter(lambda x: x.isdigit(), integer.split()))
    integer = sum([int(s) for s in integer])
    
    if integer >= 20:
        integer = 20
    
    elif integer <= 0:
        integer = 0
        
    return integer


def examMarkCleanse(integer):
    
    integer = list(filter(lambda x: x.isdigit(), integer.split()))
    integer = sum([int(s) for s in integer])
    
    if integer >= 100:
        integer = 100
    
    elif integer <= 0:
        integer = 0
        
    return integer


def printLayout(nameinstance,IDinstance,courseinstance,markinstance,percentinstance,gradeinstance,txtarea):
   
    txtarea.insert(END,"Name: " + nameinstance + "\n")
    txtarea.insert(END,"Number: " + IDinstance + "\n")
    txtarea.insert(END,"Coursework Total: " + courseinstance + "\n")
    txtarea.insert(END,"Exam Mark: " + markinstance)
    txtarea.insert(END,"Overall Percentage: " + str(percentinstance) + "% \n")
    txtarea.insert(END, "\nGrade: " + gradeinstance + "\n")


def mainMenu():
    
    deleteItems()
    
    openFile()
    getValues()
    
    names = StringVar()
    sorts2 = StringVar()
    
    title = Label(mainwindow, text = "STUDENT MANAGER", font = "Arial 32 bold", bg = "#141211", fg = "white")
    title.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
    b1 = Button(mainwindow, text = "View All Records", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: allRecords(txtarea))
    b1.place(relx = 0.25, rely = 0.2, anchor = CENTER)
    
    b2 = Button(mainwindow, text = "Show Highest Score", font = "Corbel 12", bg = "#dbc15a", width = 16, 
                bd = 0, command = lambda: highestScore(txtarea))
    b2.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    b3 = Button(mainwindow, text = "Show Lowest Score", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: lowestScore(txtarea))
    b3.place(relx = 0.75, rely = 0.2, anchor = CENTER)
    
    sen1 = Label(mainwindow, text = "Individual Student Records:", font = "Corbel 13", bg = "#141211", fg = "white")
    sen1.place(relx = 0.28, rely = 0.285, anchor = CENTER)
    
    records = ttk.Combobox(mainwindow, width = 25, textvariable = names)
    records['values'] = studentnames
    records.place(relx = 0.55, rely = 0.285, anchor = CENTER)
    
    b4 = Button(mainwindow, text = "View Record", font = "Corbel 12", bg = "#dbc15a", width = 12, 
                bd = 0, command = lambda: oneRecord(txtarea, names))
    b4.place(relx = 0.775, rely = 0.285, anchor = CENTER)
    
    txtarea = Text(mainwindow)
    txtarea.place(relx = 0.5, rely = 0.55, anchor = CENTER, height = 300, width = 500)
    
    scrollV = Scrollbar(mainwindow, orient = "vertical")
    scrollV.place(relx = 0.85, rely = 0.55, anchor = CENTER, height = 300)
    scrollV.config(command = txtarea.yview)
    txtarea.config(yscrollcommand = scrollV.set)

    sorts = ttk.Combobox(mainwindow, width = 25, textvariable = sorts2)
    sorts['values'] = options
    sorts.place(relx = 0.55, rely = 0.8, anchor = CENTER)
    
    b5 = Button(mainwindow, text = "Sort", font = "Corbel 12", bg = "#dbc15a", width = 12,
                bd = 0, command = lambda: sortData(txtarea, sorts))
    b5.place(relx = 0.775, rely = 0.8, anchor = CENTER)
    
    b6 = Button(mainwindow, text = "Add Student", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: addStudent())
    b6.place(relx = 0.25, rely = 0.885, anchor = CENTER)
    
    b7 = Button(mainwindow, text = "Delete Record", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: deleteRecord(names))
    b7.place(relx = 0.5, rely = 0.885, anchor = CENTER)
    
    b8 = Button(mainwindow, text = "Update Record", font = "Corbel 12", bg = "#dbc15a", width = 16,
                bd = 0, command = lambda: updateRecord())
    b8.place(relx = 0.75, rely = 0.885, anchor = CENTER)
    
mainMenu()

mainwindow.mainloop()

