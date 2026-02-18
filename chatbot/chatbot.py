print("chatbot: Hello! Type 'bye' to exit.") 

while True:
    user = input("You: ").lower() 
    
    if user in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! How can I help you?")
        
    elif "name" in user:
        print("Chatbot: I am a simple python chatbot.") 
        
    elif "weather" in user:
        print("Chatbot: I cannot check weather yet!") 
        
    elif "help" in user:
        print("Chatbot: You can ask about my name or say hello.")
        
    elif user == "bye":
        print("Chatbot: Goodbye!") 
        break 
    
    else:
        print("Chatbot: Sorry, I didn't understand")
    