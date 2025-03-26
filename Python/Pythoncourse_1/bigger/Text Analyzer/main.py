print("[*] Welcome to the SIGMA text analyzer!!")
ece = input("[!] Enter your text: ")
positive_numbers = {"happy", "great", "awesome", "good", "excellent", "wonderful", "amazing", "beautiful", "love", "joy", "fantastic", "perfect", "nice", "lovely", "exciting", "brilliant", "super", "cool", "fun", "glad", "positive", "success", "win", "cheerful", "delight", "pleasure", "hope"}
negative_numbers = {"sad", "bad", "terrible", "awful", "horrible", "depressing", "angry", "hate", "miserable", "poor", "dreadful", "pain", "sucks", "stupid", "ugly", "boring", "annoying", "mad", "furious", "fail", "negative", "stress", "anxiety", "fear", "disappoint", "upset", "hurt"}

def text_check(text):
    if text == '':
        print(f"[!] ERROR no text provided exiting.....")
        return False
    else:
        return True

def word_count(text):
    words = text.split()
    count = len(words)
    print(f"Word Counter: {count}")

def mood_check(text, pos, neg):
    pos_count = 0
    neg_count = 0
    text = text.lower()
    words = text.split()
    for i in words:
        i = i.lower()
        if i in pos:
            pos_count += 1
        elif i in neg:
            neg_count += 1
    if pos_count > neg_count:
        print(f"The text is Positive! ")
    elif neg_count > pos_count:
        print(f"The text is Negative! ")
    else:
        print(f"The text is Neutral.. ")

def text_stats(text):
    space_count = 0
    letter_count = 0
    digit_count = 0
    text.lower()
    for i in text:
        if i == " ":
            space_count += 1
        elif i.isalpha():
            letter_count += 1
        elif i.isdigit():
            digit_count += 1

    print(f"Spaces: {space_count}\nLetters: {letter_count}\nDigits: {digit_count}")

def top_3_words(text):
    text = text.split()
    text.sort(key=len, reverse=True)
    for i in range(1, 4):
        print(f"{i}: {text[i]}, length: {len(text[i])}")



## More to come (SOON)


while True:
    if text_check(ece):
        print(f"\n=== Menu ===\n! - Count Words\n2 - Mood Check\n 3 - Text Stats\n4- Top 3 Longest Words")
        choice = int(input("Pick a choice: "))
        match choice:
            case 1:
                word_count(ece)
            case 2:
                mood_check(ece, positive_numbers, negative_numbers)
            case 3:
                text_stats(ece)
            case 4:
                top_3_words(ece)
            case _:
                print("[!] ERROR, try again!")
    else:
        break


