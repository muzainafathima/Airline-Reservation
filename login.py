import mysql.connector as sql
import string_generator
import mainpg
def signup():
    con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
    cursor=con.cursor()
    print("*"*50)
    print("SIGNUP HERE")
    username=input("ENTER YOUR USERNAME:")
    query="SELECT USERNAME FROM LOGIN"
    cursor.execute(query)
    item=cursor.fetchall()
    password=input("ENTER YOUR PASSWORD:")
    password1=input("CONFIRM YOUR PASSWORD:") 
    if username in item:
        print("THIS USERNAME IS TAKEN. PLEASE TRY ANOTHER ONE")
        us=input("ENTER YOUR USERNAME:")
        query1="INSERT INTO login(username,passwd)VALUES('{}','{}')".format(us,password)
    else:
        query1="INSERT INTO login(username,passwd)VALUES('{}','{}')".format(username,password)     
    if password != password1:
        print("Passwords do not match. please try again...")
    else:
        print("ACCOUNT CREATED SUCCESSFULLY!")
    batch=string_generator.batch()
    print("THIS IS YOUR BATCH NUMBER:",batch)    
    mainpg.main()
    cursor.execute(query1)
    con.commit()
    cursor.close()
    con.close()
def login_():
    print("*"*50)
    con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
    cursor=con.cursor()
    print("LOGIN HERE")
    username =input("ENTER YOUR USERNAME:")
    pss=input("ENTER YOUR PASSWORD:")
    batch=string_generator.batch()    
    #cursor=con.cursor()
    query="SELECT * FROM login "
    cursor.execute(query)
    cname=cursor.fetchall()
    login=False
    for data in cname:
        if username==data[0] and pss==data[1]:
            login=True
    if login:
        print("Logged in successfully")
        print("THIS IS YOUR BATCH NUMBER:",batch)
        mainpg.main()    
    else:
        print("SORRY THE ACCOUNT DOES'NT EXIST. PLEASE SIGN UP.")
        confirm=input("Do you want to sign up(Y/N):")
        if confirm=='y' or confirm=='Y':
            signup()
        else:
            print("HAVE A NICE DAY")
      
    

