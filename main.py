from utils import clear_console, encrypt, decrypt
from constants import userInfoPath,driverInfoPath
from validations import isCarModelValid, isCarNumberValid, isConfrimPasswordValid, isUserNameValid, isPhoneNumberValid, isValidEmail, isValidName, isPasswordValid, isValidCarName

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

def intro_screen(intro_text=""):
    print("---------------------------------------------")
    print("|    Welcom the City to City cab service    |")
    print("---------------------------------------------\n")
    print(intro_text)

def new_screen(fx):
    def mfx(*args, **kwargs):
        clear_console()
        intro_screen()
        result = fx(*args, **kwargs)
        return result
    return mfx

@new_screen
def getValue(key, validate, error, *args, **kwargs):
    print("Register your Account")
    if(error):
        print(f"*** {error} ***")
    value = input(f"Enter the {" ".join(key.split("_")).capitalize()}: ")
    validation = validate(value, *args, **kwargs)
    print(validation["Status"])
    if(validation["Status"]):
            return value
    else:
       error= validation["Message"] 
       return getValue(key, validate, error, *args, **kwargs)

def action_selector(initail_statement, *opts):
    generated_opts = "\n".join([f"({index+1}) {item}" for index, item in enumerate(opts)])
    content = f"{initail_statement}\n{generated_opts}\nNote: Enter \"1\"or \"2\" etc otherwise the input will be invalid\nEnter Answer :"
    return input(content)

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

@new_screen   
def add_to_file(role, data):
    payload = ""
    for index, (key, val) in enumerate(data.items()):
        if(key!= "confrim_password"):
            print(f"{" ".join(key.split("_")).capitalize()} : {val}")
        if (index == 0):
            payload += f"{val}"
        elif(key == "password"):
            pass
        else:
            payload += f",{val}"
    action = action_selector("Do you confrim Registration? ", "Yes", "No")
    if (action == "1"):
        with open(userInfoPath if role == "user" else driverInfoPath, "a") as f:
            f.write(f"{payload}\n")
    
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

        driver["username"] = getValue("username", isUserNameValid, None, role)
        driver["first_name"]= getValue("first_name", isValidName, None)
        driver["last_name"]= getValue("last_name", isValidName, None)
        driver["email"] = getValue("email", isValidEmail, None, role)
        driver["phone"] = getValue("phone", isPhoneNumberValid, None)
        driver["password"] = getValue("password", isPasswordValid, None)
        driver["confrim_password"] = encrypt(getValue("confrim_password", isConfrimPasswordValid, None, driver["password"]))
        driver["car_name"] = getValue("car_name", isValidCarName, None)
        driver["car_model"] = getValue("car_model", isCarModelValid, None)
        driver["car_number"] = getValue("car_number", isCarNumberValid, None)

        # Registering Car has AC or not   
        clear_console()
        intro_screen()
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


        add_to_file(role, driver)        
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

        user["username"] = getValue("username", isUserNameValid, None, role)
        user["first_name"]= getValue("first_name", isValidName, None)
        user["last_name"]= getValue("last_name", isValidName, None)
        user["email"] = getValue("email", isValidEmail, None, role)
        user["phone"] = getValue("phone", isPhoneNumberValid, None)
        user["password"] = getValue("password", isPasswordValid, None)
        user["confrim_password"] = encrypt(getValue("confrim_password", isConfrimPasswordValid, None, user["password"]))
                
        add_to_file(role, user) 


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