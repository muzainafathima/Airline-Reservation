import reservation         
import food
import transaction                   
import feedback
import delete 
def main():
    while True:
        print("1.RESERVATION")
        print("2.REFUND")
        print("3.CUISINE")
        print("4.DELETE YOUR ACCOUNT")
        print("5.REVIEWS")
        print("6.EXIT")
        ch=int(input("---Enter your choice---:"))
        if ch==1:
            print("-"*35,"RESERVATION","-"*35)
            reservation.booking()  
        elif ch==2:
            transaction.refund()                              
        elif ch==3:
            food.food_menu()
            food.food_receipt()            
        elif ch==4:
            delete.dele()
            break
        elif ch==5:
            feedback.reviews()
        else:
            print("-"*25,"THANL YOU FOR CHOOSING US!","-"*25)
            break

