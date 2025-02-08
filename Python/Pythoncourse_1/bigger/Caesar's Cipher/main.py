from art import logo

play = True
while play:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26  

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
                    new_position = (position + shift3) % 26  
                else:
                    new_position = (position - shift3) % 26  
                new_letter = alphabet[new_position]
                sigma_text += new_letter
            else:
                sigma_text += char

        if gona_encrypt:
            print(f"The encrypted code is {sigma_text}")
        else:
            print(f"The decrypted code is {sigma_text}")

        decision = input("Do you want to restart the cipher program? Type 'yes' or 'no':\n").lower()
        if decision == "yes":
            play = True
        else:
            play = False

    caesar(text, shift, direction)
