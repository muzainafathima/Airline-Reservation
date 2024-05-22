#food
import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
cursor=con.cursor()

def food_menu():
    print("-"*20,"FOOD MENU","-"*20)
    query="SELECT * from food"
    cursor.execute(query)
    item=cursor.fetchall()
    print("\t Sno.","\t Food Items","\t Price")
    for i in item:
        if i[1]=="Tea" or  i[1]=="Pizza" or i[1]=="Pasta":
            print("\t",i[0],"\t",i[1],"\t\t",i[2])
        else:
            print("\t",i[0],"\t",i[1],"\t",i[2])
    print("-"*50)

def food_receipt():
    ch=int(input("ENTER YOUR CHOICE:"))
    print("-"*50)
    pay=input("Enter your payment method:")
    pin=int(input("Enter your pin:"))
    print("----FOOD RECEIPT----".center(55))
    if ch==1:
        query="SELECT * from food where sno=1"
        cursor.execute(query)
        item=cursor.fetchone()
       
    if ch==2:
        query="SELECT * from food where sno=2"
        cursor.execute(query)
        item=cursor.fetchone()
       
    if ch==3:
        query="SELECT * from food where sno=3"
        cursor.execute(query)
        item=cursor.fetchone()
      
    if ch==4:
        query="SELECT * from food where sno=4"
        cursor.execute(query)
        item=cursor.fetchone()
        
    if ch==5:
        query="SELECT * from food where sno=5"
        cursor.execute(query)
        item=cursor.fetchone()
        
    if ch==6:
        query="SELECT * from food where sno=6"
        cursor.execute(query)
        item=cursor.fetchone()
        
    if ch==7:
        query="SELECT * from food where sno=7"
        cursor.execute(query)
        item=cursor.fetchone()
        
    if ch==8:
        query="SELECT * from food where sno=8"
        cursor.execute(query)
        item=cursor.fetchone()
        
    if ch==9:
        query="SELECT * from food where sno=9"
        cursor.execute(query)
        item=cursor.fetchone()
        
    if ch==10:
        query="SELECT * from food where sno=10"
        cursor.execute(query)
        item=cursor.fetchone()
    for i in item:
        a = isinstance(i, str)
        if a == True:
            c = i
        else:
            b = i
    print("Items Purchased ",c)
    print('Amount',b)
    print("PAID")
    print("HOPE YOU ENJOYED YOUR MEAL")
    print("-"*50)
    
    





      
