contact_dict = {} 

print("\n1. Add Contact") 
print("2. Search Contact") 
print("3. Delete Contact") 
print("4. show contact detailed") 
print("5. exit") 

choose = int(input("Enter your number: "))

while True: 
    if choose == 1 :
        name = input("Enter name: ") 
        number = input("Enter number: ") 
        
        contact_dict[name] = number 
        print("contact Added!") 
        
    elif choose == 2 :
        name = input("Enter to search name: ")  
        if name in contact_dict :
            print("number: ",  contact_dict[name]) 
            
        else :
            print("Contact not found!")
        
    elif choose == 3 :
        name = input("Enter your name: ") 
        if name in contact_dict:
            del contact_dict[name] 
            print("contact deleted")
            
        else :
            print("Contact not found!") 
            
    elif choose == 4 : 
        print("Contact number: ", contact_dict) 
        
    elif choose == 5:
        
        
        print("Good bye...!") 
        
    else :
        print("invalid choice!")
        
        
    