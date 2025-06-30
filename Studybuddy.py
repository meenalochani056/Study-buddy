# Study-buddy
Pomodoro timer with motivational quotes in python 
import time
import random

quotes = [
    "Believe in yourself 💪",
    "You can do hard things 🌟",
    "Push through the discomfort 🚀",
    "Every step counts 🧠",
    "Keep going, future engineer 👩‍💻"
]

def pomodoro_session():
    print("\n🟢 Starting 25-minute study session... Stay focused!\n")
    for i in range(5):
        print(f"Minute {i+1}...")
        time.sleep(1)
    print("\n⏸️ Time for a 5-minute break! Stretch or relax...")
    time.sleep(2)

def start_study_buddy():
    session_count = 0
    print("👋 Welcome to Study Buddy!\n")
    while True:
        choice = input("Start a new session? (yes/no): ").lower()
        if choice == "yes":
            pomodoro_session()
            session_count += 1
            print(f"✅ You've completed {session_count} session(s) today.")
            print("💡 Motivational Quote:", random.choice(quotes), "\n")
        elif choice == "no":
            print(f"👋 You completed {session_count} session(s) today. Goodbye!")
            break
        else:
            print("Please type 'yes' or 'no'.")

start_study_buddy()
