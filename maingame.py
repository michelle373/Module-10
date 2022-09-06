# setting up global variables
import random
from typing import List

import globalvariables

import numpy as np
import time

#result2 = globalvariables.rand75()
#print(result2)
# things the pilot needs to gather
def setup():
    global shipFuel
    global mineral
    global shipFuelMax
    global mineralMax


shipFuel = 0
mineral = 0
shipFuelMax = 2000
mineralMax = 50


def shipFlight():
    if shipFuel <= shipFuelMax:
        print('You have enough fuel for take off.')
    else:
        print('You need ', shipFuelMax, ' for take off.')


# in the pilot inventory
# def inventory():
#    global mineralCount
#    global fuelGal


mineralCount = 0
fuelGal = 0


# def character():
#    inventory(mineralCount)
#    inventory(fuelGal)


# posible encounter with the villager
def villager():
    global npcName
    global responses


npcName = 'Sasha'
responses = ['Hello, who are you?!', 'I can help you find what your looking for.',
             'You do not seem like good company, I do not want to join you']


def villagerHostileTakeover():
    fight = ['You win!', 'You lost the fight!']
    return random.choice(fight)


def villagerInventory():
    global villagerMineral
    global villagerFuel


villagerMineral = 50
villagerFuel = 2000


def trekSashaHelpful():
    # inventory.mineralCount
    print("You reveal you need", shipFuelMax, 'gallons in order to leave this planet.')
    print(npcName, ": We need ", villagerMineral, 'minerals')
    print("I have", globalvariables.mineralCount, 'minerals')
    print(npcName, "Great we only need to find a few more.\nI'll take you to our council leaders afterwards.")
    print(npcName, "takes you to a cave where you find a cave with a plentiful amount of minerals.")
    print('You are able to mine 60 more minerals')
    globalvariables.mineralCount = globalvariables.mineralCount + 60
    print(globalvariables.mineralCount)
    returnToCivialization()


# mineralCount = mineralCount + 60
#print(mineralCount)


def returnToCivialization():
    print("You return to the villager's civilization")
    print("You show the leader how many minerals you have")
    print("Hello I have", globalvariables.mineralCount, "minerals")
    print("Council leaders are so impressed")
    print("You trade the", globalvariables.mineralCount, "minerals in exchange for their fuel")
    print("Which is", villagerFuel)
    print("You are now able to get off this planet.")
    print("Council leaders agree a trading relationship.")
    print("You accomplished all your goals. Thank you for playing")


def trekSashaLessHelpful():
    print("You reveal you need", shipFuelMax, 'gallons in order to leave this planet.')
    print(npcName, ": We need ", villagerMineral, 'minerals')
    print("I have", globalvariables.mineralCount, 'minerals')
    print(npcName, "takes you to a cave where you find a cave with a plentiful amount of minerals.")
    print('You are able to mine 60 more minerals')
    globalvariables.mineralCount = globalvariables.mineralCount + 60
    print("You now have", globalvariables.mineralCount)
    time.sleep(2.5)
    print("You are on your way back to civilization.")
    print("You've been walking for a while.\nYou lose Sasha, most likely because she doesn't trust you.")
    time.sleep(2.5)
    print("You come across a dangerous preditor.\nYou take a step back.")
    time.sleep(2.5)
    print("There a snap of a twig as you step back")
    time.sleep(3.5)
    print("Now is the moment.\nDo you decide to run or fight this preditor? Run / Fight")
    globalvariables.ans5 = input(">>")
    if globalvariables.ans5 in globalvariables.answerRun:
        if globalvariables.result2 in [1]:
            print("You were able to get away!")
            returnToCivializationWithoutSahsa()
        elif globalvariables.result2 in [0]:
            print("You were not able to get away. Game Over!")
    elif globalvariables.ans5 in globalvariables.answerFight:
        if globalvariables.result2 in [1]:
            print("You won the fight")
            returnToCivializationWithoutSahsa()
        elif globalvariables.result2 in [0]:
            print("You lost the fight. You died. Game Over!")
    else:
        print("\nYou typed the wrong input. Try again!")

def returnToCivializationWithoutSahsa():
    print("You return to the villager's civilization")
    print("You show the leader how many minerals you have")
    print("Hello I have", globalvariables.mineralCount, "minerals")
    print("Council leaders notice you don't have Sasha.")
    print("Council Member: We've heard what you did with one of our own")
    print("Council Member: We have heard of your perils.")
    print("Council Member: We will deliberate and we will let you know if we device to have a trading relation")
    time.sleep(3.5)
    if globalvariables.result2 in [1]:
        print("Council Member: We have decided to help you")
        print("Council Member: We will give you the fuel you need as long as you give us the minerals.")
        print("Council Member: We are happy to establish a trading relation.")
        print("You accomplished all your goals. Thank you for playing")

    else:
        print("Council Member: We have decided to help you get off this planet")
        print("Council Member: You will online get the fuel you need and we better not see the likes of you again!")
        print("You part of your goals. Thank you for playing")



