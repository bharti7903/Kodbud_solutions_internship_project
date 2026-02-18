import re

print("password must contain at least 1 number, 1 special character, 1 uppercase letter")
password = input("Enter your password: ")


length_ok = len(password) >= 8 
has_number = re.search(r"\d", password) 
has_upper = re.search(r"[a-z]", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) 

if length_ok and has_number and has_upper and has_special:
    print("Strong password!") 
    
else:
    print("Weak password!")