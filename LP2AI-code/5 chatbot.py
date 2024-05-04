import datetime

def chatbot():
    print("Customer Service Bot: Hello! Welcome to Fictional Company's customer service. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if "hi" in user_input.lower() or "hello" in user_input.lower():
            print("Customer Service Bot: Hi! How can I help you?")
        elif "problem" in user_input.lower() or "issue" in user_input.lower():
            print("Customer Service Bot: I'm sorry to hear that. Could you please provide more details about the problem?")
        elif "thanks" in user_input.lower() or "thank you" in user_input.lower():
            print("Customer Service Bot: You're welcome! If you need further assistance, feel free to ask.")
        elif "date" in user_input.lower() or "time" in user_input.lower():
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Customer Service Bot: The current date and time is:", current_time)
        elif "bye" in user_input.lower():
            print("Customer Service Bot: Goodbye! Have a great day!")
            break
        else:
            print("Customer Service Bot: I'm sorry, I didn't understand that. Can you please rephrase?")
            
# Run the chatbot
chatbot()
