#Importing modules
import datetime


#Defining function to read the .txt file
def read_file():
    file = open("abc.txt", "r")
    Resource = file.readlines()
    
    return Resource

#Defining function to write in the data dictionary
def dict(readfile):
    dict = {}
    
    for i in range(len(readfile)):
        dict[i + 1] = readfile[i].replace("\n", "").split(",")
        
    return dict

#Defining function for displaying list of costumes and its details
def menu(dict):
    print("")
    print("+---------------------------------------------------------+")
    print("| S.N.", "\t", "Costume Name", "\t\t",
          "Brand", "\t", "Price", "\t", "Quantity |")
    print("+---------------------------------------------------------+")

    for key, value in dict.items():
        print("| ", key, "\t", value[0], "\t", value[1],
              "\t", value[2], "\t", value[3], "       |")
    print("+---------------------------------------------------------+")
    print("")
        
    return ""

#Defining function for date and time
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    date = year + ":" + month + ":" + day
    
    return date


def timee():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    time = str(hour + minute + second)
    
    return time

#Defining function For id validation
def id_validation(dict):
    loop = False
    
    while loop == False:
        while True:
            try:
                s_number = int(input("Select Costume ID: "))
                break
            except:
                print("Please enter a Numeric Value.")
                
        if s_number < 1 or s_number > len(dict):
            print("ID is invalid")
        else:
            return s_number

#Defining function For quanitity validation
def quantity_validation():
    loop = True
    
    while loop == True:
        while True:
            try:
                quantity_no = int(input("Select quantity: "))
                break
            except:
                print("Please enter a Numeric Value.")
                
        if quantity_no < 1:
            print("You need to select atleast one.")
        else:
            return quantity_no

#Defining function for combination of id_validation and quantity_validation
def id_and_quantity():
    loop = False
    while loop == False:
        data = id_validation(main_data)

        if int(main_data[data][3]) > 0:
            quantity_no = quantity_validation()
            if quantity_no > int(main_data[data][3]):
                print("We dont have enough in stock for your selected quantity.")
            else:
                cart.append(data)
                quant.append(quantity_no)
                
                main_data[data][3] = int(main_data[data][3]) - quantity_no
                main_data[data][3] = str(main_data[data][3])
                menu(main_data)
                update_quantity(main_data)
                
                loop = True
        else:
            print("We are out of stock.")


#Defining function for updating quantity in text file
def update_quantity(dict):
    file = open("abc.txt", "w")
    
    for value in dict.values():
        write = value[0] + "," + value[1] + \
            "," + value[2] + "," + value[3] + "\n"
        file.write(write)
    file.close()

#Defining function for renting multiple costumes
def multiple_rent():
    loop = False
    
    while loop == False:
        multiple = input("Rent again? Enter 'yes' to rent again and 'no' to exit: ")
        
        if multiple == "yes":
            if total_quantity() == 0:
                print("We are out of Stock")
                loop = True
            else:
                id_and_quantity()
        elif multiple == "no":
            loop = True
        else:
            print("Enter 'yes' to Rent Again and 'no' to exit: ")

#Defining function for displaying invoice
def invoice(name, phone, title):
    print("")
    print("------------------------------------")
    print("        "+title+" Invoice")
    print("------------------------------------")
    print("Costumer Name: ", name)
    print("Costumer Phone: ", phone)
    print()
    print("------------------------------------")
    print("          Costume Details")
    print("------------------------------------")
    for i in range(len(cart)):
        print("Costume : ", main_data[cart[i]][0])
        print("Costume Brand: ", main_data[cart[i]][1])
        print("Quantity: ", quant[i])
        print()
    print("------------------------------------")

#Defining Function For Renting
def total_quantity():
    sum = 0
    for i in main_data:
        sum = int(main_data[i][3])+sum
    return sum


def rent():
    menu(main_data)
    
    if total_quantity() == 0:
        print("We are out of stock.")
    else:
        id_and_quantity()
        multiple_rent()
        name = input("Enter Your Name: ")
        phone = input("Enter Your Phone number: ")
        price_ = 0.0
        for i in range(len(cart)):
            price = float(main_data[cart[i]][2]) * quant[i]
            price_ = price_ + price
        invoice(name, phone, "Rent")
        print("Date: ", date())
        print("Total Price: ", price_)
        
        file = invoice_write(name, phone, "Rent")
        file.write("\nTotal Price: " + str(price_))
        file.write("\n------------------------------------")

#Defining function to return
def return_():
    menu(main_data)
    
    loop1 = False
    
    while loop1 == False:
        data = id_validation(main_data)
        quantity_no = quantity_validation()
        cart.append(data)
        quant.append(quantity_no)
        
        main_data[data][3] = int(main_data[data][3]) + quantity_no
        main_data[data][3] = str(main_data[data][3])
        
        menu(main_data)
        update_quantity(main_data)
        
        fine = 0.0
        
        loop2 = False
        
        while loop2 == False:
            multiple = input("Want to Return Again?")

            if multiple == "yes":
                loop1 = False
                loop2 = True
            elif multiple == "no":
                loop3 = False
                while loop3 == False:
                    time = input("Are the costumes returned in time?")

                    if time == "yes":
                        print("Thank You:)")
                        loop3 = True
                    elif time == "no":
                        while True:
                            try:
                                days = int(
                                    input("How many days is it returned late?: "))
                                
                                fine = days*10

                                loop3 = True

                                break
                            except:
                                print("Please enter a Numeric Value.")
                    else:
                        print("yes or no")
                        
                        loop3 = False
                        
                name = input("Enter Your Name: ")
                phone = input("Enter Your Phone number: ")
                invoice(name, phone, "Return")
                print("Your Total File is :", fine)

                file = invoice_write(name, phone, "Return")
                file.write("\nTotal Fine: "+str(fine))
                file.write(
                    "\n------------------------------------")
                loop1 = True
                loop2 = True
            else:
                print("yes or no")

#Defining function for writing invoice

def invoice_write (name, phone, title):
    print("------------------------------------")
    file = open(str(name)+str(timee())+".txt", "w")
    file.write("\n------------------------------------")
    file.write("\n        "+title + " Bill ")
    file.write("\n------------------------------------")
    file.write("\nCostumer Name: "+str(name))
    file.write("\nCostumer Phone: "+str(phone))
    file.write("\nDate :"+str(date()))
    file.write("\n")
    file.write("\n------------------------------------")
    file.write("\n          Costume Details")
    file.write("\n------------------------------------")
    for i in range(len(cart)):
        file.write("\nCostumesName: "+str(main_data[cart[i]][0]))
        file.write("\nBrand :"+str(
            main_data[cart[i]][1]))
        file.write("\nQuantity: "+str(quant[i]))
        file.write("\n")
        
    file.write("\n")
    file.write("------------------------------------")
    
    cart.clear()
    quant.clear()

    return file

#Assigning value in dict file
main_data = dict(read_file())

#list declaration
cart = []
quant = []
