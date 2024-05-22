#seat,mode of flight,date
import mysql.connector as sql
import transaction
def seat():
    con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
    cursor=con.cursor()
    print("ECONOMY CLASS:")
    print("""\tOne piece of carry on baggage is permitted with maximum dimensions 55X38X20cm.
\tMaximum weight:7 Kg""")
    print("FIRST AND BUSINESS CLASS:")
    print("""\tTwo piece of carry on naggage is permitted: one briefcase and one garment bag.
\tThe total combined weight may not exceed 14Kgs.Garment bag with dimensions 55X38X20cm""")
    print("1.First Class -800$ per seat")
    print("2.Business Class -500$ per seat")
    print("3.Economics Class -200$ per seat")
    ch=int(input("CHOOSE A CHOICE:"))    
    batch=input("Enter your batch number:")
    if ch==1:
        a="First"
        cost="800$"
        query="INSERT INTO cabin_class(class,cost,batch)values('{}','{}',{})".format(a,cost,batch)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
    elif ch==2:
        a="Second"
        cost="500$"
        query="INSERT INTO cabin_class(class,cost,batch)values('{}','{}',{})".format(a,cost,batch)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
    elif ch==3:
        a="Third"
        cost="500$"
        query="INSERT INTO cabin_class(class,cost,batch)values('{}','{}',{})".format(a,cost,batch)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
    else:
        print("INVALID CHOICE!!!TRY AGAIN")
    print("-"*35,"MODE OF FLIGHT","-"*35)
    flight()
    
def flight():
    con=sql.connect(host='localhost',user='root',passwd='#muzaina123',database='airline')
    cursor=con.cursor()
    print("-----SELECT YOUR ORIGIN AND DESTINATION-----".center(55))
    country=input("Enter passenger country:")
    print("\t\t1.INTERNATIONAL FLIGHT")
    print("\t\t2.DOMESTIC FLIGHT")
    ch=int(input("Enter your choice:"))
    batch=input("Enter your batch number:")
    if ch==1:
        flight="International"
        print("--WELCOME TO INTERNATIONAL FLIGHT--".center(30))
        departure=input("Enter Departure:")
        arrival=input("Enter Arrival:")
        query="""INSERT INTO location(flight_type,departure,arrival,batch)values('{}','{}','{}',{})
        """.format(flight,departure,arrival,batch)
    elif ch==2:
        flight="Domestic"
        print("--WELCOME TO DOMESTIC FLIGHT--".center(30)) 
        departure=input("Enter Departure:")
        arrival=input("Enter Arrival:")
        query="""INSERT INTO location(flight_type,departure,arrival,batch)values('{}','{}','{}',{})
        """.format(flight,departure,arrival,batch)
    else:
        print("INVALID CHOICE!!!TRY AGAIN")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    transaction.payment()  




