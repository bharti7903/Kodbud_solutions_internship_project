import random

secret = random.randint(1, 100)
count = 0 

while True:
    num = int(input("Enter your favourite number (1-100): ")) 
    count += 1
    if num > secret:
        print("Too high") 
        
    elif num < secret:
        print("Too low") 
        
    else: 
        print("Correct! you guessed it") 
        break 
    
print(f"Total attempts = {count}")