# cas
#College Allotment system

from tkinter import *

global rank
global board
global score
global roll
global allot
score=[]
board=[]
roll=[]
allot=[]
def sorty():
    fii=open("Student Details.txt","r")
    d=fii.readlines()
    for i in d:
        pr=i.split()
        score.append(pr[3])
        board.append(pr[4])
        roll.append(pr[2])
    fii.close()

    for i in range(1,len(score),1):
        j=i-1
        while j>=0 and score[j]<=score[j+1]:
            if score[j]==score[i]:
                if board[j]<=board[i]:
                    roll[j+1]=roll[j]
            else:
                roll[j+1]=roll[j]
            j=j-1
        roll[j+1]=roll[i]

    choicelist=[]
    fil=open("choice.txt","r")
    dr=fil.readlines()
    for i in dr:
        pre=i.split()
        choicelist.append(pre)
    
    choicedict={}
    flag=0
    for i in roll:
        for j in choicelist: 
            if i==j[0]:
                for k in range(1,len(j),1):
                  if flag==0:
                    if choicedict.get(j[k],0)==0:
                        choicedict[j[k]]=1
                        allot.append(j[k])
                        flag=1
                    else:
                        if choicedict[j[k]]!=2:
                            choicedict[j[k]]+=1
                            allot.append(j[k])
                            flag=1
                            
        if flag==0:
          allot.append("Not Alloted")


def sub():
    sorty()
    global res
    res = Tk() 
    res.title('Result and edit')
    res.config(bg="linen")
    res.geometry("1200x1600")
    Label(res,text=user.get(),font=("Arial",30),bg="linen",fg="red").place(x=100,y=100)
    j=0
    for i in roll:
        if i!=user.get():
            j+=1
        else:
            break
    Label(res,text=allot[j],font=("Arial",30),bg="linen",fg="red").place(x=400,y=100)
       
    
def add():
       if s.get()!="Select Choice":
           if s.get() not in li:
               if len(li)==5:
                    Label(choice,text="Choices can't be more than 5",font=("Arial",10),bg="linen",fg="red").place(x=400,y=440)
               else:    
                li.append(s.get())
                lb.insert(END,s.get())
                Label(choice,text="\t\t\t\t\t",font=("Arial",10),bg="linen",fg="red").place(x=400,y=440)

           else:
                Label(choice,text="Choices can't be same\t\t\t",font=("Arial",10),bg="linen",fg="red").place(x=400,y=440)

def remove():
    ti=list(lb.curselection())
    li.remove(li[ti[0]])
    lb.delete(ti[0])
    Label(choice,text="\t\t\t\t\t",font=("Arial",10),bg="linen",fg="red").place(x=400,y=440)
def discho():
    choice.destroy()
    loginn()
def submit():
    fil=open("choice.txt","a+")
    fil.write(user.get()+"\t")
    for i in li:
        fil.write(i+"\t")
    fil.write("\n")
    fil.close()
    Label(choice,text="Choices Submitted Succesfully",font=("Arial",10),bg="linen",fg="green").place(x=450,y=540)
    button=Button(choice,text="Log out",font=("Arial",10),fg="white",bg="red",command=discho,activebackground="blue").place(x=450,y=600)

global li
li=[]
def chhoice():
 r.destroy()
 global choice
 choice=Tk()
 choice.configure(background="linen")
 choice.geometry("1600x1200")
 choice.title("CHOICE")
 global s
 s=StringVar()
 s.set("Select Choice")
 Label(choice,text="SELECT YOUR CHOICES",font=("Times New Roman",20),bg="linen",fg="red").place(x=400,y=15)
 ch=["IITBombay(Cs)","IITBombay(IT)","IITDelhi(Cs)","IITDelhi(IT)","IITKanpur(Cs)","IITKanpur(IT)","IITKhadagpur(Cs)","IITKhadagpur(IT)","IITRoorkee(Cs)","IITRoorkee(IT)"]
 OptionMenu(choice,s,*ch).place(x=300,y=100)
 global lb
 lb=Listbox(choice,height=15,width=40,highlightcolor="blue",bd=5,selectmode=BROWSE)
 lb.place(x=500,y=100) 

 button=Button(choice,text="Add",font=("Arial",10),fg="white",bg="red",command=add,activebackground="blue").place(x=400,y=400)
 button=Button(choice,text="Remove",font=("Arial",10),fg="white",bg="red",command=remove,activebackground="blue").place(x=500,y=400)
 button=Button(choice,text="Submit",font=("Arial",10),fg="white",bg="red",command=submit,activebackground="blue").place(x=450,y=500)


def result():
 global r
 r = Tk() 
 r.title('Result and edit')
 r.geometry("1200x1600")
 r.config(bg="linen")
 button1 = Button(r, text='Show Result', width=25, activebackground= "red",command=sub) 
 button1.place(x=300, y=300)
 button2 = Button(r, text='Edit your choices', width=25, activebackground= "red",command=chhoice) 
 button2.place(x=700, y=300)

 r.mainloop() 
