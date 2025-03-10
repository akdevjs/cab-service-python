from constants import userInfoPath, driverInfoPath
from utils import has_all_types, is_valid_email, decrypt

def isUserNameValid(username, role):
    with open(userInfoPath if role == "user" else driverInfoPath) as f:
        for item in  f.readlines():
            if(item.split(",")[0] == username):
                return {"Status":False, "Message":"username has been already used"}   
        if(len(username) < 8):
            return {"Status":False, "Message":"username must have atleast 8 characters"} 
        if(not has_all_types(username)):
            return {"Status":False, "Message":"username must have alphabets, numbers and special character"} 
    return {"Status":True}

def isValidName(name):
    if(name.isalpha() and len(name) >2):
        return {"Status":True}
    else:
        return {"Status":False, "Message":"Enter Valid Name"}
    
def isValidCarName(name):
    if(len(name) >2):
        return {"Status":True}
    else:
        return {"Status":False, "Message":"Enter Valid Name"}
    
def isPhoneNumberValid(phone_number):
    if(phone_number.isnumeric() and len(phone_number) == 11):
        return {"Status":True}
    else:
        return {"Status":False, "Message":"Enter Valid Phone number, Should be number and has 11 digits"}
    
def isValidEmail(email, role):
    if(not is_valid_email(email)):    
        return {"Status":False, "Message":"Enter Valid Email"}    
    with open(userInfoPath if role == "user" else driverInfoPath) as f:
        for item in  f.readlines():
            if(item.split(",")[3] == email):
                return {"Status":False, "Message":"email has been already used"}
    return {"Status":True}
    
def isPasswordValid(password):
    if(len(password) < 8):
        return {"Status":False, "Message":"password must have atleast 8 characters"} 
    if(not has_all_types(password)):
        return {"Status":False, "Message":"password must have alphabets, numbers and special character"} 
    return {"Status":True}

