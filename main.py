from utils import clear_console, encrypt, decrypt
from constants import userInfoPath,driverInfoPath
from validations import isUserNameValid, isPhoneNumberValid, isValidEmail, isValidName, isPasswordValid, isValidCarName

"""
1. Are you driver or Passenger:
     (1) Diver
     (2) Passenger

2. Login/Register
    1.Login
    2.Register

3. Login
    input -> username
    input -> password

2. Register(Driver)
    input -> Username
    input -> First Name
    input -> Last Name
    input -> Email
    input -> Phone number
    input -> Password
    input -> Confrim Password
    input -> Car Name
    input -> Car Model
    input -> Car Number
    input -> is it AC?
    input -> Category(Mini, Sedan, Bike, etc.)

1. Register (User)
    input -> Username
    input -> First Name
    input -> Last Name
    input -> Email
    input -> Phone Number
    input -> Password
    input -> Confirm Password
    
"""

authenticated_driver = {
            "username":None,
            "first_name":None,
            "last_name":None,
            "email":None,
            "phone":None,
            "password":None,
            "car_name":None,
            "car_model":None,
            "car_number":None,
            "car_has_ac":None,
            "category":None
        } 
authenticated_user = {
            "username":None,
            "first_name":None,
            "last_name":None,
            "email":None,
            "phone":None,
            "password":None,
            
        } 

def intro_screen():
    print("---------------------------------------------")
    print("|    Welcom the City to City cab service    |")
    print("---------------------------------------------")



def auth(role):
    clear_console()
    intro_screen()
    while(True):
        login_or_register = action_selector("Want to Login or Register", "Login", "Register")
        if(login_or_register == "1"):
            login(role)
            break
        elif(login_or_register == "2"):
            register(role)
            break
        else:
            clear_console()
            intro_screen()
            print("\n*** You have added invalid input kindly try again!! ***\n")
 

def login(role):
    clear_console()
    intro_screen()
    print("Login")
    expected_data = ""          
    while(True):
        found = False
        username = input("Enter the Username: ") 
        with open(userInfoPath if role == "user" else driverInfoPath) as f:
            for item in  f.readlines():
                if(item.split(",")[0] == username):
                    found = True 
                    expected_data=item.split(",")
                    if(role != 'driver'):
                        expected_data[len(expected_data)-1] =expected_data[len(expected_data)-1][0:-1] 
                    break
                    
        if(not found):
            clear_console()
            intro_screen()
            print("Login")
            print(f"\n*** Username not registered ***\n")
        else:
            break

    clear_console()
    intro_screen()
    print("Login")
    while(True):
        password = input("Enter the Password: ") 
        if(password == decrypt(expected_data[5])):
            clear_console()
            intro_screen()
            print("Successfully Loggedin!!")
            print(f"Welcome {expected_data[1]}, following is your saved information:\n")
            for index, key in enumerate(authenticated_driver if role == "driver" else authenticated_user):
                (authenticated_driver if role == "driver" else authenticated_user)[key] = expected_data[index]
                if(key != "password"):
                    print(f"{" ".join(key.split("_")).capitalize()} : {(authenticated_driver if role == "driver" else authenticated_user)[key]}")
            break
        else:
            clear_console()
            intro_screen()
            print("Login")
            print("\n*** Invalid Password***\n")


