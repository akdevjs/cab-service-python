import random
import re
import os
# Encryption of the password
def encrypt(password):
    randomChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+[{]}\\|;:'\"<.>/?"
    encrypted = ""
    for char in password:
       encrypted = encrypted + str(ord(char)) + "".join(random.choices(randomChar, k=3))        
    return "".join(random.choices(randomChar, k=2)) + encrypted +"".join(random.choices(randomChar, k=2)) 

# Decryption of the password
def decrypt(encrypted_password):
    ascii_list =list(map(int, filter(None, re.sub(r"\D{3}", ",", encrypted_password[2:-2]).split(",")))) 
    return "".join(chr(num) for num in ascii_list)

# Clearing the screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Check the string has alphabets, numbers and special characters or not
def has_all_types(s):
    return bool(re.search(r"[A-Za-z]", s)) and bool(re.search(r"\d", s)) and bool(re.search(r"[^\w\s]", s))

# Check the string has alphabets, numbers and special characters or not
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

dex = 'At97~h?115lU*100~!D97iWv115W}D100RtA49mBt50=Vu51VAZ33Y(l*?'
print(decrypt(dex))




