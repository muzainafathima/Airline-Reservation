#reservation
import mysql.connector as sql
import cabin_class
import login
con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
cursor=con.cursor()
def booking():
        name=input("Enter Passenger Name:")
        email=input("Enter Passenger E-mail address:")
        country=input("Enter Passenger country:")
        dob=input("Enter date of birth:(yyyy-mm-dd)")
        address=input("Enter Passenger address:")
        pincode=int(input("Enter pincode"))
        mobile=int(input("Enter Mobile No.:"))
        rdate=input("Enter the Reservation Date(yyyy-mm-dd):")
        dest=input("Enter Your Destination")
        batch=input("Enter your batch number:")
        query="""INSERT INTO passengers(name,email,country,dob,address,pincode,mobile,rdate,dest,batch)
        values('{}','{}','{}','{}','{}',{},{},'{}','{}',{})
        """.format(name,email,country,dob,address,pincode,mobile,rdate,dest,batch)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        print("Customer Details Accessed")
        print("-"*35,"CABIN CLASS","-"*35)
        cabin_class.seat()
    #try:
        
'''    except:
        print("Information Not Saved")'''
    
def airliner():
    airliner=input("Enter the airline you want to travel in:")
    return airliner



