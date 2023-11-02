import mysql.connector as sql
import random
import pickle
connection=sql.connect(host="localhost",user="root",passwd="password",database="school")
cursor=connection.cursor()

#_________________________________________________BASIC Functions___________________________________________________



#_1__________________________________________________________________________________________________________________
def fake_loading(delay):
    for i  in range(120*delay):
        for j in range(7):
            print(".",end="")
    
        for k in range(7):
            print("\b",end="")

#120 is creating a time delay of almost 1 seconds
#_2__________________________________________________________________________________________________________________
def generate():
    query="Select Num from random"
    cursor.execute(query)
    data =cursor.fetchall()
    
    bool=True
    while (bool==True):
       
        num=random.randint(100000,999999)
        bool=(num,) in data
    
        if bool==False:
            query = "INSERT INTO random values({})".format(num)
            cursor.execute(query)
            connection.commit()
            return num
            break

#_3__________________________________________________________________________________________________________________
def check_response(operation_response,operation_response_keys):
    bool=operation_response in operation_response_keys
    if bool==True:
        operation_response_keys[operation_response]()

    elif operation_response==0:
        home()
        
    else:
        while (bool==False):
            print("\nEnter the Correct Key Combinations \n")
            operation_response=int(input())
            bool=operation_response  in operation_response_keys
            
            if bool==True:
                operation_response_keys[operation_response]()

    return operation_response

#_4__________________________________________________________________________________________________________________
   
def write(file):
    
    f=open(file,"wb")
   
    while True:
        s=input()+"\n"
        if  s!="DONE\n":
            pickle.dump(s,f)
        else:
            break

    f.close()

#_5__________________________________________________________________________________________________________________
def read(file):
    
    f=open(file,"rb")
    try:
        while True:
            content=pickle.load(f)
            print(content,end="")

    except EOFError:
        f.close()

#_6__________________________________________________________________________________________________________________
def match_credentials(id,password):
    
    
    query="SELECT S_Id AS ID ,Password FROM student UNION SELECT Emp_Id, Password FROM employee;"
    cursor.execute(query)
    data=cursor.fetchall()
    
    t=(id,password) #create in a tuple form to match that credential
    result=t in data

    return result

#_7__________________________________________________________________________________________________________________
def check_login_response():
    
    result=False
    while (result==False):
        global id
        id=int(input(("\n\n\nEnter Your ID : ")))
        password =input("Enter Your Password : ")
        result=match_credentials(id,password)

        if (result==False):
            print("\nWrong Credentials.... Try Again ! \n\n")
        else:
            query="SELECT S_Id AS ID ,Name FROM student UNION SELECT Emp_Id,Emp_Name FROM employee;"
            cursor.execute(query)
            data= cursor.fetchall()
            for i in data:
                if id in i:
                    print("\n\n\t\t\t\t\t\t\tHi ! {}\n\n".format(i[1]))
            
            return id

#_8__________________________________________________________________________________________________________________
def common(r_id,id):
     
    num=generate()
    sender_id=id
  
     
    receiver_id=r_id

    L_file="_"+str(num)+".dat"
    L_id="#"+str(sender_id)+"_"+str(receiver_id)
  
    query="Insert into letters(Letter_Id,Letter_file) values ('{}','{}')".format(L_id,L_file)
    cursor.execute(query)
    connection.commit()
    print("Start Typing The Letter And Type 'DONE' after writing\n\n\n")
    write(L_file)
    print("\n\nReady for sending the letter.\t",end="")
    fake_loading(2)
    print("\nSent !\n\n")

#_9__________________________________________________________________________________________________________________
def change_password():
    new_password=input("Enter The New Password : ")
    query ="Update student Set password ='{}' Where S_id={}".format(new_password,123456)
    cursor.execute(query)
    connection.commit()
    print("\nPassword Changed To : ",new_password,"\n\n")

#_10_________________________________________________________________________________________________________________
def read_notices(To):
    cursor.execute("Select Notice_file,Notice_Id From notices where Notice_Id like '{}'".format(To))
    data=cursor.fetchall()
    if data==[]:
        print("No NOTICES To Show")
    else:
        c=0
        for i in data:
            c=c+1

            print("\n\t\t\t\t\t\t\t\tNotice: ",c,"\n\n")
            read(i[0])

