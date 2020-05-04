import time
import random
item = []
danger = ["pirates", "harpies", "sirens"]


def print_pause(s):
    print(s)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        answer = input(prompt)
        if option1 in answer:
            break
        elif option2 in answer:
            break
        else:
            print_pause("Please enter a valid input.")
    return answer


def intro():
    print_pause("You wake up finding yourself on an island alone.")
    print_pause("There's no one else here. You try to figure out "
                "how to get home.")
    print_pause("In front of you are two vehicles: a jet-ski "
                "and a hot balloon.")


def jet_ski():  # when player choos jet ski
    print_pause("You take the jet-ski and try to get out of the island.")
    print_pause("You are in the middle of the sea and you see a giant ship.")
    choice = valid_input("Would you like to 1 Approach the ship "
                         "or 2 Steer away?", '1', '2')
    if choice == '1':
        print_pause("You approach the ship.")
        print_pause("You step on the ship, however before you "
                    "found out there are a bunch of " + random.choice(danger) +
                    ", it was too late.")
        print_pause("You are killed. You lost.")
    if choice == '2':
        print_pause("You steer away from the ship and get "
                    "to an island called Banana Island.")
        print_pause("The Banana islanders welcome you.")
        if "gift" in item:
            print_pause("But there's nothing more to show you.")
            play_game()
        else:
            print_pause("They show you their hospitality with "
                        "local food and booze.")
            item.append("gift")
            print_pause("You head back to the island with the gift.")
            play_game()


def hot_balloon():  # when player choose hot balloon
    print_pause("You hop into the hot balloon.")
    if "gift" in item:
        print_pause("And you carry the gift with you.")
        print_pause("You opened the gift. Perfect! "
                    "It's the fuel for the hot balloon!")
        print_pause("You ride the hot balloon and find your home."
                    "Yay!You won!")
        item.clear()  # clear list in case player want to play again
        play_again()
    else:
        print_pause("Unfortunately there is no fuel.")
        print_pause("You have to find fuel somewhere else.")
        print_pause("You head back to the island.")
        play_game()


def play_again():
    print_pause("Would you like to play again?")
    time.sleep(2)
    response = valid_input("Please enter 1 if yes, 2 if no", '1', '2')
    if response == '2':
        print_pause("Ok, exit game.")
    elif response == '1':
        item.clear()
        play_game()


def play_game():
    vehicle = valid_input("Please enter 1 to take the jet-ski, "
                          "2 to take the hot balloon.\n", '1', '2')
    if vehicle == '1':
        jet_ski()
    elif vehicle == '2':
        hot_balloon()
    play_again()


intro()
play_game()