def destl():
    student.destroy()
    loginn()
def fileh():
    fo=open("Student Details.txt", "a+")
    fo.seek(0, 0)
    s= fo.read()
    l= s.split()
    flag=1
    for i in range(2, len(l), 6):
        if stu_rollno.get()==l[i]:
            Label(student, text="This user already exist", fg="red", font=('Comic Sens MS', 12)).place(x=500, y=530)
            flag=0

        elif flag==1:
            Label(student, text="                                        ", fg="red", font=('Comic Sens MS', 12), bg= "linen").place(x=500, y=530)

    if stu_name.get().isalpha():
        l1=Label(student, text="                                                       ", font=("Comic Sens MS", 10), fg="red", bg="linen")
        l1.place(x=810,y=140)
        flag=1
        
    elif not stu_name.get().isalpha():
        l1=Label(student, text="Only alphabets are allowed", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=140)
        flag=0
        
    if stu_age.get().isdigit():
        l1=Label(student, text="                                                       ", font=("Comic Sens MS", 10), fg="red", bg="linen")
        l1.place(x=810,y=180)
        flag=1
        

    elif stu_age.get()=='':
        l1=Label(student, text="Mandatory field", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=180)
        flag=0
        
    elif not stu_age.get().isdigit() and flag==1:
        l1=Label(student, text="Only numerals are allowed", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=180)
        
    if stu_rollno.get().isdigit():
        l1=Label(student, text="                                                       ", font=("Comic Sens MS", 10), fg="red", bg="linen")
        l1.place(x=810,y=290)
        flag=1
        
        
    elif stu_rollno.get()=='':
        l1=Label(student, text="Mandatory field", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=290)
        flag=0

    elif not stu_rollno.get().isdigit() and flag==1:
        l1=Label(student, text="Only numerals are allowed", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=290)
        
    if stu_score.get().isdigit():
        l1=Label(student, text="                                                       ", font=("Comic Sens MS", 10), fg="red", bg="linen")
        l1.place(x=810,y=330)
        flag=1
        
        
    elif stu_score.get()=='':
        l1=Label(student, text="Mandatory field", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=330)
        flag=0

    elif not stu_score.get().isdigit() and flag==1:
        l1=Label(student, text="Only numerals are allowed", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810, y=330)
        
    if stu_percent.get().isdigit():
        l1=Label(student, text="                                                       ", font=("Comic Sens MS", 10), fg="red", bg="linen")
        l1.place(x=810,y=370)
        flag=1
        
        
    elif stu_percent.get()=='':
        l1=Label(student, text="Mandatory field", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=370)
        flag=0

    elif not stu_percent.get().isdigit() and flag==1:
        l1=Label(student, text="Only numerals are allowed", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=410)
        
    if not stu_password.get()=='':
        l1=Label(student, text="                                                       ", font=("Comic Sens MS", 10), fg="red", bg="linen")
        l1.place(x=810,y=410)

    elif stu_password.get()=='':
        l1=Label(student, text="Mandatory field", font=("Comic Sens MS", 10), fg="red")
        l1.place(x=810,y=410)
            
    if(flag==1):
        fo.seek(0, 2)
        fo.write(stu_name.get()+"\t")
        fo.write(stu_age.get()+"\t")
        fo.write(stu_gender.get()+"\t")
        fo.write(stu_rollno.get()+"\t")
        fo.write(stu_score.get()+"\t")
        fo.write(stu_percent.get()+"\t")
        fo.write(stu_password.get()+"\n")
        destl()

