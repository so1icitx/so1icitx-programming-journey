import time

def is_pass_strong(password1):

    print("[*] Checking password strength....")
    time.sleep(2)

    print("[*] bee.... boop....")
    time.sleep(2)

    if len(password) < 8:
        print("[!] Your password is weak ,it must contain at least 8 characters!")
        return False

    print("[*] Finalizing......")
    time.sleep(4)

    if password1.isupper() or password1.islower():
        print("[!] Your password is invalid, it should contain at least one upper/lower case letter")
        return False

    print("[*] Nearly there....")
    time.sleep(2.7)

    if password1.isalpha() or password1.isdigit():
        print("[!] Your password is weak, it must contain at least one letter and one number")
        return False

    print(f"[OK] the password: {password} is a valid password\nWelcome user!")
    return True

print("Welcome to the Password Validator")

while True:
    password = input("Enter a password: ")
    if is_pass_strong(password):
        break




