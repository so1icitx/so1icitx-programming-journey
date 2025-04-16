import time
import random

sentences = [
    "The cat jumped onto the soft couch quickly.",
    "She always drinks coffee before starting her day.",
    "Music helps me focus when I feel distracted.",
    "The sun disappeared behind the cloudy grey sky.",
    "Bob delivered the package before the rain started.",
    "I never eat breakfast when I wake up late.",
    "Typing fast is fun once you build the skill.",
    "We played games until the power went out.",
    "He forgot his keys at the coffee shop.",
    "I read three books during the long weekend.",
    "Her laptop died in the middle of class.",
    "The internet connection dropped during the meeting again.",
    "I like walking alone on quiet rainy nights.",
    "She smiled after finishing the final exam early.",
    "The pizza arrived cold but still tasted good.",
    "He fixed the bug after hours of debugging.",
    "Sometimes silence says more than a thousand words.",
    "We stayed up late watching old horror movies.",
    "His cat knocked over the glass of water.",
    "The teacher gave us extra time for the test."
]

text = random.choice(sentences)
start = time.time()


def wpm_calculation(txt,time_start,time_end):
    time_taken = time_end - time_start
    words = len(txt) / 5
    wpm = words / (time_taken / 60)
    return round(wpm, 2)

while True :
    print(text)
    print(f"Enter the above text below:")
    text_input = input()
    if text_input == text:
        end = time.time()
        break

wpm_final = wpm_calculation(text,start,end)
if wpm_final >= 100:
    print(f"{wpm_final} HACKER - not cool bro.....")
elif wpm_final >= 81:
    print(f"{wpm_final} ROCKET - touch some grass")
elif wpm_final >= 61:
    print(f"{wpm_final} CHEETAH - speed sigma detected")
elif wpm_final >= 41:
    print(f"{wpm_final} FOX - average")
elif wpm_final >= 21:
    print(f"{wpm_final} TURTLE - my grandam types faster")
else:
    print(f"You type so slow you dont get your own animal BOO HOO")





