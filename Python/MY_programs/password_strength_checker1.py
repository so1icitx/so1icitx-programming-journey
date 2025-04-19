print("Password strength checker.")
password = input("Enter your password for analysis:")

def number(passw):
    return any(num.isdigit() for num in passw)

def letter(passw):
    return any(lett.isalpha() for lett in passw)

def symbol(passw):
    return any(not sym.isalnum() for sym in passw)

def capital(passw):
    return any(cap.isupper() for cap in passw)

def lower(passw):
    return any(low.islower() for low in passw)

if len(password) > 8:
    if number(password) and letter(password) and symbol(password) and capital(password) and lower(password):
        print("Strong")
    else:
        print("Weak")
else:
    print("Weak")


