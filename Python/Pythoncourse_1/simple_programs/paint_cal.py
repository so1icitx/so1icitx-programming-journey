import math

def paint_calc(height, width, cover):
    total = (height * width) / 5
    print(f"You'll need {math.ceil(total)} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)
