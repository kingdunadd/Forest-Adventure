# Written by Daisy Simmons

# NOT FINISHED

import random
import time

cook_food = False
id_book = False
make_fire = False
food = 0 # each tin is 1 unit
water = 0 # 10 units of water for each litre of water
torch = 0 # can use 50 times 
area_map = False
tarpaulin = False
penknife = False
bike = False
tent = False
enemy = ""
days = 0

left_path = False
right_path = False
straight_path = False


cmdlist = []

def game():
    global person

    print ("Welcome to Forest Adventure!")
    wait()
    print()
    print ("You are stuck in the middle of a forest.")
    wait()
    print("You have to find your way out - and try to do it in the smallest number of days possible!")
    wait()
    print("Let the adventure begin!")
    wait()
    print("\n")
    wait()

    # lets you select which character you want to be
    print ("Do you choose to be Daisy, Rowan or Ash? ")
    print("1. Daisy")
    print("2. Rowan")
    print("3. Ash")
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    # tells you about your selected character
    if cmd == '1':
        person = "Daisy"
        print("You are Daisy")
        print()
        wait()
        print("You have 10 pieces of equipment. These are:")
        wait()
        print("a sleeping bag")
        # all have sleeping bag so no need for variable
        sleeping_bag = True
        wait()
        print("an ID book for foraging")
        id_book = True
        wait()
        print("a full packet of matches (containing 50 matches)")
        make_fire = True
        wait()
        print("a penknife")
        penknife = True
        wait()
        print("a compass")
        # all have compass so no need for variable
        wait()
        print("a backpack full of tinned food") # 15 tins
        food = 15
        wait()
        print("a big 1 litre waterbottle")
        water = 10
        wait()
        print("a saucepan")
        cook_food = True
        wait()
        print("a tarpaulin")
        tarpaulin = True
        wait()
        print("and a rope.")
        wait()

    if cmd == '2':
        person = "Rowan"
        print("You are Rowan")
        print()
        wait()
        print("You have 10 pieces of equipment. These are:")
        wait()
        print("a set of climbing gear (with a harness and some rope)")
        wait()
        print("a 1 litre waterbottle")
        water = 10
        wait()
        print("a tarpaulin")
        tarpaulin = True
        wait()
        print("a tinderbox with firestarting materials")
        make_fire = True
        wait()
        print("a saucepan")
        cook_food = True
        wait()
        print("a bike")
        bike = True
        wait()
        print("a compass")
        # all have compass so no need for variable
        wait()
        print("a torch with a limited amount of power")
        torch = 50
        wait()
        print("a full pack of matches (containing 50 matches)")
        wait()
        print("and a sleeping bag.")
        # all have sleeping bag so no need for variable
        wait()

    if cmd == '3':
        person = "Ash"
        print("You are Ash")
        print()
        wait()
        print("You have 10 pieces of equipment. These are:")
        wait()
        print("a bike")
        bike = True
        wait()
        print("a backpack full of tinned food and 2 1-litre waterbottles") # 10 tins
        food = 10
        water = 20
        wait()
        print("some outdoor clothes (including a raincoat)")
        wait()
        print("2 flares")
        wait()
        print("a map of the surrounding area")
        area_map = True
        wait()
        print("a tent")
        wait()
        print("a sleeping bag")
        # all have sleeping bag so no need for variable
        wait()
        print("a compass")
        wait()
        # all have compass so no need for variable
        print("and a torch with a limited amount of power.")
        torch = 50
        wait()
            
        

def waytogo():
    global right_path, left_path, straight_path
    print()
    print("There are three paths ahead of you. You can go")
    print("1. Left")
    print("2. Right")
    print("3. Straight ahead")
    wait()

    if area_map == True:
        print("You check your map to find the best way to go.")
        print("It says that the left path looks mostly clear.")
        print("There is a swamp further along the path straight ahead.")
        print("There is a bog along the right path.")
        print("The map doesn't tell you which path to take to get out of the forest, but at least you know what's ahead")
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        print("You start along the left path.")
        right_path = False
        straight_path = False
        left_path = True

        wait()
        print("As you are walking along a wolf jumps out in front of you!")
        fight_wolf()

    if cmd == '2':
        print("You start along the right path.")
        right_path = True
        left_path = False
        straight_path = False
        wait()
        print("It is getting dark.")
        print("As you look for a place to spend the night, you notice a light bobbing close to you.")
        print("It begins to move away.")
        willowisp()

    if cmd == '3':
        print("You start along the path straight ahead.")
        straight_path = True
        right_path = False
        left_path = False
        wait()
        print("As the day goes on you start to feel hungry.")
        print("You spot a patch of mushrooms growing at the side of the path.")
        poison()


def fight_wolf():
    global enemy
    print("The wolf growls and looks like it's going to jump at you!")
    enemy = "wolf"

    attack()

