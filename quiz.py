import tkinter as tk
from tkinter import *
import tkinter.font as font
import random
import sqlite3   #for datastorage
import time      #interval of time for question
import re        #regular expression for password validation
from tkinter import messagebox

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#45818e")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="#45818e")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Login",fg="#FFA500",bg="#45818e")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.4,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username :",fg='white',bg='#45818e')
    ulabel.place(relx=0.20,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password :",fg='white',bg='#45818e')
    plabel.place(relx=0.20,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="#413e65")
    log.configure(width = 15,height=1, activebackground = "#45818e", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Quiz App')
    
    fname = StringVar() 
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#45818e")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#45818e")  #13e65
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="SignUp",fg="#FFA500",bg="#45818e") #BADA55
    heading.config(font=('calibri 40'))
    heading.place(relx=0.40,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name :",fg='black', bg='#45818e')
    flabel.place(relx=0.19,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username :",fg='black', bg='#45818e')
    ulabel.place(relx=0.19,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password  :",fg='black', bg='#45818e')
    plabel.place(relx=0.19,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*") #show "*" hides the password
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country  :",fg='black', bg='#45818e')
    clabel.place(relx=0.20,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)

    
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country =  c.get()
        special_symbols =['$', '@', '#', '%']
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            #error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            #error.place(relx=0.37,rely=0.7)
            messagebox.showerror('Form validation','Please Enter all the fields')
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            messagebox.showerror('Form validation','Please Enter all the fields')
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            messagebox.showerror('Form validation','username and password cant be empty')

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            messagebox.showerror('Form validation','username cant be empty')
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
           messagebox.showerror('Password validation','Password cant be empty') 
        
        elif len(pas.get()) < 8:
            messagebox.showerror('Password validation','Password must have atleast 8 charachters') 

        elif re.search('[0-9]',password) is None:
            messagebox.showerror('Password validation','No digits in password') 

        elif re.search('[A-Z]',password) is None: 
            messagebox.showerror('Password validation','No uppercase in password')
        elif not any(characters in special_symbols for characters in password): 
            messagebox.showerror('Password validation','Password should have at least one of the symbols $@#%')
        
        else:
        
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor() #instance using which you can invoke methods that execute SQLite statements, fetch data from the result sets of the queries.
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute('SELECT * FROM userSignUp')
            omm=create.fetchall()
            for a,un,pd,d in omm:
                if un == uname.get():
                    messagebox.showerror('Form validation','Username already exists, pls enter another username') 
                    break
            else:
                create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
                conn.commit()
                create.execute('SELECT * FROM userSignUp')
                z=create.fetchall()
                print(z)
                #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
                conn.close()
                loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="#413e65",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#45818e", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#45818e", fg="black")
    log.configure(width = 16,height=1, activebackground = "#45818e", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Quiz App Menu')
    
    
    menu_canvas = Canvas(menu,width=720,height=403)
    img = PhotoImage(file="images\questbg.png")
    menu_canvas.create_image(0,0,image=img,anchor=NW)
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#45818e")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#45818e") 
    wel.config(font=('Broadway 21'))
    wel.place(relx=0.1,rely=0.2)
    
    abcdefgh='Welcome '+ abcdefgh
    level34 = Label(menu_frame,text=abcdefgh,bg="#45818e",font="calibri 18",fg="orange")
    level34.place(relx=0.17,rely=0.25)
    
    level = Label(menu_frame,text='Select your Difficulty Level !!',bg="#45818e",font="calibri 18")
    level.place(relx=0.25,rely=0.4)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Easy',bg="#45818e",font="calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.5)
    
    mediumR = Radiobutton(menu_frame,text='Medium',bg="#45818e",font="calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.6)
    
    hardR = Radiobutton(menu_frame,text='Hard',bg="#45818e",font="calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.7)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="#413e65",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.82)
    menu.mainloop()



def easy():
    
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')
    
    easy_canvas = Canvas(e,width=720,height=403)
    img = PhotoImage(file="images\questbg.png")
    easy_canvas.create_image(0,0,image=img,anchor=NW)
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="#45818e")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQ = [
                 [
                     "What will be the output of the following code snippet?" 
                     "1.) print(type(5 / 2))",
                     "float",
                     "int",
                     "char",
                     "double" 
                 ] ,
                 [
                     "Which of the following concepts is not a part of Python?" ,
                    "Dynamic typing",
                    "Loops",
                    "Pointer",
                    "All of the above"
                     
                 ],
                [
                    "How is a code block indicated in a Python" ,
                    "Brackets",
                    "Indentation",
                    "Key",
                    "None of the above"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ]
            ]
    answer = [
                "float",
                "Pointer",
                "Indentation",
                "Class",
                "^"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="#45818e")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="#45818e")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="#45818e")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="#45818e")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="#45818e")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit", bg="#413e65",fg="white")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next", bg="#413e65",fg="white")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    m.title('Quiz App - Medium Level')
    
    med_canvas = Canvas(m,width=720,height=403)
    img = PhotoImage(file="images\questbg.png")
    med_canvas.create_image(0,0,image=img,anchor=NW)
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="#45818e")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQ = [
                [
                    "Which of the following is not an exception handling keyword in Python?",
                     "accept",
                     "finally",
                     "except",
                     "try"
                ],
                [
                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
                    "3",
                    "5",
                    "25",
                    "1"
                ],
                [
                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
                    "Error",
                    "None",
                    "25",
                    "2"
                ],
                [
                    "print(0xA + 0xB + 0xC):",
                    "0xA0xB0xC",
                    "Error",
                    "0x22",
                    "33"
                ],
                [
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ], 
            ]
    answer = [
            "accept",
            "1",
            "25",
            "33",
            "none of the mentioned"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="#45818e")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="#45818e")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="#45818e")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="#45818e")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="#45818e")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit", fg="white", bg="#413e65")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next", fg="white", bg="#413e65")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    #count=0
    h = Tk()
    h.title('Quiz App - Hard Level')
    
    hard_canvas = Canvas(h,width=720,height=403)
    img = PhotoImage(file="images\questbg.png")
    hard_canvas.create_image(0,0,image=img,anchor=NW)
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="#45818e")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    hardQ = [
                [
       "All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],
    [
        "Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],
    [
        "How can assertions be disabled in Python ?",
        "Passing -O when running python",
        "Assertions are disabled by default",
        "Both 1 and 2 are wrong",
        "Asserations cannot be disabled in python",
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ] 
            
]
    answer = [
            "None of the mentioned",
            "in",
            "Passing -O when running python",
            "4",
            "error"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="#45818e")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="#45818e")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="#45818e")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="#45818e")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="#45818e")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        #count=count+1
        if (var.get() in answer):
            score+=1
        display()
    
   # def lastPage():
    #    h.destroy()
     #   showMark()
    
    submit = Button(hard_frame,command=calc,text="Submit", fg="white", bg="#413e65")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next", fg="white", bg="#413e65")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
   # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    sh = Tk()
    sh.title('Your Marks')
    
    st = "Your score is "+str(mark)+"/5"
    mlabel = Label(sh,text=st,fg="black", bg="white")
    mlabel.pack()
    
    def callsignUpPage():
        sh.destroy()
        start()
    
    def myeasy():
        sh.destroy()
        easy()
    
    b24=Button(text="Re-attempt", command=myeasy, bg="black", fg="white")
    b24.pack()
    
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained','Failed'
    sizes = [int(mark),5-int(mark)]
    explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    b23=Button(text="Sign Out",command=callsignUpPage,fg="white", bg="black")
    b23.pack()
    
    sh.mainloop()

def start():
    global root  #create it as global as we have to use it in another functions
    root = Tk()  #initializing the tk
    root.title('Welcome To Quiz App')
    canvas = Canvas(root,width = 590,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="images\home3.png")
    canvas.create_image(0,0,image=img,anchor=NW) #nw means north west i.e starting from left top corner

    button = Button(root, text='Start',command = signUpPage,bg="#413e65",fg="white") 
    button.configure(width = 65,height=1, activebackground = "#45818e", relief = RAISED,font= ('bold')) #flat, rased, sunken
    button.grid(column = 0 , row = 2)
    
    root.mainloop() #responsible for executing the script and displaying the output window. 
    
    
if __name__=='__main__':
    start()
