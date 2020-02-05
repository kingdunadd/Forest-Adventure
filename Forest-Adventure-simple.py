# Written by Daisy Simmons

from random import randint
import random
import time

def setup():
    global cook_food, id_book, make_fire, food, water, torch, area_map, tarpaulin
    global penknife, bike, tent, days, done_wolf, done_pool, done_poison
    global done_rous, done_willowisp, done_bog, done_tree, cmdlist, climbing, follow_willowisp
    # sets up all the variables needed
    cook_food = False
    id_book = False
    make_fire = False
    food = 1 # each tin is 1 unit
    water = 1 # 10 units of water for each litre of water
    torch = 0 # can use 50 times 
    area_map = False
    tarpaulin = False
    penknife = False
    bike = False
    tent = False
    climbing = False

    days = 0

    # to see where to go next
    done_wolf = False
    done_pool = False
    done_poison = False
    done_rous= False
    done_willowisp = False
    done_bog = False
    done_tree = False
    follow_willowisp = False

    cmdlist = []
    game()

def game():
    global person, cook_food, id_book, make_fire, food, water, torch
    global area_map, tarpaulin, penknife, bike, tent, climbing

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
        climbing = True
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
    #global area_map
    # the user chooses which way to go
    print()
    print("There are three paths ahead of you. You can go")
    print("1. Left")
    print("2. Right")
    print("3. Straight ahead")
    print()
    wait()

    # if they have a map of the area then they can use it to find out what lies ahead
    if area_map == True:
        print("You check your map to find the best way to go.")
        wait()
        print("It says that the left path looks mostly clear.")
        wait()
        print("There is a swamp further along the path straight ahead.")
        wait()
        print("There is a bog along the right path.")
        wait()
        print("The map doesn't tell you which path to take to get out of the forest, but at least you know what's ahead.")
        wait()
        print()
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        print("You start along the left path.")
        wait()
        wolf()

    if cmd == '2':
        print("You start along the right path.")
        wait()
        willowisp()

    if cmd == '3':
        print("You start along the path straight ahead.")
        wait()
        mushrooms()


def wolf():
    global done_wolf
    done_wolf = True
    print()
    print("As you are walking along a wolf jumps out in front of you!")
    print("The wolf growls and looks like it's going to jump at you!")
    attack("wolf")

def pool():
    global water, cook_food, make_fire, done_pool
    done_pool = True
    print()
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
            night()
        else:
            print("You drink some of the water, as you are thirsty.")
            print()
            wait()
            water += 5
            print("Later in the evening you start to feel sick and start vomiting.")
            print("You fall asleep, but are hot and clammy.")
            print("You start hallucinating...")
            dead()
    if cmd == '2':
        night()


def willowisp():
    global done_willowisp, follow_willowisp
    done_willowisp = True
    wait()
    print("It is getting dark.")
    print("As you look for a place to spend the night, you notice a light bobbing close to you.")
    print("It begins to move away.")
    print("Do you decide to follow it?")
    print("1. Yes")
    print("2. No")
    wait()
            
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        follow_willowisp = True
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
    global done_bog
    done_bog = True
    print()
    if follow_willowisp == True:
        print("You keep wading deeper into the bog, following the light.")
        print("The mud gets deeper and thicker.")
        wait()
        print("You are stuck!")
        print("The mud seems to be pulling you down.")
        print("As you struggle, the mud closes around you.")
        print("The mud closes over your head as you take one last breath...")
        dead()
    if follow_willowisp == False:
        print("You keep wading deeper into the bog.")
        print("You move away from where the flickering light is.")
        print("You have heard tales of lights like these, called will-o-wisps.")
        print("They lure travellers into deep mud and drown them.")
        print()
        print("You safely get to the edge of the bog.")
        
        tree()


