def prime_checker(number):
    is_prim = True
    if number <= 1:
        is_prim = False
    for i in range(2, number):
        if number % i == 0:
            is_prim = False
    if is_prim:
        print(f"The number {number} is a prime number")
    else:
        print(f"The number {number} is not a prime number")


n = int(input())
prime_checker(number=n)
