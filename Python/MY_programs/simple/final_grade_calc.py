subject = 0
sum = 0
while True:
    number = int(input("grade: "))
    if number == 0:
        break
    subject += 1
    sum += number



print(sum/subject)
