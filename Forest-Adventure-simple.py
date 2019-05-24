# Written by Daisy Simmons

# NOT FINISHED

from random import randint
import time

id_book = False
make_fire = False
food = 0 # each tin is 1 unit
water = 0 # 10 units of water for each litre of water
torch = 0 # can use 50 times 
area_map = False
tarpaulin = False
penknife = False
bike = False
days = 0

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
    print()
    print("There are three paths ahead of you. You can go")
    print("1. Left")
    print("2. Right")
    print("3. Straight ahead")
    wait()
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        print ("You start along the left path.")
        wait()
        print ("As you are walking along a wolf jumps out in front of you!")
        fight()

    if cmd == '2':
        print ("You start along the right path.")
        wait()
        print ("It is getting dark.")
        print ("As you look for a place to spend the night, you notice a light bobbing close to you.")
        print ("It begins to move away.")
        willowisp()

    if cmd == '3':
        print ("You start along the path straight ahead.")
        wait()
        print ("As the day goes on you start to feel hungry.")
        print ("You spot a patch of mushrooms growing at the side of the path.")
        poison()


def fight():

    if penknife == True:
        fight_no = int((randint(1, 2)))
        print("You pull out your penknife and start to fight with the wolf.")
        if fight_no == 1:
            wait()
            print ("The wolf wounded you! You run back into the forest.")
            hurt()

        elif fight_no == 2:
            wait()
            print ("You wounded the wolf and it ran away.")
    else:
        wait()
        print ("The wolf wounded you! You run back into the forest.")
        hurt()



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
                
    if cmd == '2':
        wait()
        print ("You turn around and keep looking for a place to sleep.")
        night()
        


def poison():
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
            print ("You look the mushroom up and see that the mushroom is poisonous.")
            print("You eat a tin of food instead.")
            food -= 1
        else:
            print("You get poisoned by the mushrooms, but not enouh to kill you.")
            hurt()
    if cmd == 2:
        print("You eat a tin of food instead.")
        food -= 1

def night():
    print("The sky gets slowly darker and you decide to find a place to spend the night.")

    if tent == True:
        print("You set up your tent and go to sleep.")
    else:
        print("You go to sleep.")
    wait()
    days += 1
    print("It is morning and you decide to")
    print("1. Keep going along the same path")
    print("2. Go back the way you came")

def hurt():
    print("You take a day to recover.")
    days += 1

def wait():
    time.sleep(1)

def getcmd(cmdlist):
    cmd = input("\nEnter your number: ")
    if cmd in cmdlist:
        return cmd


# main program
game()
waytogo()
getcmd(cmdlist)
