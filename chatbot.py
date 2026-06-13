from datetime import datetime

def bot_reply(message):
    message = message.lower()

    if message in ["hi", "hello", "hey"]:
        return " Hello! Nice to meet you."

    elif "how are you" in message:
        return " I'm doing great and ready to help!"
    
    elif "can i ask you a question" in message:
        return "Yes, please.I'm always ready to help!"
    
    elif "good morning" in message:
        return "Good Morning! Hope you are having a good day."
    
    elif "how are you" in message:
        return " I'm doing great and ready to help!"

    elif "your name" in message:
        return " I'm SmartBot, a simple rule-based AI chatbot."
    
    elif "who created you" in message:
        return " I am created by a python developer named Vardan."
    
    elif "what can you do" in message:
        return " I am a chatbot that basically responds to the predefined commands."
    
    elif "what is ai" in message:
        return " AI stands for Artificial Intelligence, enabling machines to mimic human intelligence."

    elif "what is internship" in message:
        return " Internships help students gain practical industry experience and develop professional skills."

    elif "what is python" in message:
        return " Python is one of the most popular programming languages for AI, Machine Learning, and Data Science."

    elif "thank you" in message or "thanks" in message:
        return " You're welcome! Happy to help."

    else:
        return " Sorry, I don't understand that. Please try another question."

# Chatbot Header
print("=" * 60)
print("🤖 SMARTBOT - RULE BASED CHATBOT")
print("🚀 Built using Python, Control Flow & Decision Making")
print("=" * 60)
print("\nType 'exit/bye/quit' to end the conversation.\n")

# Continuous Chat Loop
while True:
    user_input = input("👤 You: ")

    if user_input.lower() in ["exit", "bye", "quit"]:
        print(f"🤖 SmartBot [{datetime.now().strftime('%H:%M:%S')}]:")
        print("👋 Goodbye! Thank you for chatting with me.")
        print("\nSession Ended Successfully.")
        break

    response = bot_reply(user_input)

    print(f"🤖 SmartBot [{datetime.now().strftime('%H:%M:%S')}]:")
    print(response)
    print("-" * 60)