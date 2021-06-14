import random
import os
import pickle
from termcolor import colored

# This is a terminal application that helps you with DnD 5e,
#   Enjoy.


### FUNCTIONS ###

def display_title_bar():
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nI will remember these players.")
    except Exception as e:
        print("\n Error Loading Player names.")
        print(e)
    
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')
              
    print(colored("\t**********************************************", 'red'))
    print(colored("\t***", 'red'),colored("         DnD 5e - Helper Tool", 'yellow'),colored("         ***", 'red'))
    print(colored("\t**********************************************", 'red'))
    
def get_user_choice():
    # Let users know what they can do.
    print(colored("\n[1] Attack Target", 'yellow'))
    print(colored("[2] Roll Dice", 'yellow'))
    print(colored("[3] Add Players", 'yellow'))
    print(colored("[4] Current Players", 'yellow'))
    print(colored("[5] Random Target", 'yellow'))
    print(colored("[6] Delete Player", 'yellow'))
    print(colored("[q] Quit", 'red'))
    
    return input("What would you like to do? ")
    
def show_names():
    # Shows the names of everyone who is already in the list.
    print("\nCurrent players.\n")
    for name in names:
        print(name.title())
        
def get_new_name():
    # Asks the user for a new name, and stores the name if we don't already
    new_name = input("\nPlease enter character name: ")
    if new_name in names:
        print("\n%s is already added, please add different name." % new_name.title())
    else:
        names.append(new_name)
        print("\n%s is added." % new_name.title())
        
def load_names():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        file_object = open('names.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []

def delete_names():
    # try to delete the given user, handle if the user doesn't exist.
    show_names()
    user_to_delete = input("\nPlease enter character name to DELETE: ")
    try:
        names.remove(user_to_delete)
    except Exception as user:
        print("{user} doesn't exist in db".format(user=user_to_delete))

def random_target():
    name = load_names()
    x = random.sample(name, 1)
    for y in x:
        print("%s is the target." % y.title())
        
def quit():
    # This function dumps the names into a file, and prints a quit message.
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nI will remember these players.")
    except Exception as e:
        print("\n I won't be able to add these players.")
        print(e)

def roll_attack():
    num_sides = 20      # 1D20
    modifier = int(input('Modifier for attacking creatures:\n'))
    num_dice = int(input('Enter the number of attacking creatures:\n'))       # input the number of creatures
    num_AC = int(input('Enter the targets AC:\n'))

    print(num_dice, 'Are attacking.')
    for i in range(num_dice):
        num = random.randint(1, num_sides)
        total =  num + modifier
        
        if num == 20:
            print(num, '+',modifier,'=', total, "CRIT!")
        elif total > num_AC:
            print(num, '+',modifier,'=', total, "HIT")
        else:
            print(num, '+',modifier,'=', total)

def roll_dice():
    num_type = int(input('Type of dice:\n'))      # example 20 for 1D20
    num_dice = int(input('Number of dice:\n'))       # input the number of dice
    num_mod = int(input('Modifier for dice:\n'))  
    num_sum = sum(random.randint(1, num_type) for _ in range(num_dice))
    total = num_sum + num_mod
    
    print(num_sum, "+", num_mod, "=", total)
              
### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
names = load_names()

choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        roll_attack()
    elif choice == '2':
        roll_dice()
    elif choice == '3':
        get_new_name()
    elif choice == '4':
        show_names()
    elif choice == '5':
        random_target()
    elif choice == '6':
        delete_names()
    elif choice == 'q':
        quit()
        print("\nBye.")
    else:
        print("\nI didn't understand that choice.\n")
