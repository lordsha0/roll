#!/usr/bin/python3
 
import sys
import random

def roll_dice(max):
    currentRoll = random.randint(1,max)
    message = "d{0}: {1}".format(max, currentRoll)
    if max == 20:
        if currentRoll == 1 or currentRoll == max:
            message = "d{0}: Nat {1}".format(max, currentRoll)
    return message

try:
    if sys.argv[1] == 'd4' or sys.argv[1] == '4':
        print(roll_dice(4))
    elif sys.argv[1] == 'd6' or sys.argv[1] == '6':
        print(roll_dice(6))
    elif sys.argv[1] == 'd8' or sys.argv[1] == '8':
        print(roll_dice(8))
    elif sys.argv[1] == 'd10' or sys.argv[1] == '10':
        print(roll_dice(10))
    elif sys.argv[1] == 'd12' or sys.argv[1] == '12':
        print(roll_dice(12))
    elif sys.argv[1] == 'd20' or sys.argv[1] == '20':
        print(roll_dice(20))
    elif sys.argv[1] == '-help' or sys.argv[1] == '--help' or sys.argv[1] == 'help':
        print("roll [option]")
        print("Options:")
        print("d4: rolls a die 4")
        print("d6: rolls a die 6")
        print("d8: rolls a die 8")
        print("d10: rolls a die 10")
        print("d12: rolls a die 12")
        print("d20: rolls a die 20")
        print("help: shows the options")
    else:
        print("Not a valid die to roll")
except:
    print("Please insert a die to roll")