def madeContact():
    print("\nYou make contact.\nYou learn that they are willing to make an exchange.")
    time.sleep(2.5)
    print("\nIn order to strike the best agreement possible you have to weight your options carefully.")
    time.sleep(2.5)
    print("\nThe locals need minerals, you need fuel, and you want a lucrative trade to be established. ")
    time.sleep(2.5)
    print("A villager greats you.")
    time.sleep(2.5)
    print("Vilager: Hello my names is", npcName)
    print(npcName, ': ', responses[1])
    print("Do you take the help or do you instead offer to help them?")
    print("Take help / Offer help")
    globalvariables.ans4 = input(">>")


# result4 = globalvariables.ans4()


# b = ans4
# ['Take help', 'take help', 'Offer help', 'offer help']

answerShip = ["Ship", "ship"]
answerExplore = ["Explore", "explore"]
answerRiver = ["River", "river"]
answerApproach = ["Approach", "approach"]
answerHostage = ["Hostage", "hostage"]
answerLand = ["Land", "land"]

# back ground setting
print("""
Your and intergalactic space pilot who is trying to prove yourself to your superiors.
You don't have much experience but you crash land on and unknown planet. Do your first
run a diagnosis check on the ship or explore the surrounding area? (Ship / Explore)
""")

ans1 = input(">>")

if ans1 in answerShip:
    print("\nYou run a diagnosis check and learn that you ship's fuel is at, ", shipFuel, 'gallons.\nYou need at least',
          shipFuelMax, 'gallons to get off this planet')
    fuelGal = 0
elif ans1 in answerExplore:
    print("\nYou find precious 20 minerals that seem worth salvaging")
    globalvariables.mineralCount = 20
    print("""You go back to your ship and the fuel is at,""", shipFuel, '\nYou need at least',
          shipFuelMax, ' to get off this planet')
else:
    print("\nYou typed the wrong input. Try again!")

print("""
Now that you've adjusted yourself to your new surrounding you need to start exploring.
You can either follow a river, or explore the land. (River / Land)
""")

ans2 = input(">>")

if ans2 in answerRiver:
    print("\nCome across a civilization.\nYou notice some inhabitants.")
    print("Do you approach them or wait for an opportunity to take one of them hostage?")
    print("""Consider this decision carefully, these villager seem to be your equal.\nOne of these choices could yield 
    better rewards.\n(Approach / Hostage)""")
    ans3 = input(">>")
    if ans3 in answerApproach:
        madeContact()
    elif ans3 in answerHostage:
        print("you fight the villager.\nYou realize your strengths are equal.")
        time.sleep(2)
        print("You have a fifty fifty chance of wining.")
        time.sleep(2.5)
        print("This")
        time.sleep(2)
        print('was')
        time.sleep(3)
        print('a')
        time.sleep(3)
        print('really')
        time.sleep(3)
        print('close')
        time.sleep(3)
        print('fight...')
        time.sleep(5)
        result = villagerHostileTakeover()
        if result in ["You lost the fight!"]:
            print("You lost the fight...")
            time.sleep(3.5),
            print("Game")
            time.sleep(2.5)
            print("Over!")
        else:
            print("You won the fight!")
            time.sleep(3.5)
            print("""Villager will help you.\nVillager: You won this fight. My name is""", npcName)
            print("Sasha: I see you you minerals.\nOur people need those minerals as we use them for a fuel source.")
            print("Sasha: I can show where plentifully and my people will help get you off this planet")
            print(mineralCount)
            trekSashaLessHelpful()
            returnToCivializationWithoutSahsa()

elif ans2 in answerLand:
    print("\nYou find another 20 minerals that seem worth salvaging")
    globalvariables.mineralCount = 20 + globalvariables.mineralCount
    print("\nMineral amount is now: ", globalvariables.mineralCount)
    time.sleep(2.5)
    print('You to continue to explore and you make contact with a village.')
    time.sleep(2.5)
    madeContact()
else:
    print("\nYou typed the wrong input. Try again!")

# ans4Result = madeContact()

if globalvariables.ans4 in globalvariables.answerHelp:
    trekSashaHelpful()
    #returnToCivialization()
elif globalvariables.ans4 in globalvariables.answerTakeHelp:
    trekSashaLessHelpful()
    #returnToCivializationWithoutSahsa()
else:
    print("\nYou typed the wrong input. Try again!")