def chatbot():
    print("ChatBot: Hello! I'm ChatBot 1.0 🤖. How can I assist you today?")
    print("Type 'bye' anytime to exit the conversation.")

    while True:
        user_input = input("You: ").lower()

   
        if user_input in ["bye", "exit", "quit", "goodbye"]:
            print("ChatBot: Goodbye! It was nice talking to you. 👋")
            break


        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hey there! 👋 How can I help you?")
        elif "good morning" in user_input:
            print("ChatBot: Good morning! Hope you have a productive day 🌞")
        elif "good night" in user_input:
            print("ChatBot: Good night! Sleep well 🌙")

        elif "how are you" in user_input:
            print("ChatBot: I'm doing great, thanks! How about you?")
        elif "i'm fine" in user_input or "i am fine" in user_input:
            print("ChatBot: That's great to hear! 😊")
        elif "what's up" in user_input or "sup" in user_input:
            print("ChatBot: Just chatting with you! 😄")


        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot 2.0, your virtual assistant.")
        elif "who made you" in user_input:
            print("ChatBot: I was created by a Python enthusiast!")

       
        elif "help" in user_input or "what can you do" in user_input:
            print("ChatBot: I can tell you jokes, give the current time, greet you, and have a casual chat!")
        elif "joke" in user_input:
            print("ChatBot: Why did the developer go broke? Because he used up all his cache! 😂")
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%I:%M %p")
            print(f"ChatBot: The current time is {now} 🕒")
        elif "date" in user_input:
            from datetime import datetime
            today = datetime.now().strftime("%B %d, %Y")
            print(f"ChatBot: Today's date is {today} 📅")

        elif "python" in user_input:
            print("ChatBot: Python is a popular programming language known for its simplicity and readability.")
        elif "weather" in user_input:
            print("ChatBot: I'm not connected to a weather API right now, but it's always sunny in code-land! 🌤️")

        else:
            print("ChatBot: Sorry, I didn't understand that. Can you rephrase? 🤔")

# Start the chatbot
chatbot()
