import time
import random



def pause(a):
    print(a)
    time.sleep(2)

def intro():
    pause('You find yourself standing in an open field, filled with grass and yellow wildflowers.')
    pause('Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.')
    x=['dragon', 'witch', 'fairie', 'ogre', 'pirate']
    enemy=print(random.choice(x))

def restartgame():
    while True:
        while True:
            response=input('Would you like to play again? (y/n)')
            pause(response)
            if 'y' in response:
                pause('Excellent! Restarting the game ...')
                intro()
                field()
                break
            elif 'n' in response:
                pause('Thanks for playing! See you next time')
                break
            else:
                pause('Please enter y or n')
                break
def field():
    pause('Enter 1 to knock on the door of the house.')
    pause('Enter 2 to peer into the cave.')
    pause('What would you like to do?')
    while True:
        while True:
            response=input('Please enter 1 or 2')
            pause(response)
            if '1' in response:
                housewithoutsword()
                break
            elif '2' in response:
                cave()
                break
            else:
                pause('please enter (1) or (2)')
                break

def fieldaftercave():
    pause('Enter 1 to knock on the door of the house.')
    pause('Enter 2 to peer into the cave.')
    pause('What would you like to do?')
    while True:
        while True:
            response=input('Please enter 1 or 2')
            pause(response)
            if '1' in response:
                housewithsword()
                break
            elif '2' in response:
                cave2()
                break
            else:
                pause('please enter (1) or (2)')
                break

def housewithoutsword():
    pause('You approach the door of the house')
    pause('You are about to knock when the door opens and out steps a (enemy)')
    pause('eep this is the print (enemy) house')
    pause('The (enemy) attacks you')
    pause('You feel a bit under-prepared for this, what with only having a tiny dagger')
    while True:
        while True:
            response=input('Would you like to (1) fight or (2) run away?')
            pause(response)
            if '1' in response:
                pause('You do your best ...')
                pause('but your dagger is no match for the (enemy)')
                pause('You have been defeated!')
                restartgame()
                break
            elif '2' in response:
                pause("You run back into the field, luckily you don't seem to have been followed.")
                field()
                break
            else:
                pause('Please enter 1 or 2')
                break


def cave():
    pause('You peer cautiously into the cave.')
    pause('It turns out to be only a very small cave.')
    pause('Your eye catches a glint of metal behind some rock.')
    pause('You have found the magical Sword of Ogoroth!')
    pause('You discard your silly old dagger and take the sword with you.')
    pause('You walk back to the field')
    fieldaftercave()

def cave2():
    pause('You peer cautiously into the cave')
    pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    pause("You walk back out to the field")
    field()


def housewithsword():
    pause('You approach the house')
    pause('You are about to knock when the door opens and out steps a (enemy).')
    pause('Eep! This is the (enemy) house')
    pause('The (enemy) attacks you')
    while True:
        while True:
            response=input('Would you like to (1) fight or (2) run away?')
            pause(response)
            if '1' in response:
                pause('As the (enemy) moves to attack you, you unsheath your new sword. ')
                pause('The sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.')
                pause('But the (enemy) takes one look at your shiny new toy and runs away!')
                pause('You have rid the town of the (enemy). You are victorious!')
                restartgame()
                break
            elif '2' in response:
                pause("You run back into the field, luckily you don't seem to have been followed.")
                field()
                break
            else:
                pause('Please enter 1 or 2')
                break


intro()
field()