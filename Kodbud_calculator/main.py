try:
    a = int(input("Enter your first number : ")) 
    b = int(input("Enter your second number: ")) 
    
    print("what kind of operation do you want to perform. if addition press + n\if subtraction press - n\if division press / n\if multiplication press * ")
    o = input("Enter your operation: ") 
    match o:
        case "+":
            print(f"The result = {a+b} ") 
            
        case "-":
            print(f"The result = {a-b} ") 
            
        case "/": 
            print(f"The result = {a/b} ") 
            
        case "*":
            print(f"The result = {a*b} ")  
            
        case default: 
            print(f"There was an error")
            
        
except :
    print("Enter valid value of a and b")