def register(role):
    if(role == "driver"):
        driver={
            "username":None,
            "first_name":None,
            "last_name":None,
            "email":None,
            "phone":None,
            "password":None,
            "confrim_password":None,
            "car_name":None,
            "car_model":None,
            "car_number":None,
            "car_has_ac":None,
            "category":None
        }     

        # Registering Username   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            username = input("Enter the username: ")
            validation = isUserNameValid(username, role)
            if(validation["Status"]):
                driver["username"] = username
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering First Name   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            first_name = input("Enter the First Name: ")
            validation = isValidName(first_name)
            if(validation["Status"]):
                driver["first_name"] = first_name
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Last Name   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            last_name = input("Enter the Last Name: ")
            validation = isValidName(last_name)
            if(validation["Status"]):
                driver["last_name"] = last_name
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Email   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            email = input("Enter the Email: ")
            validation = isValidEmail(email, role)
            if(validation["Status"]):
                driver["email"] = email
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Phone   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            phone = input("Enter the Phone Number: ")
            validation = isPhoneNumberValid(phone)
            if(validation["Status"]):
                driver["phone"] = phone
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Password   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            password = input("Enter the Password: ")
            validation = isPasswordValid(password)
            if(validation["Status"]):
                driver["password"] = password
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Confriming Password   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            confrim_password = input("Enter the Password Again to Confrim: ")
            validation = isPasswordValid(confrim_password)
            if(driver["password"] == confrim_password):
                driver["confrim_password"] = encrypt(confrim_password)
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** Passwords doesn't match ***\n")
                
        # Registering Car Name   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            car_name = input("Enter the Car Name: ")
            validation = isValidCarName(car_name)
            if(validation["Status"]):
                driver["car_name"] = car_name
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Car Model   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            car_model = input("Enter the Car Model: ")
            if(car_model.isnumeric() and len(car_model) == 4):
                driver["car_model"] = car_model
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** enter the valid model of car like YYYY ***\n")

        # Registering Car Number   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            car_number = input("Enter the Car Number: ")
            if(car_model.isalnum() and len(car_number) > 3):
                driver["car_number"] = car_number
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** enter the valid car number like ABC123 ***\n")
        print(driver)

        # Registering Car has AC or not   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            car_has_ac = action_selector("Does your car has functional AC?: ", "Yes", "No")
            if(car_has_ac == "1" or car_has_ac =="2"):
                driver["car_has_ac"] = not bool(int(car_has_ac)-1)
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** Invalid input ***\n")
        print(driver)

        # Registering Car Category   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            category = action_selector("Which one of the following categories your car fall in?: ", "Mini", "Sudan", "Bike")
            if(category == "1"):
                driver["category"] = "mini"
                break
            elif(category == "2"):
                driver["category"] = "sudan"
                break
            elif(category == "3"):
                driver["category"] = "bike"
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** Invalid input ***\n")
        data = f"{driver["username"]},{driver["first_name"]},{driver["last_name"]},{driver["email"]},{driver["phone"]},{driver["confrim_password"]},{driver["car_name"]},{driver["car_model"]},{driver["car_number"]},{int(driver["car_has_ac"])},{driver["category"]}"

        clear_console()
        intro_screen()
        while(True):
            print("\n** Following are the Values you have entered **\n")
            for key,val in driver.items():
                if(key != "confrim_password"):
                    print(f"{" ".join(key.split("_")).capitalize()} : {val}")
            action = action_selector("Do you confrim Registration? ", "Yes", "No")
            if(action == "1"):
                with open(driverInfoPath, "a") as f:
                    f.write(data + "\n")
            auth(role)
            
        
    else:
        user={
            "username":None,
            "first_name":None,
            "last_name":None,
            "email":None,
            "phone":None,
            "password":None,
            "confrim_password":None,
        }    
                # Registering Username   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            username = input("Enter the username: ")
            validation = isUserNameValid(username, role)
            if(validation["Status"]):
                user["username"] = username
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering First Name   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            first_name = input("Enter the First Name: ")
            validation = isValidName(first_name)
            if(validation["Status"]):
                user["first_name"] = first_name
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Last Name   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            last_name = input("Enter the Last Name: ")
            validation = isValidName(last_name)
            if(validation["Status"]):
                user["last_name"] = last_name
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Email   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            email = input("Enter the Email: ")
            validation = isValidEmail(email, role)
            if(validation["Status"]):
                user["email"] = email
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Phone   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            phone = input("Enter the Phone Number: ")
            validation = isPhoneNumberValid(phone)
            if(validation["Status"]):
                user["phone"] = phone
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Registering Password   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            password = input("Enter the Password: ")
            validation = isPasswordValid(password)
            if(validation["Status"]):
                user["password"] = password
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** {validation["Message"]} ***\n")

        # Confriming Password   
        clear_console()
        intro_screen()
        print("Register your account")
        while(True):
            confrim_password = input("Enter the Password Again to Confrim: ")
            validation = isPasswordValid(confrim_password)
            if(user["password"] == confrim_password):
                user["confrim_password"] = encrypt(confrim_password)
                break
            else:
                clear_console()
                intro_screen()
                print(f"\n*** Passwords doesn't match ***\n")
        
        data = f"{user["username"]},{user["first_name"]},{user["last_name"]},{user["email"]},{user["phone"]},{user["confrim_password"]}"

        clear_console()
        intro_screen()
        while(True):
            print("\n** Following are the Values you have entered **\n")
            for key,val in user.items():
                if(key != "confrim_password"):
                    print(f"{" ".join(key.split("_")).capitalize()} : {val}")
            action = action_selector("Do you confrim Registration? ", "Yes", "No")
            if(action == "1"):
                print(data)
                with open(userInfoPath, "a") as f:
                    f.write(data + "\n")
            auth(role)

def action_selector(initail_statement, *opts):
    generated_opts = "\n".join([f"({index+1}) {item}" for index, item in enumerate(opts)])
    content = f"{initail_statement}\n{generated_opts}\nNote: Enter \"1\"or \"2\" etc otherwise the input will be invalid\nEnter Answer :"
    return input(content)


def select_role():
    clear_console()
    intro_screen()
    while(True):
        user_answer = action_selector("Select The role", "Driver", "Passenger")
        if(user_answer == "1"):
            auth("driver")
            break
        elif(user_answer == "2"):
            auth("user")
            break
        else:
            clear_console()
            intro_screen()
            print("\n*** You have added invalid input kindly try again!! ***\n")


select_role()