
#1st page 
import login
print("------WELCOME TO OUR FLIGHT RESERVATION SYSTEM------".center(70))
print("--LOGIN OR SIGNUP TO PROCEED--".center(65))
print("---MAIN FORM---".center(65))
#LOGIN OR SIGNUP  
while True:
    print("1.SIGN UP")
    print("2.LOGIN")
    ch=int(input("---Enter your choice---:"))
    if ch==1:
        print("Creating your account...")
        login.signup()        
    elif ch==2:
        
        print("Logging in...")
        login.login_()                            
    else:
        print("Invalid choice")
        break



