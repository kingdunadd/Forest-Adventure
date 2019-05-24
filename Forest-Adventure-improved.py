# Written by Daisy Simmons

# NOT FINISHED

from random import randint

def game():
    global person

    print ("Welcome to Forest Adventure!")
    print()
    print ("You are stuck in the middle of a forest.")
    print("You have to find your way out.")
    print("Let the adventure begin!")
    print("print")

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
        print("You have 10 pieces of equipment. These are:")
        print("a sleeping bag")
        print("an ID book for foraging")
        print("a full packet of matches (containing 50 matches)")
        print("a penknife")
        print("a compass")
        print("a backpack full of tinned food")
        print("a big 1 litre waterbottle")
        print("a saucepan")
        print("a tarpaulin")
        print("and a rope.")

    if cmd == '2':
        person = "Rowan"
        print("You are Rowan")
        print("You have 10 pieces of equipment. These are:")
        print("a set of climbing gear (with a harness and some rope)")
        print("a 1 litre waterbottle")
        print("a tarpaulin")
        print("a tinderbox with firestarting materials")
        print("a saucepan")
        print("a bike")
        print("a compass")
        print("a torch with a limited amount of power")
        print("a full pack of matches (containing 50 matches)")
        print("and a sleeping bag.")

    if cmd == '3':
        person = "Ash"
        print("You are Ash")
        print("You have 10 pieces of equipment. These are:")
        print("a bike")
        print("a backpack full of tinned food and 2 waterbottles")
        print("£10")
        print("some outdoor clothes (including a raincoat)")
        print("2 flares")
        print("a map of the surrounding area")
        print("a tent")
        print("a sleeping bag")
        print("a compass")
        print("and a torch with a limited amount of power.")
            
        

def waytogo():
    print()
    print("There are three paths ahead of you. You can go")
    print("1. Left")
    print("2. Right")
    print("3. Straight ahead")
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
        print ("You start along the left path.")
        print ("...")
        print ("As you are walking along a wolf jumps out in front of you!")
        fight()

    if cmd == '2':
        print ("You start along the right path.")
        print ("...")
        print ("It is getting dark.")
        print ("As you look for a place to spend the night, you notice a light bobbing close to you.")
        print ("It begins to move away.")
        willowisp()

    if cmd == '3':
        print ("You start along the path straight ahead.")
        print ("...")
        print ("As the day goes on you start to feel hungry.")
        print ("You spot a patch of mushrooms growing at the side of the path.")
        poison()


def fight():
    fight = int((randint(1, 2)))

    if fight == 1:
        print ("The wolf wounded you! You run back into the forest.")

    elif fight == 2:
        print ("You wounded the wolf and it ran away.")

                 #person == daisy
           # print ("You have a penknife, use it to attack the wolf.")
            #fight = int((randint(1, 2)))

            #if fight == 1:
                #print ("The wolf wounded you! You run back into the forest.")

            #elif fight == 2:
               # print ("You wounded the wolf and it ran away.")


def willowisp():
    print ("Do you decide to follow it?")
    print("1. Yes")
    print("2. No")
            
    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
	
    if cmd == '1':
            print ("You start to follow the light. It is blue and slowly bobs up and down.")
                
    if cmd == '2':
            print ("You turn around and go the other way.")
        


def poison():
    # do the mushrooms poison you or not

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)
    
    print ("")

def getcmd(cmdlist):
    cmd = input("printEnter your number: ")
    if cmd in cmdlist:
        return cmd


# main program
game()
waytogo()
getcmd(cmdlist)