#_11_________________________________________________________________________________________________________________
def read_letters(To):
    cursor.execute("Select Letter_file From letters where Letter_Id like '{}'".format('%'+str(To)))
    letters=cursor.fetchall()
    if letters==[]:
        print("No LETTERS To Show")
    else:
        c=0
        for i in letters:
            c=c+1
            print("\n\t\t\t\t\t\t\t\tLetter: ",c,"\n\n")
            read(i[0])

#_12_________________________________________________________________________________________________________________
def match_teacher(t_id):
    
    
    query="SELECT Emp_Name FROM employee Where Emp_Id={}".format(t_id)
    cursor.execute(query)
    data=cursor.fetchall()

    if data==[]:
        print("\nNo Such Teacher with ID {} exisit.\nKindly Enter the Correct ID".format(t_id))
        return False
        P_letters()
    else:
        print("\nYou are Going to Type Letter for {}".format(data[0][0]))
        return True




#____________________________________________________________________________________________________________________#__________________________________________________1. STUDENT functions______________________________________________

def S_personal_details():
    query="Select * From student where S_Id={}".format(id)
    cursor.execute(query)
    data=cursor.fetchall()
    
    s="\n\nID: {}\tName: {}\tClass: {}\t Section: {}\tDOB: {}\t\tSex: {}\n"
    print(s.format(data[0][0], data[0][1],data[0][2],data[0][3],data[0][5], data[0][4]) )

    s="Father Name: {}\tOccupation: {}\nMother Name: {}\tOccupation: {}\n"
    print(s.format(data[0][6], data[0][7],data[0][8],data[0][9] ))

    s="Contact: {}\t\tAddress: {}\nPassword: {}\n"
    print(s.format(data[0][11], data[0][10],data[0][12] ))

def fee_details():
    query="Select * From fee_details"
    cursor.execute(query)
    data=cursor.fetchall()
    query="Select * From fee_details where S_Id ={}".format(id)
    cursor.execute(query)
    data=cursor.fetchall()
   
    s="Your ID: {}\n\nQuarter I: {}\nQuarter II: {}\nQuarter III: {}\n\nPenalties: {}\n\n"
    print(s.format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))
    
def progress_report():
    query="Select * From progress_report where S_Id ={}".format(id)
    cursor.execute(query)
    data=cursor.fetchall()
    
    s="Your ID: {}\n\nUnit Test-I: {}%\nHalf Yearly: {}%\nUnit Test-II: {}%\nAnnual {}%\n\n"
    print(s.format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))

def issue_books():
    print("\n\t\t\t\t\t\t\tWelcome To The LIBRARY\n\n")
    S_Id=id
    print("\nSelect the Required Books From the Provided List in the following format :")
    print("Format : [Sno1,Sno2,....]\n")
    print("Ex : If you want book no.3 only -->[3]")
    print("Ex : If you want book no.3,4,8 -->[3,4,8]\n\n")

    query="Select Book_Id,Book_Name,Book_Author From Books"
    cursor.execute(query)
    data=cursor.fetchall()
    

    i=0
    for book in data:
        i=i+1
        print(i,". ",book[1]," BY ",book[2])
    
    print()
    issue_response=eval(input())
    cursor.execute("select curdate()")
    date =cursor.fetchone()[0]
    
    #Updating the library
    print("\n\nFollowing Books Are Issued to You : \n\n")
    for n in issue_response:
        book_id=data[n-1][0]
     
        query1="Update Books Set Book_Issued_Qty = Book_Issued_Qty + 1 Where Book_id={}".format(book_id)
        query2="Insert into issuedbookdetails values({},{},'{}')".format(book_id,S_Id,date)

        cursor.execute(query1)
        cursor.execute(query2)
        connection.commit()
        print(data[n-1][1], " BY ",data[n-1][2])
        
def S_letters():
    print("\n\nYou Can Send the Letter ONLY TO Principal.....! \n")
    num=generate()
    sender_id=id
  
    cursor.execute("Select Emp_Id From employee Where Duty='{}'".format('Principal'))
    data=cursor.fetchall()
    receiver_id=data[0][0]

    L_file="_"+str(num)+".dat"
    L_id="#"+str(sender_id)+"_"+str(receiver_id)
  
    query="Insert into letters(Letter_Id,Letter_file) values ('{}','{}')".format(L_id,L_file)
    cursor.execute(query)
    connection.commit()
    print("Start Typing The Letter And Press 'DONE' after writing\n\n\n")
    write(L_file)
    
    print("\n\nReady for sending the letter.\t",end="")
    fake_loading(2)
    print("\nSent !\n\n")
    
