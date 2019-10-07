import time
import random
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def charactors_who():    
    charactors = ["Saitama", "Goku", "Jojo", "Zoro", "Mario", "Naruto"]
    random.choice(charactors)
    print_pause("Welcome! We picked your name randomly (^^) ")
    print_pause("Your name is ......")
    print(random.choice(charactors))
    print_pause("The story has begun...")
    time.sleep(3)
    
     
def intro():
    print_pause("You find yourself standing in an open field,\n"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a dragon is somewhere around here,\n"
                "and has been terrygying the nearby villege.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your 25 cents\n"
                "(absolutely NOT effective).")

    
def house():
    response = input("Enter 1 to knock on the door of the house.\n"
                     "Enter 2 to peer into the cave.\n"
                     "(Please enter 1 or 2 ): ")
    if response == "1":
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door\n"
                    "opens and out steps a dragon.")
        print_pause("Eep! This is the dragon's house!")
        print_pause("The dragon attacks you!")
        print_pause("You feel a bit under-prepared for this,")
        print_pause("what with only having a 25 cents...")
        response_s = input("Would you like to (1) give 25 cents?\n"
                           "or (2) run away?\n"
                           "(Please enter 1 or 2 ):\n")
        if response_s == "1":
            print_pause("...That was bad decision.....")
            print_pause("You do your best...")
            print_pause("but your money is not enough for the dragon.")
            print_pause("You have been defeated! - GAME OVER")
            return play_again()        
        elif response_s == "2":
            print_pause("You run back into the field.")
            print_pause("Luckily, you don't seem to have been followed.")
            print_pause("Now what would you like to do ..?")
        else:
            print_pause("..............sorry I don't understand.")
            return response_s
    elif response == "2":
        return cave()
    else:
        print_pause("Sorry I don't understand...")
        return house()  
    
    
def house_cave():
    response = input("Enter 1 to go back to the house.\n"
                     "Enter 2 to peer into the cave.\n"
                     "(Please enter 1 or 2 ): ")
    if response == "1":
        print_pause("Does dragon care about money..really?")
        print_pause("I need to something to fight with...")
        return house_cave()
    elif response == "2": 
        print_pause("That's the right choice! I need to find something\n"
                    "to fight with..")
        return cave()
    else:
        print_pause("..............again!? I don't understand.")
        return house_cave()   
    
    
def cave():           
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You put 25 cents in your pocket and take the\n"
                "sword with you.")
    print_pause("You walk back out to the field.")
    items.append("Sword of Ogoroth")
    return field(items)    


def field(items):
    response = input("Enter 1 to knock on the door of the house.\n"
                     "Enter 2 to peer into the cave.\n"
                     "(Please enter 1 or 2 ):\n")
    if response == "1":    
        print_pause("As the dragon moves to attack, you unsheath\n"
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause("But the dragon takes one look at your shiny\n"
                    "new toy and runs away!")
        print_pause("You have rid the town of the dragon. You WIN this game")
        return play_again()
    elif response == "2":
        print_pause("You have already been there!")
        print_pause("You are ready to fight!!!")
        return field(items)
    else:
        print_pause("..............")
        return field(items)
    
    
def play_again():
    a = input("Would you like to play again? (y / n) ").lower()
    if a == "n":
        print_pause("Thank you for playing! Good bye")
        exit()
    elif a == "y":
        print_pause("Good choice. restarting the game...")
        return adventure_game()
    else:
        print_pause("I only accept 'y' or 'n' - thanks!")
        return play_again()
    return intro()  


def adventure_game():
    charactors_who()
    intro()
    house()
    house_cave()
    cave()
    field(items)
    play_agein() 

  
adventure_game()
    
