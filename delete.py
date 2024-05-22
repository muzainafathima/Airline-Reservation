#DELETE AN ACCOUNT
import mysql.connector as sql
def dele():
    try:
        con=sql.connect(host='localhost',user='root',passwd='#muzaina1234',database='airline')
        cursor=con.cursor()
        username=input("ENTER YOUR USERNAME TO DELETE YOUR ACCOUNT:")
        password=input("ENTER YOUR PASSWORD:")
        confirm=input("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT(Y/N):")
        if confirm=='Y' or 'y':
            query="DELETE FROM login WHERE username='{}'".format(username)
            cursor.execute(query)
            cursor.close()
            con.close()
            print("ACCOUNT DELETED SUCCESSFULLY")
        else:
            print("DELETION CANCELLED")
    except:
        print('''THE SPECIFIED ACCOUNT DOES NOT EXIST.
                PLEASE INPUT A VALID USERNAME''')
        
