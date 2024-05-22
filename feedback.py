#feedback
import mysql.connector as sql

con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')


def reviews():
    review="""HOPE YOU HAVE A SAFE JOURNEY!
    PLEASE TAKE A MOMENT TO TELL
    US ABOUT YOUR EXPERIENCE WITH OUR SERVICE:"""
    input(review)
    rate=input("RATE out of *****:")
    query="INSERT INTO feedback(review,rate)values(review,rate)".format(review,rate)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
   
           
def show_reviews():
    query="SELECT * FROM feedback"
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    item=cursor.fetchall()
    for i in item:
        print("\t",i,"\t")
    cursor.close()

con.close()