def apply():
 login.destroy()
 global stu_name
 global stu_age
 global stu_gender
 global stu_percent
 global stu_score
 global stu_rollno
 global stu_password
 global student
 student= Tk()
 student.config(bg="linen")
 student.geometry("1200x800")
 student.title("Student details")
 Label(student, text= "Student details ", font=("Times new roman", 30), fg="red", bg="linen").place(x=350 ,y=60)

 stu_password= StringVar()
 stu_name= StringVar()
 stu_age= StringVar()
 stu_gender= StringVar()
 stu_score= StringVar()
 stu_rollno= StringVar()
 stu_percent= StringVar()

 Label(student, text="Student Name: ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=120)
 Entry(student, textvariable=stu_name , font=('Comic Sens MS', 20)).place(x=500,y=130)

 Label(student, text="Age:   ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=160)
 Entry(student, textvariable=stu_age, font=('Comic Sens MS', 20)).place(x=500,y=170)
 
 Label(student, text="Gender:   ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=200)
 Checkbutton(student, text="Male ", font=('Comic Sens MS', 12), bg="linen").place(x=500,y=210)
 Checkbutton(student, text="Female ", font=('Comic Sens MS', 12), bg="linen").place(x=500,y=240)
 
 Label(student, text="Roll number:   ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=270)
 Entry(student, textvariable=stu_rollno, font=('Comic Sens MS', 20)).place(x=500,y=280)

 Label(student, text="Qualifying Exam Score:   ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=310)
 Entry(student, textvariable=stu_score, font=('Comic Sens MS', 20)).place(x=500,y=320)

 Label(student, text="Board Percentage:   ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=350)
 Entry(student, text="", textvariable=stu_percent, font=('Comic Sens MS', 20)).place(x=500,y=360)

 Label(student, text="Create Password:   ", font=('Comic Sens MS', 20), bg="linen").place(x=100,y=390)
 Entry(student, text="", textvariable=stu_password, font=('Comic Sens MS', 20), show="*").place(x=500,y=400)

 Button(student, text="Proceed", font=('Comic Sens MS', 20), activebackground="Red", bg="linen", command=fileh).place(x=500,y=480)


def cllglist():
 global student
 student= Tk()
 student.config(bg="linen")
 student.geometry("1200x800")
 student.title("College Rank details")
 Label(student, text= "College Ranks: ", font=("Times new roman", 24), fg="red", bg="linen").place(x=350,y=60)

 Label(student, text="Rank: ", font=('Comic Sens MS', 10), bg="linen").place(x=100, y=120)
 Label(student, text="Info: ", font=('Comic Sens MS', 10), bg="linen").place(x=300, y=120)
 Label(student, text="Total Seats: ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=120)
 Label(student, text="1. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=140)
 Label(student, text="CS, IIT Bombay ", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=140)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=140)
 Label(student, text="2. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=160)
 Label(student, text="CS, IIT Delhi ", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=160)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=160)
 Label(student, text="3. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=180)
 Label(student, text="IT, IIT Bombay ", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=180)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=180)
 Label(student, text="4. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=200)
 Label(student, text="CS, IIT Kanpur", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=200)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=200)
 Label(student, text="5. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=220)
 Label(student, text="IT, IIT Delhi", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=220)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=220)
 Label(student, text="6. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=240)
 Label(student, text="CS, IIT Khadakpur", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=240)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=240)
 Label(student, text="7. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=260)
 Label(student, text="CS, IIT Roorkee", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=260)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=260)
 Label(student, text="8. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=280)
 Label(student, text="IT, IIT Kanpur", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=280)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=280)
 Label(student, text="9. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=300)
 Label(student, text="IT, IIT Khadakpur", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=300)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=300)
 Label(student, text="10. ", font=('Comic Sens MS', 10), bg="linen").place(x=100,y=320)
 Label(student, text="IT, IIT Roorkee", font=('Comic Sens MS', 10), bg="linen").place(x=300,y=320)
 Label(student, text="2 ", font=('Comic Sens MS', 10), bg="linen").place(x=500, y=320)

def relo():
    login.destroy()
    result()
def log():
   file=open("Student Details.txt","r+")
   d=file.readlines()
   file.seek(0)
   flag=0
   for i in d:
       p=i.split()
       if p[2]==user.get() and p[5]==pas.get():
           print(11)
           flag=1
           break
   file.close()
   if flag==0:
       Label(login,text="Invalid Roll no. or Password",font=("Arial",7),fg="Red",bg="black").place(x=1100,y=150)
   else:
       relo()
       


def loginn():
 global login
 global user
 global pas
 login=Tk()
 login.configure(background="black")
 login.geometry('1600x1200')
 login.title("LOG IN")
 user=StringVar()
 pas=StringVar() 
 Label(login,text="JOINT COUNSELLING AUTHORITY",font=("Times New Roman",30),fg="light yellow",bg="black").place(x=300,y=15)
 Label(login,text="Roll No.",font=("Arial",10),fg="white",bg="black").place(x=1000,y=100)
 Label(login,text="Password",font=("Arial",10),fg="white",bg="black").place(x=1000,y=130)
 Entry(login,textvariable=user,font=("Arial",10),bg="white").place(x=1100,y=100)
 Entry(login,show="*",textvariable=pas,font=("Arial",10),bg="white").place(x=1100,y=130)

 button=Button(login,text="Log in",font=("Arial",10),fg="white",bg="blue",command=log,activebackground="Red").place(x=1200,y=180)
 Label(login,text="or",font=("Arial",10),fg="white",bg="black").place(x=1220,y=210)
 button=Button(login,text="Apply Now",font=("Arial",10),fg="white",bg="blue",command=apply,activebackground="Red").place(x=1180,y=240)
 Label(login,text="For list of Colleges",font=("Comic Sans MS",15),fg="white",bg="black").place(x=1000,y=350)
 button=Button(login,text="Click Here",font=("Arial",10),fg="white",bg="blue",command=cllglist,activebackground="Red").place(x=1190,y=355)

 img=PhotoImage(file="coll.ppm")
 ll=Label(login,image=img,width=950,bg="white")
 ll.image=img
 ll.place(x=10,y=80)

loginn()
