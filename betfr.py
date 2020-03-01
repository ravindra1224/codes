import random
import os
import math
from typing import Any, Union


def main():

    generate_lotto_numbers(100)


def clear():
    os.system('clear')


def pwr_ball():
    x = random.randint(1, 26)

    return x


def times_to_win(args, x):
    # Call system clear
    clear()
    # Keep track of count
    count = 1
    # Infinite loop
    while True:
        clear()
        # Display goal until user presses Enter
        print("Goal Lottery Numbers: " + str(args) + " Power Ball: " + str(x))

        # Grab five non-repeating random numbers from x to y
        lottery_num = random.sample(range(13, 58, 1), 9)

        # Add Power Ball
        power_ball = pwr_ball()

        # Print out current attempt
        print("Attempt # " + str(count) + " - " + str(lottery_num) + " - Power Ball " + str(power_ball))

        # Test if the amount of like numbers = 5
        if len(set(lottery_num) & set(args)) == 9 and power_ball == x:
            print("It took " + str(count) + " times to win the lottery!")
            # Exit when found!
            exit()
        else:
            count += 1


def generate_lotto_numbers(amount):
    l=[]
    k=[]
    sm=0
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    a11 = 0
    a12 = 0
    a13 = 0
    a14 = 0
    correct_amount = amount + 1
	# Display lotto Numbers the ammount of times listed in the variable
    for x in range(1, correct_amount):
        p=random.sample(range(1, 50, 1), 9)
        l.append(p[0:6])
        k=l[x-1]


        print('Lottery Numbers: ' + str(p) + ' - Power Ball: ' + str(pwr_ball()))

        print('sum of first 6 numbers is',sum(k))
        if(21<=sum(k)<=74):
            a1+=1
        elif(75<=sum(k)<=100):
            a2+=1
        elif (101 <= sum(k) <= 110):
            a3 += 1
        elif (111 <= sum(k) <= 120):
            a4 += 1
        elif (121 <= sum(k) <= 130):
            a5 += 1
        elif (131 <= sum(k) <= 140):
            a6+= 1
        elif (141 <= sum(k) <= 150):
            a7 += 1
        elif (151 <= sum(k) <= 160):
            a8 += 1
        elif (161 <= sum(k) <= 170):
            a9 += 1
        elif (171 <= sum(k) <= 180):
            a10 += 1
        elif (181 <= sum(k) <= 190):
            a11 += 1
        elif (191 <= sum(k) <= 200):
            a12 += 1
        elif (201 <= sum(k) <= 210):
            a13 += 1
        elif (211 <= sum(k) <= 279):
            a14 += 1
    print('1r',a1)
    print('2r',a2)
    print('3r',a3)
    print('4r',a4)
    print('5r',a5)
    print('6r',a6)
    print('7r', a7)
    print('8r', a8)
    print('9r', a9)
    print('10r', a10)
    print('11r', a11)
    print('12r', a12)
    print('13r', a13)
    print('14r', a14)



main()
