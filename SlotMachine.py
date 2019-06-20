#Slot Machine
'''
Slot Machine
By Damian Bocanegra
Slot Machine application for Windows command line.

How to start:
Open Windows command line and navigate to directory containing SlotMachine.py
Type command 'python SlotMachine.py'

Instructions:
You will start with 100 points and the slot machine will start running upon start up.
The slot machine will award a payout and then ask if you would like to play again.
To play again type 'Y' or 'y', typing anything else will exit the application.
If you do not have 20 points the application will exit.

Score as high as you can, good luck!

'''

import random
import time
from os import system


#Prize table
prize1 = ["CCA", "AAA"] #100 points
prize2 = ["CCB", "CBC", "AAC", "ACC", "BBB", "CAC"] #50 points
prize3 = ["CAA", "ACA", "AAB", "ABA", "BCB", "BAA", "BCC"] # 20 points
prize4 = ["CBB", "ABB", "BBC", "BBA", "BAB", "CAB", "ABC"] # 10 points
prize5 = ["ACB", "BCA", "BAC", "CBA"] #0 points

#Function determines the payout
def selectPrize(combo):
    if combo in prize1:
        return 100
    elif combo in prize2:
        return 50
    elif combo in prize3:
        return 20
    elif combo in prize4:
        return 10
    elif combo in prize5:
        return 0
    else:
        return 200

#Function animates the slot machine on the screen.
def animateSlots(r1, r2, r3, positions, score):

    spin = random.randint(0, 50)
    i = 0
    spinning = True

    pick1 = random.randint(0, (len(r1) - 1))
    pick2 = random.randint(0, (len(r2) - 1))
    pick3 = random.randint(0, (len(r3) - 1))
    
    while i < spin:
        print("Score: " + str(score))
        print("Pick 1: " + (str(r1[positions[0]])))
        print("Pick 2: " + (str(r2[positions[1]])))
        print("Pick 3: " + (str(r3[positions[2]])))

        positions[0] = (positions[0] + 1) % len(r1)
        positions[1] = (positions[1] + 1) % len(r2)
        positions[2] = (positions[2] + 1) % len(r3)
        i = i + 1
        time.sleep(.04)
        system('cls')

    while spinning:
        spinning = False
        print("Score: " + str(score))
        print("Pick 1: " + (str(r1[positions[0]])))
        print("Pick 2: " + (str(r2[positions[1]])))
        print("Pick 3: " + (str(r3[positions[2]])))
        
        if positions[0] != pick1:
            positions[0] = (positions[0] + 1) % len(r1)
            spinning = True
        if positions[1] != pick2:
            positions[1] = (positions[1] + 1) % len(r2)
            spinning = True
        if positions[2] != pick3:
            positions[2] = (positions[2] + 1) % len(r3)
            spinning = True
        time.sleep(.04)
        if spinning:
            system('cls')
        
            
    
#Main program that runs the slot machine
def main():
    system('cls')
    reelOne = ['A', 'B', 'C', 'B', 'A', 'A']
    reelTwo = ['A', 'B', 'C', 'B', 'B', 'B']
    reelThree = ['A', 'B', 'C', 'B', 'A', 'A', 'B', 'C', 'A', 'B']

    playing = True
    score = 100

    reelP1 = random.randint(0, (len(reelOne) - 1))
    reelP2 = random.randint(0, (len(reelTwo) - 1))
    reelP3 = random.randint(0, (len(reelThree) - 1))

    positions = [reelP1, reelP2, reelP3]

    while playing:
        
        animateSlots(reelOne, reelTwo, reelThree, positions, score)
        slotResult = str(reelOne[positions[0]] + reelTwo[positions[1]] + reelThree[positions[2]])

        points = selectPrize(slotResult)

        score = score + points

        system('cls')
        print("Score: " + str(score))
        print("Pick 1: " + (str(reelOne[positions[0]])))
        print("Pick 2: " + (str(reelTwo[positions[1]])))
        print("Pick 3: " + (str(reelThree[positions[2]])))

        print("You won " + str(points) + " pts")

        ans = input("Play Again? Cost: 20 points (Y/N)")
        
        if ans == 'Y' or ans == 'y':
            if score < 20:
                print("You don't have enough, Thanks for playing!")
                playing = False
            else:
                score = score - 20
                system('cls')
        else:
            print("Thanks for playing!")
            playing = False

#Function for testing and balancing payouts.
def simulation():
    reelOne = ['A', 'B', 'C', 'B', 'A', 'A']
    reelTwo = ['A', 'B', 'C', 'B', 'B', 'B']
    reelThree = ['A', 'B', 'C', 'B', 'A', 'A', 'B', 'C', 'A', 'B']

    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0

    playing = 0

    while playing < 100:
        #print("Score: " + str(score))
        pick1 = reelOne[random.randint(0, (len(reelOne) - 1))]
        pick2 = reelTwo[random.randint(0, (len(reelTwo) - 1))]
        pick3 = reelThree[random.randint(0, (len(reelThree) - 1))]

        #print("Pick 1: " + str(pick1))
        #print("Pick 2: " + str(pick2))
        #print("Pick 3: " + str(pick3))

        slotResult = str(pick1 + pick2 + pick3)

        points = selectPrize(slotResult)

        if points == 200:
            p6 = p6 + 1
        elif points == 0:
            p5 = p5 + 1
        elif points == 10:
            p4 = p4 + 1
        elif points == 20:
            p3 = p3 + 1
        elif points == 50:
            p2 = p2 + 1
        else:
            p1 = p1 + 1

        playing = playing + 1

    print("Games played: " + str(playing))
    print("Won 200 points: " + str(p6/playing))
    print("Won 100 points: " + str(p1/playing))
    print("Won 50 points: " + str(p2/playing))
    print("Won 20 points: " + str(p3/playing))
    print("Won 10 points: " + str(p4/playing))
    print("Won 0 points: " + str(p5/playing))

        

main()        

        


        


'''
Victory table:
CCC - 200

CCA - 100
AAA - 100

CCB - 50
CAC - 50
CBC - 50
AAC - 50
ACC - 50
BBB - 50

BCB - 20
BAA - 20
BCC - 20
CAA - 20
ACA - 20
AAB - 20
ABA - 20

ABB - 10
CBB - 10
BBC - 10
BBA - 10
BAB - 10
CAB - 10
ABC - 10

ACB - 0
BCA - 0
BAC - 0
CBA - 0


200 = 1/27 ~ 3.7%
100 = 2/27 ~ 7.4%
50 = 6/27 ~ 22.2%
20 = 7/27 ~ 26%
10 = 7/27 ~ 26%
0 = 4/27 ~ 14.9%


'''