def S_notices():
    read_notices('%S')

def student(id):
    
    #Functions which a student can perform.....
    print("\tKEYS\tOPERATIONS\n")
    print("\t1.\tCheck the Personal Details.")
    print("\t2.\tCheck the Fee Details.")
    print("\t3.\tCheck Your Prgress Report.")
    print("\t4.\tGet Book From Library.")
    print("\t5.\tWriter a Letter.")
    print("\t6.\tCheck the Notices.")
    print("\t7.\tChange Your Password.")
    print("\t0.\tGo Back To Home Page.")
    
    operation_response_keys={
    1:S_personal_details,
    2:fee_details,
    3:progress_report,
    4:issue_books,
    5:S_letters, 
    6:S_notices,
    7:change_password,
    0:home
    }
    
    
    operation_response=None
    s=""
    while operation_response!=0:
        print("\n\nWhat",s,"You Want To Do......\t",end="")
        operation_response=int(input())
        operation_response= check_response(operation_response,operation_response_keys)
        s="Else"
        


#____________________________________________________________________________________________________________________#__________________________________________________2. EMPLOYEE functions_____________________________________________


def Emp_personal_details():
    query="Select * From employee where Emp_Id={}".format(id)
    cursor.execute(query)
    data=cursor.fetchall()
    
    s="\n\nID: {}\tName: {}\tDOB: {}\tSex: {}\n"
    print(s.format(data[0][0], data[0][1],data[0][3],data[0][2] ))

    s="Father Name: {}\tMother Name: {}\n"
    print(s.format(data[0][4], data[0][5]))

    s="Contact: {}\tAddress: {}\nDuty: {}\t\tJoining Date: {}\tSalary: {}\n"
    print(s.format(data[0][7], data[0][6],data[0][9],data[0][8],data[0][11] ))

    s="Password: {}\n"
    print(s.format(data[0][12]))

def Emp_letters():
    print("\nYou can send the Letters to the following : ")
    print("1. Principal\n2. Director\n")
    global principal_id
    global director_id

    inp= int(input())
    if inp==1:
        
        common(principal_id,id)
    

    elif inp==2:
       
        common(director_id,id)
    
    else:
        print("Enter the Correct Keys \n\n")
        Emp_letters()
           
def Emp_notices():
    read_notices('%E')

def Emp_check_letters():
    read_letters(id)
def employee(id):
    #Functions which a employee can perform.....
    
    print("\tKEYS\tOPERATIONS\n")
    print("\t1.\tCheck the Personal Details.")
    print("\t2.\tWrite a Letter.")
    print("\t3.\tCheck the Letters.")
    print("\t4.\tCheck the Notices.")
    print("\t5.\tChange Your Password.")
    print("\t0.\tGo Back To Home Page.")
    
    operation_response_keys={
    1:Emp_personal_details,
    2:Emp_letters, 
    3:Emp_check_letters,
    4:Emp_notices,
    5:change_password,
    0:home
    }
    
    operation_response=None
    s=""
    while operation_response!=0:
        print("\n\nWhat",s,"You Want To Do......\t",end="")
        operation_response=int(input())
        operation_response= check_response(operation_response,operation_response_keys)
        s="Else"
        if(operation_response==0):
            break


#____________________________________________________________________________________________________________________#__________________________________________________3. PRINCIPAL functions____________________________________________



def P_letters():
    print("\nYou can send the Letters to the following : ")
    print("1. Teacher\n2. Director\n")
    global director_id
   
    
    inp= int(input())
    if inp==1:  
        result=False
        while result==False:
             
             t_id=int(input("\nEnter the ID of that Teacher :"))
             result=match_teacher(t_id)

             if result==True:
                 common(t_id,id)
                 break

    elif inp==2:
       common(director_id,id=102030)
    
    else:
        print("\nEnter the Correct Keys \n")
        P_letters()

def P_check_notices():
    read_notices('%P')

def P_check_letters():
    global principal_id
    read_letters(principal_id)
 
