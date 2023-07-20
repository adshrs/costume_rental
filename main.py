from functions import *


loop = False
while loop == False:
        print("")
        print("+-------------------------------------------+")
        print("| Welcome to Our Costume Rental Application |")
        print("+-------------------------------------------+")
        print("")
        print("(1) Enter 1 to rent Costume")
        print("(2) Enter 2 to return Costume")
        print("(3) Enter 3 to to exit")
        print("")
        
        while True:
            try:
                main_select = int(input("Select an option: "))
                break
            except:
                print("Please enter a numeric value.")
                
        if main_select < 1 or main_select > 3:
            print("please select an existing option.")
        if main_select == 1:
            rent()
        if main_select == 2:
            return_()
        if main_select == 3:
            print("Thanyou for using our application. :)")
            
            loop = True


