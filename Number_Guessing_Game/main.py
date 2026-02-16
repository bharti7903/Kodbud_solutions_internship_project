num = int(input("Enter your favourite number: ")) 
print("Number must be between 1 to 100")

count = 0
for i in range(0, 101) :
    if num > i :
        print("Too high") 
        count += 1
        
    elif num < i :
        print("Too low") 
        count += 1
        
    elif num == i :
        print(i) 
        count += 1 
    print(count)
    