def issue_notice():
    print("\n\nYou Can Send the Notices To Students and Employees.....! \n\n")
    num=generate()
    sender_id=id
    codes={1:"S",2:"E"}

    print("Select Any One Whom You Want To Send The NOTICE : \n1. Students\n2. Employees\n")
    whom = int(input())
    
    if whom in  codes:
        duty_code=codes[whom]


        N_file="_"+str(num)+".dat"
        N_id="#"+str(sender_id)+"_"+str(duty_code)
  
        query="Insert into notices(Notice_Id,Notice_file) values ('{}','{}')".format(N_id,N_file)
        cursor.execute(query)
        connection.commit()
        print("Start Typing The Notice And Press 'DONE' after writing\n\n\n")
        write(N_file)
    
    else:
        print("\nKindly Enter the Correct Keys \n")
        issue_notice()

def principal(id):
    #Functions which a principal can perform.....
    print("\tKEYS\tOPERATIONS\n")
    print("\t1.\tCheck the Personal Details.")
    print("\t2.\tWriter a Letter.")
    print("\t3.\tCheck the Letters.")
    print("\t4.\tCheck the Notices.")
    print("\t5.\tIssue Notice.")
    print("\t6.\tChange Your Password.")
    print("\t0.\tGo Back To Home Page.")
    
    operation_response_keys={
    1:Emp_personal_details,
    2:P_letters, 
    3:P_check_letters,
    4:P_check_notices,
    5:issue_notice,
    6:change_password,
    0:home
    }
    
    operation_response=None
    s=""
    while operation_response!=0:
        print("\n\nWhat",s,"You Want To Do......\t",end="")
        operation_response=int(input())
        operation_response= check_response(operation_response,operation_response_keys)
        s="Else"
     

#____________________________________________________________________________________________________________________#__________________________________________________4. DIRECTOR functions_____________________________________________

def D_letters():
    print("\nYou can send the Letters to the following : ")
    print("1. Teacher\n2. Principal\n")
    global principal_id
   
    
    inp= int(input())
    if inp==1:  
        result=False
        while result==False:
             
             t_id=int(input("\nEnter the ID of that Teacher :"))
             result=match_teacher(t_id)

             if result==True:
                 common(t_id,id)
                 break

    elif inp==2:
       common(principal_id,id)
    
    else:
        print("\nEnter the Correct Keys \n")
        D_letters()

def D_check_letters():
    global director_id
    read_letters(director_id)

def director(id):
    #Functions which a principal can perform.....
    print("\tKEYS\tOPERATIONS\n")
    print("\t1.\tCheck the Personal Details.")
    print("\t2.\tWriter a Letter.")
    print("\t3.\tCheck the Letters.")
    print("\t4.\tIssue Notice.")
    print("\t5.\tChange Your Password.")
    print("\t0.\tGo Back To Home Page.")
    
    operation_response_keys={
    1:Emp_personal_details,
    2:D_letters, 
    3:D_check_letters,
    4:issue_notice,
    5:change_password,
    0:home
    }
    
    operation_response=None
    s=""
    while operation_response!=0:
        print("\n\nWhat",s,"You Want To Do......\t",end="")
        operation_response=int(input())
        operation_response= check_response(operation_response,operation_response_keys)
        s="Else"


#____________________________________________________________________________________________________________________#__________________________________________________REGISTERATION functions_________________________________________


def match_Id(user_id) :
    query="SELECT S_Id AS ID FROM student UNION SELECT Emp_Id FROM employee;"
    cursor.execute(query)
    data=cursor.fetchall()
    t=(user_id,)
    bool= t in data

    if bool==True:
        return True
    else :
        return False

def stu_details(user_id,password):
    name=input("Enter the Name: ")
    _class=input("Enter the Class: ")
    sec=input("Enter the Section: ")[0]
    sex=input("Enter the Sex(M/F): ")[0]
    dob=input("Enter the DOB (YYYY-MM-DD): ")
    fname=input("Enter Your Father Name: ")
    foccu=input("Enter Your Father Occupation: ")
    mname=input("Enter Your Mother Name: ")
    moccu=input("Enter Your Mother Occupation: ")
    address=input("Enter Your Address: ")
    cno=input("Enter Your Contact number: ")[:11]
    dcode='S'

    query="Insert Into student Values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(user_id,name,_class,sec,sex,dob,fname,foccu,mname,moccu,address,cno,password,dcode)
    
    return query