def tree():
    global done_tree, food
    done_tree = True
    print()
    print("You come across an apple tree with apples on.")
    print("Do you")
    print("1. Climb the tree to collect some apples")
    print("2. Keep on walking")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        if climbing == True:
            print("You use your climbing gear to climb the tree easily.")
            print("You pick some apples.")
            food += 8
            night()
        else:
            print("You climb the tree.")
            fall = randint(1,2)
            if fall == 1:
                print("Your foot slips, but you manage to put it back in place.")
                print("You pick some apples.")
                food += 7
                night()
            if fall == 2:
                print("Your foot slips and you fall out of the tree!")
                print("Luckily it isn't very high and you only twist your ankle.")
                hurt()


def mushrooms():
    global food, water, done_poison
    done_poison = True
    # do the mushrooms poison you or not - if you eat them
    wait()
    print("As the day goes on you start to feel hungry.")
    print("You spot a patch of mushrooms growing at the side of the path.")
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
            water -= 2
            next_way()
        else:
            poisoned = randint(1,2)
            if poisoned == 1:
                print("The mushroom is poisonous!")
                print("You ate enough mushrooms to really feel the poison.")
                print("You start to hallucinate...")
                dead()
            if poisoned == 2:
                print("The mushroom was poisonous, but didn't kill you.")
                hurt()
    if cmd == 2:
        print("You eat a tin of food instead.")
        food -= 1
        water -= 2
        next_way()

def rous():
    global enemy, done_rous
    done_rous = True
    # rodents of unusual size
    print("You are walking through a swamp when you see a sign saying 'Beware of the rodents of unusual size'.")
    print("ROUSes? You don't belive they exist.")
    print("When you turn around you see a large rodent behind you!")
    attack("rodent")

def lake():
    print("You come to the side of a big lake.")
    
    out_of_forest()

def night():
    global days, food, water
    print()
    print("The sky gets slowly darker and you decide to find a place to spend the night.")

    if tent == True:
        print("You set up your tent and go to sleep.")
    else:
        print("You go to sleep in your sleeping bag.")
    wait()
    days += 1
    food -= 1
    water -= 2
    print("It is morning and you get out of your sleeping bag.")
    next_way()


def next_way():
    global food, water
    food -= 1
    water -= 2
    print()
    print("You decide to")
    print("1. Keep going along the same path")
    print("2. Go back the way you came")

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        print("You keep walking along the path.")

        if done_wolf == True:
            pool()
        if done_poison == True:
            rous()
        if done_willowisp == True:
            tree()
        if done_rous == True:
            lake()

    if cmd == '2':
        print("You turn back along the path.")
        waytogo()
        

def attack(enemy):
    print()
    if penknife == True:
        fight_hurt = random.choice([True, False])
        print("You pull out your penknife and start to fight with the", enemy,".")
        if fight_hurt == True:
            print ("The", enemy ,"wounded you! You run back into the forest cover.")
            print()
            hurt()

        elif fight_hurt == False:
            print ("You wounded the", enemy ,"and it ran away.")
    else:
        print ("The", enemy ,"wounded you! You run back into the forest cover.")
        print()
        hurt()

    night()


def starved():
    print("You start to feel lightheaded.")
    print("You realize that you have run out of food and water!")
    print("You have no energy to find anything.")
    print("You decide to lie down for a little sleep...")
    print()
    dead()

def hurt():
    global days, food ,water
    print("You take a day to recover from it.")
    days += 1
    food -= 3
    water -= 6
    next_way()

def dead():
    wait()
    print("You died.")
    print()
    again = input("Do you want to play again? (y/n): ")
    print()
    if again in ['y','Y','yes','Yes','YES']:
        setup()
    else:
        sys.exit(0)


def out_of_forest():
    wait()
    print("You made it out of the forest in ", days ,"days.")
    print("You only had ", food, " bits of food and ", water ," units of water left!")
    print()
    again = input("Do you want to play again? (y/n): ")
    if again in ['y','Y','yes','Yes','YES']:
        setup()
    else:
        sys.exit(0)



def wait():
    time.sleep(1)

def getcmd(cmdlist):
    cmd = input("\nEnter your number: ")
    print()
    try:
        if cmd in cmdlist:
            return cmd
    except ValueError:
        cmd = 1



# main program
setup()
waytogo()
while True:
    if food >= 0 and water >= 0:
        starved()
