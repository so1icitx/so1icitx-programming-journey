from art import logo

play = True
while play:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    def caesar(text3, shift3, direction3):
        global play
        sigma_text = ""
        if direction3 == "encode":
            gona_encrypt = True
        elif direction3 == "decode":
            gona_encrypt = False

        for i in range(len(text3)):
            char = text3[i]
            if char in alphabet:
                position = alphabet.index(char)
                if gona_encrypt:
                    new_position = position + shift3
                else:
                    new_position = position - shift3
                new_letter = alphabet[new_position]
                sigma_text += new_letter
            else:
                sigma_text += char

        if gona_encrypt:
            print(f"The encrypted code is {sigma_text}")
        else:
            print(f"The decrypted code is {sigma_text}")

        print("Do you want to restart the cipher program?, 'yes' or 'no' ")
        decision = input()
        if decision == "yes":
            play = True
        else:
            play = False

    caesar(text, shift, direction)





#my first try at this AHHAHAHAH

"""
user_text = []
places_text = []
encrypted_text = []

def encrypt (text1, shift1):
    text_length = len(text1)
    for i in range(text_length):
        user_text.append(text1[i])
        places_text.append(alphabet.index(text1[i])+ shift1)
    for i in range(len(places_text)):
        encrypted_text.append(alphabet[places_text[i]])
    encrypted_string = ''.join(encrypted_text)
    print(f"The encode text is: {encrypted_string}")
"""
#my first try ends here , pls don't judge i was just trying smth

#i did this then thought of a cleaner way pt2
"""
def encrypt(text1, shift1):
    encrypted_text = ""
    for i in range(len(text1)):
        position = alphabet.index(text1[i]) + shift1
        new_letter = alphabet[position]
        encrypted_text += new_letter
    print(encrypted_text)

def decrypt(text2, shift2):
    decrypted_text = ""
    for i in range(len(text2)):
        position = alphabet.index(text2[i]) - shift2
        new_letter = alphabet[position]
        decrypted_text += new_letter
    print(decrypted_text)

if direction ==  "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
"""
#it ends here
