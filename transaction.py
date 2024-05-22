import mysql.connector as sql
import cabin_class
import datetime
import reservation
import string_generator
now=datetime.datetime.now
def payment():
    con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
    cursor=con.cursor()
    print("---------- TRANSACTION ----------".center(50))
    name=input("Enter your name:")
    print("1.Visacard")
    print("2.Paypal")
    print("3.Mastercard")
    ch=int(input("Select your choice"))
    q="SELECT * FROM  passengers WHERE name= {}".format(name)
    cursor.execute(q)
    item=cursor.fetchall()
    for k in item:
        a=k[0]
    batch=input("Enter your batch number:")
    q1="SELECT * FROM cabin_class WHERE batch={}".format(batch)
    cursor.execute(q1)
    i=cursor.fetchall()
    for l in i:
        b1=l[0]
        b2=l[1]
    q2="SELECT * FROM location WHERE batch={}".format(batch)
    cursor.execute(q2)
    i2=cursor.fetchall()
    for m in i2:
        c1=m[1]
        c2=m[2]
        c3=m[0]
    flightno=string_generator.flight()
    bookingno=string_generator.ticket()
    if ch==1:
        card="Visacard"
        cardno=int(input("Enter your card pin:"))
        expirydate=input("Enter card expiry date(yyyy-mm-dd):")
        query="""INSERT INTO payment(name,card,cardno,expirydate,bookingno,batch)
        values('{}','{}',{},'{}',{},{})
        """.format(name,card,cardno,expirydate,bookingno,batch)
    elif ch==2:
        card="Paypal"
        cardno=int(input("Enter your card pin:"))
        expirydate=input("Enter card expiry date(yyyy-mm-dd):")
        query="""INSERT INTO payment(name,card,cardno,expirydate,bookingno,batch)
        values('{}','{}',{},'{}',{},{})
        """.format(name,card,cardno,expirydate,bookingno,batch)
    elif ch==3:
        card="Mastercard"
        cardno=int(input("Enter your card pin:"))
        expirydate=input("Enter card expiry date(yyyy-mm-dd):")
        query="""INSERT INTO payment(name,card,cardno,expirydate,bookingno,username)
        values('{}','{}',{},'{}',{},{})
        """.format(name,card,cardno,expirydate,bookingno,batch)
    else:
        print("INVALID CHOICE!!!TRY AGAIN")
    cursor.execute(query)
    airline=reservation.airliner()
    #BOARDING PASS    
    print("-"*30,"BOARDING PASS","-"*30)   
    print("  ","AIRLINES-".center(20),airline)
    print("  ","PASSENGER NAME-".center(20),name) 
    print("  ","CABIN CLASS-".center(20),b1)      
    print("  ","DEPARTURE-".center(20),c1)        
    print("  ","ARRIVAL-".center(20),c2)         
    print("  ","MODE OF FLIGHT-".center(20),c3)  
    print("  ","MODE OF PAYMENT-".center(20),card)
    print("  ","RESERVATION DATE-".center(20),date())
    print("  ","FLIGHT NUMBER-".center(20),flightno)     
    print("  ","TICKET NUMBER-".center(20),bookingno)    
    print("  ","PASSENGER'S COUNTRY-".center(20),a) 
    print("\t\t\t\t\t",now)
    print("---PAID---".center(20),b2) 
    print("---THANK YOU FOR CHOOSING US.HAVE A SAFE JOURNEY---.".center(50))
    con.commit()
    cursor.close()
    con.close()
def date():
    con=sql.connect(host='localhost',user='root',passwd='#muzaina123',database='airline')
    cursor=con.cursor()
    query="SELECT * FROM  sampledate"
    cursor.execute(query)
    dat=cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()
    a=str(dat)
    b=a[15:26]
    print(b)
def refund():
    con=sql.connect(host='localhost',user='root',passwd='#muzaina123',database='airline')
    cursor=con.cursor()
    q="SELECT * FROM payment"
    cursor.execute(q)
    i=cursor.fetchall()
    print("--------REFUND--------".center(55))
    booking_no=int(input("Enter your ticket number:"))
    check=False
    for data in i:
        if booking_no==data[4]:
            check=True
        if check:
            print("Proceed...")
        else:
            print("The following booking number has never been issued previously.\
            Please check if you have entered it correctly.")
            break
    name=input("Enter your name:")
    flightno=input("Enter your flight number:")
    depdate=input("Enter your departure date(yyyy-mm-dd):")
    refund =input("Enter the mode you want your refund in:")
    amt=int(input("Enter the amount paid:"))
    amt=amt*20/100
    query="Insert INTO refund(booking_no,name,flightno,depdate,amt)values({},'{}','{}','{}',{})".format(booking_no,name,flightno,depdate,amt)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("-"*50,"REFUND RECEIPT","-"*50)
    print("BOOKING NUMBER:",booking_no)
    print("NAME OF THE PASSENGER:",name)
    print("FLIGHT NUMBER:",flightno)
    print("THE MODE OF REFUND SELECTED:",refund)
    print("THE AMOUNT REFUNDED:",amt)
    print("-"*35,"THANK YOU FOR CHOOSING US","-"*35)
    print("-"*100)



    
    
           
    