def attack():
    if penknife == True:
        fight_hurt = random.choice([True, False])
        print("You pull out your penknife and start to fight with the", enemy ,".")
        if fight_hurt == True:
            print ("The ", enemy ," wounded you! You run back into the forest cover.")
            hurt()

        elif fight_hurt == False:
            print ("You wounded the ", enemy ," and it ran away.")
    else:
        print ("The ", enemy ," wounded you! You run back into the forest cover.")
        hurt()

    if enemy == "wolf":
        night()
    elif enemy == "rodent":
        night()


def pool():
    global water, cook_food, make_fire
    print("You come to a large pool of stagnant water.")
    print("You decide to ")
    print("1. Fill up your water bottle(s)")
    print("2. Keep going")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if cook_food == True and make_fire == True:
            print("You boil the water in your saucepan to get rid of any germs.")
            water += 5 
            # next module
        else:
            print("You drink some of the water, as you are thirsty.")
            water += 5
            print("Later in the evening you start to feel sick and start vomiting.")
            print("You fall asleep, but are hot and clammy.")
            print("You start hallucinating...")
            dead()
    if cmd == '2':
        pass


def willowisp():
    wait()
    print("Do you decide to follow it?")
    print("1. Yes")
    print("2. No")
    wait()
            
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        wait()
        print("You start to follow the light. It is blue and slowly bobs up and down.")
        wait()
        print("As you are walking, the ground starts to feel squelchier underneath.")
        wait()
        print("You suddenly realise you have walked into a bog.")
        print("Do you")
        print("1. Turn around and head out of the bog")
        print("2. Keep going")
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
        if cmd == '1':
            print ("You turn around and look for a place to sleep.")
            night() 
        if cmd == '2':
            bog()
                
    if cmd == '2':
        wait()
        print ("You turn around and keep looking for a place to sleep.")
        night()
        
def bog():
    print("You keep wading deeper into the bog, following the light.")
    tree()

def tree():
    print("You come across an apple tree with apples on.")
    print("Do you")
    print("1. Climb the tree to collect some apples")
    print("2. Keep on walking")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        pass


def poison():
    global food, water
    # do the mushrooms poison you or not - if you eat them
    wait()
    print("You are hungry, and don't know whether to eat them or not.")
    print("Do you decide to eat them?")
    print("1. Yes")
    print("2. No")
    wait()

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
    
    if cmd == 1:
        if id_book == True:
            print ("You look the mushroom up and see that it is poisonous.")
            print("You eat a tin of food instead.")
            food -= 1
            water -= 1
        else:
            poisoned = random.choice([True, False])
            if poisoned = True:
                print("The mushroom is poisonous!")
                print("You ate enough mushrooms to really feel the poison.")
                print("You start to hallucinate...")
                dead()
            if poisoned = False:
                print("The mushroom was poisonous, but didn't kill you.")
                hurt()
    if cmd == 2:
        print("You eat a tin of food instead.")
        food -= 1
        water -= 1

def lake():
    print("You come to the side of a big lake.")

def rous():
    global enemy
    # rodents of unusual size
    print("You are walking through a swamp when you see a sign saying 'Beware of the rodents of unusual size'.")
    print("ROUSes? You don't belive they exist.")
    print("When you turn around you see a large rodent behind you!")
    enemy = "rodent"
    attack()



def night():
    global tent, left_path, right_path, straight_path, days
    print("The sky gets slowly darker and you decide to find a place to spend the night.")

    if tent == True:
        print("You set up your tent and go to sleep.")
    else:
        print("You go to sleep in your sleeping bag.")
    wait()
    days += 1
    print("It is morning and you decide to")
    print("1. Keep going along the same path")
    print("2. Go back the way you came")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if left_path == True:
            print("You keep walking along the left path.")
            pool()
        if right_path == True:
            print("You keep walking along the right path.")
            bog()
        if straight_path == True:
            print("You keep walking along the path straight ahead.")
            rous()
    if cmd == '2':
        print("You turn back along the path.")
        waytogo()

def starved():
    print("You start to feel lightheaded.")
    print("You realize that you have run out of food and water!")
    print("You have no energy to find anything.")
    print("You decide to lie down for a little sleep...")
    dead()

def hurt():
    global days
    print("You take a day to recover from it.")
    days += 1

def dead():
    wait()
    print("You died.")
    print()
    again = input("Do you want to play again? (y/n)")
    if again in ['y','Y','yes','Yes','YES']:
        game()
    else:
        sys.exit(0)


def out_of_forest():
    wait()
    print("You made it out of the forest in ", days ,"days.")
    print("You only had ", food, " tins of food and ", water ," units of water left!")
    print()
    again = input("Do you want to play again? (y/n)")
    if again in ['y','Y','yes','Yes','YES']:
        game()
    else:
        sys.exit(0)



def wait():
    time.sleep(1)

def getcmd(cmdlist):
    cmd = input("\nEnter your number: ")
    if cmd in cmdlist:
        return cmd


# main program
game()
waytogo()
while True:
    if food == 0 and water == 0:
        starved()
