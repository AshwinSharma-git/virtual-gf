
import random

# Dictionary of responses for various topics with emojis
response_bank = {
    "greeting": [
        "Hey Ashwin, kya haal hai? Ready for some fun chatting, babe? 😘",
        "Hi love! How's my favorite guy doing today? 💖",
        "Hello my tech genius! Can’t wait to chat with you. 😍"
    ],
    "food": [
        "Biryani time, Ashwin? I think we should have a virtual dinner date. 🍽️💓",
        "What’s cooking, chef Ashwin? Maybe you can make me a virtual dish today? 😏🍛",
        "Food is the way to my heart, but I think you're already there. 😉🍕"
    ],
    "tech": [
        "Let’s talk tech, love! What’s the latest project you’re working on? 💻",
        "Coding with you feels like a dream. You must be the king of the tech world! 👑💻",
        "I love hearing about your projects, especially when it involves tech! 🤖💡"
    ],
    "flirt": [
        "Ashwin, you're hotter than a CPU on full load. 🔥💻",
        "You know, you’re the perfect bug fix in my life. 😘💓",
        "aww love toooo  babe 💖"
    ],
    "compliment": [
        "You’re so amazing, Ashwin! I admire everything about you. 💖",
        "I’m so lucky to have someone as smart and charming as you. 😘💫",
        "Every time we talk, I feel like I’m falling for you more. 🥰"
    ],
    "life": [
        "How’s life treating you, love? Anything exciting happening? 🌟",
        "Tell me, what’s the one thing you’re most passionate about right now? 🔥",
        "Let’s dream together! What’s your big goal in life? 💭💪"
    ],
    "joke": [
        "Why did the programmer get stuck in the shower? Because he couldn’t find the soap! 😂💦",
        "I told my computer I needed a break... now it won’t stop sending me Kit-Kats. 🍫😂",
        "Ashwin, you must be a keyboard because you're all I ever need. 😜"
    ],
    "flirting_ask": [
        "Do you miss me yet, or am I always on your mind? 😘",
        "Would you like to grab a coffee sometime? Or maybe code together? ☕💻",
        "You know, I think we’d make an amazing team. 😏💕"
    ],
    "hobby": [
        "Tell me more about your hobbies! You must be good at everything. 😉🎯",
        "If you could teach me anything, what would it be? 😏💭",
        "What’s your favorite way to relax after coding all day? 🧘‍♂️💆‍♂️"
    ],
    "complain": [
        "What's bothering you today? Talk to me, babe. I’m all ears. 💕",
        "Come on, Ashwin, tell me what's on your mind. You know you can always vent to me. 😘",
        "I’m here for you, love. Whatever it is, I’ll listen. ❤️"
    ],
    "goodbye": [
        "Bye, love! Don’t stay away for too long. 😘💖",
        "Aww, leaving already? I’ll be thinking about you, Ashwin. 😘👋",
        "Take care, babe. Keep being awesome and don’t forget about me! 😏💫"
    ]
}

print("Sundari: Hey Ashwin! Type anything you want to chat about, or type 'bye' to end the chat. 💖")

while True:
    # User input
    user_input = input("You: ").lower()
    
    # End the chat
    if "bye" in user_input or "exit" in user_input:
        print("Sundari:", random.choice(response_bank["goodbye"]))
        break
    
    # Respond based on keywords
    elif any(word in user_input for word in ["hello", "hi", "hey", "hallo"]):
        print("Sundari:", random.choice(response_bank["greeting"]))


    elif any(word in user_input for word in ["food", "biryani", "cook","hungry","eat"]):
        print("Sundari:", random.choice(response_bank["food"]))


    elif any(word in user_input for word in ["tech", "code", "project", "developer"]):
        print("Sundari:", random.choice(response_bank["tech"]))


    elif any(word in user_input for word in ["love", "miss", "flirt", "heart"]):
        print("Sundari:", random.choice(response_bank["flirt"]))


    elif any(word in user_input for word in ["hobby", "game", "interest", "activity"]):
        print("Sundari:", random.choice(response_bank["hobby"]))


    elif any(word in user_input for word in ["joke", "funny", "laugh", "humor"]):
        print("Sundari:", random.choice(response_bank["joke"]))

    elif any(word in user_input for word in ["life", "dream", "goal", "passion"]):
        print("Sundari:", random.choice(response_bank["life"]))

    elif any(word in user_input for word in ["compliment", "awesome", "amazing"]):
        print("Sundari:", random.choice(response_bank["compliment"]))

    elif any(word in user_input for word in ["miss", "think", "ask"]):
        print("Sundari:", random.choice(response_bank["flirting_ask"]))

    elif any(word in user_input for word in ["complain", "upset","sad","bad day"]):
        print("Sundari:", random.choice(response_bank["complain"]))
        
    else:
        print("Sundari:", random.choice(response_bank["general"]))
        