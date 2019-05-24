
from random import randint

def game():
    print ("Welcome to Forest Adventure!")
    print ("\nYou are stuck in the middle of a forest.\nYou have to find your way out.\nLet the adventure begin!")
    # lets you select which character you want to be
    person = input ("\n\nDo you choose to be Daisy, Rowan or Ash? ")
    if person == "Ash" or person == "ash" :
        #character = ash
        print ("You have 10 pieces of equipment. These are:\na bike\na backpack full of tinned food and 2 waterbottles\n£10\nsome outdoor clothes (including a raincoat)\n2 flares\na map of the surrounding area\na tent\na sleeping bag\na compass\nand a torch with a limited amount of power.")
    elif person == "Daisy" or person == "daisy" :
        #char = daisy
        print ("You have 10 pieces of equipment. These are:\na sleeping bag\nan ID book for foraging\na full packet of matches (containing 50 matches)\na penknife\na compass\na backpack full of tinned food\na big 1 litre waterbottle\na saucepan\na tarpaulin\nand a rope.")
    elif person == "Rowan" or person == "rowan" :
        #player = rowan
        print ("You have 10 pieces of equipment. These are:\na set of climbing gear (with a harness and some rope)\na 1 litre waterbottle\na tarpaulin\na tinderbox with firestarting materials\na saucepan\na bike\na compass\na torch with a limited amount of power\na full pack of matches (containing 50 matches)\nand a sleeping bag.")
    else:
        print ("This name is invalid. Please be useful and actually do what i ask you to do. You will have to start again to make the program work properly.")
        

def waytogo():
    print()
    way = input ("Choose which way to go. You can go left, right, or straight ahead. ")
    if way == "Left" or way == "left" :
        print ("You start along the left path.")
        print ("As you are walking along a wolf jumps out in front of you!")
         #person == daisy
           # print ("You have a penknife, use it to attack the wolf.")
            #fight = int((randint(1, 2)))

            #if fight == 1:
                #print ("The wolf wounded you! You run back into the forest.")

            #elif fight == 2:
               # print ("You wounded the wolf and it ran away.")

    if way == "Right" or way == "right" :
        print("You start along the right path.")



    if way == "Straight" or way == "straight" or way == "Straight ahead" or way == "straight ahead" :
        print("You start along the path straight ahead.")



# main program
game()
waytogo()