def emp_details(user_id,password):
    
    name=input("Enter the Name: ")
    sex=input("Enter the Sex(M/F): ")[0]
    dob=input("Enter the DOB (YYYY-MM-DD): ")
    fname=input("Enter Your Father Name: ")
    mname=input("Enter Your Mother Name: ")
    address=input("Enter Your Address: ")
    cno=input("Enter Your Contact number: ")[:11]
    doj=input("Enter the Joining Date (YYYY-MM-DD): ")
    duty=input("Enter the Duty: ")
    dcode=input("Enter the Duty Code As Provided: ")
    sal=input("Enter the Monthly Salary: ")
    

    query="Insert Into employee Values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}')".format(user_id,name,sex,dob,fname,mname,address,cno,doj,duty,dcode,sal,password)
    
    return query


def save_details(user_id,password,table):
    print("\nEnter Your Personal information\n")
    
    if table=='student':
        query = stu_details(user_id,password)
    elif table=='employee':
        query=emp_details(user_id,password)

    cursor.execute(query)
    connection.commit()


def register_student():
    print("\n\nEnter Your 6 digit ID As Provided From The School Authoity ")
    S_id=int(input()[:6])
    print(S_id)
    bool=match_Id(S_id)

    if bool==True:
        print("\n This ID is already present.\nTherefore, you are redirected to the login page.")
        login()
    else:
       password=input("Enter a Storng Password :  ")
       save_details(S_id,password,"student")


def register_employee():
    print("\n\nEnter Your 6 digit ID As Provided From The School Authoity ")
    S_id=int(input()[:6])
    
    bool=match_Id(S_id)

    if bool==True:
        print("\n This ID is already present.\nTherefore, you are redirected to the login page.")
        login()
    else:
       password=input("Enter a Storng Password :  ")
       save_details(S_id,password,"employee")


def register():
    print("\nYou want to Register yourself as :\n1. Student\n2. Employee\n0. Return back to Home Page")
    
    register_response_keys={1:register_student,2:register_employee ,0: home}

    register_response=None
    while register_response not in register_response_keys:
        
        register_response=int(input())
        register_response= check_response(register_response,register_response_keys)
 

#____________________________________________________________________________________________________________________#__________________________________________________LOGIN functions___________________________________________________


def login():
    global principal_id
    global director_id
    print("\t\t\t\t\t\t\tLOGIN PAGE")

    login_response_keys=[1,2,3,4]
    functions={1:student,2:employee,3:principal,4:director}
    id =None

    print("You want to Login as :\n1.Student\n2.Employee\n3.Principal\n4.Director\n")
    login_response=int(input())

    bool=login_response  in login_response_keys

    if bool==True:
        
        id=check_login_response()
        if id==principal_id:
            principal(id)
        elif id==director_id:
            director(id)
        else:
            functions[login_response](id)
    else:
        while (bool==False):
            print("\nEnter the Correct Key Combinations \n")
            login_response=int(input())
            bool=login_response  in login_response_keys
            if bool==True:
                
                id=check_login_response()
                if id==principal_id:
                    principal(id)
                elif id==director_id:
                    director(id)
                else:
                    functions[login_response](id)


#____________________________________________________________________________________________________________________#__________________________________________________HOME functions___________________________________________________ 

def home():
    print("\n\n\t\t\t\t\tWelcome To The HOME Page Of The Pillars Public School-App")
    print("\n\nInstructions For Using the App\n\n")
    print("1. Enter the Correct Keys As Mentioned.")
    print("2. To Register Yourself on the School App, Press '1'")
    print("3. To Login on the School App, Press '2'")
    print("4. Inorder to Quit the App, Press '-1'")
    choice=int(input("\nEnter Your Choice:\t"))

    if choice==1:
        register()
    elif choice==2:
        login()
    elif choice==-1:
        print("Quitting the App....")
        fake_loading(2)
    else: 
        print("\nEntered Wrong Choice\n")
        home()


#____________________________________________________________________________________________________________________#__________________________________________________EXECUTION BLOCK___________________________________________________


query="Select Emp_Id From employee Where Duty='{}' or Duty='{}'".format('Principal','Director')
cursor.execute(query)
data=cursor.fetchall()
principal_id=data[0][0]
director_id=data[1][0] 

home()


#Checck the foreign keys in the tables