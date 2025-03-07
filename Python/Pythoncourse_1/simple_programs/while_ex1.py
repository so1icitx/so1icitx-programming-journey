name = input("Enter your name: ").capitalize()


while name == "":
    print("[!] you did not enter a name!")
    name = input("Enter your name: ").capitalize()

print(f"[*] Hello {name}!")
