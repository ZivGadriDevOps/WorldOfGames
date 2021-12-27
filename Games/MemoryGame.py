from random import randint
from HelperMethods import print_with_delay, get_verified_value_from_user, \
    turn_num_into_counter, check_if_user_ready, count_down, print_faces
from time import sleep


def generate_sequence(difficulty):
    list_of_numbers = []
    for i in range(difficulty):
        rnd = randint(1, 101)
        list_of_numbers.append(rnd)
    return list_of_numbers


def get_guess_list_from_user(difficulty):
    guess_list_from_user = []
    if difficulty > 1:
        print_with_delay(f"Please enter the {difficulty} numbers as you remember them.", 30, 2)
    else:
        print_with_delay("Please enter the number as you remember.", 30, 2)

    for i in range(difficulty):
        counter = turn_num_into_counter(i+1)
        guess_list_from_user.append(get_verified_value_from_user(3, "int", f"Your {counter} number is: ", 100))
    print_with_delay("\nThe list of numbers you typed is:", 10, 1)
    for i in range(len(guess_list_from_user)):
        if i == len(guess_list_from_user) - 1:
            print(guess_list_from_user[i])
        else:
            print(f"{guess_list_from_user[i]}, ", end="")
    sleep(1)
    return guess_list_from_user


def compare_results(actual_list, user_guess_list, check_for_order):
    print_with_delay("\nThe actual list of numbers you were presented with is:", 10, 1)
    for i in range(len(actual_list)):
        if i == len(actual_list) - 1:
            print(actual_list[i])
        else:
            print(f"{actual_list[i]}, ", end="")
    sleep(1)
    if check_for_order:
        for i in range(len(actual_list)):
            if actual_list[i] != user_guess_list[i]:
                print_with_delay("Sorry, you didn't quite get it right", 10, 0.5)
                print_faces("sad")
                return False
    else:
        actual_list.sort()
        user_guess_list.sort()
        if actual_list != user_guess_list:
            print_with_delay("Sorry, you didn't quite get it right", 10, 0.5)
            print_faces("sad")
            return False
    print_with_delay("WOW!!!", 2, 1.5)
    print_with_delay("You've made it!!!", 10, 1)
    print_faces("happy")
    return True


def play(difficulty):
    if difficulty == 5:
        order_matters = True
        wait_with_list = 1.4
        print_with_delay("Please pay attention carefully.\nSince you've selected the difficulty level of "
                         "'Good luck dude',\nthe order of the numbers in the list you will be presented "
                         "with MATTERS!!!\nYou'll have to remember that too.", 8, 1)
        print_with_delay(f"But.... Since I am a reasonable person, you will be given with {wait_with_list} "
                         f"seconds to view the list before it is gone.", 8, 1.5)
    else:
        order_matters = False
        wait_with_list = 0.7
    print_with_delay(f"In a few seconds you will be presented with a list of {difficulty} numbers.\nThe list will "
                     f"remain on the screen for {wait_with_list} seconds and then it will disappear.", 10, 3)
    check_if_user_ready()
    generated_sequence = generate_sequence(difficulty)
    count_down(5)
    print_with_delay("The list generated is...:\n", 30, 1)
    print(generated_sequence)
    sleep(wait_with_list)
    for i in range(100):
        print("NO CHEATING!!! DON'T SCROLL UP!!!")
    sleep(1)
    print_with_delay("\nNow let's see what you are made of!\n", 20, 0)
    user_guess = get_guess_list_from_user(difficulty)

    return compare_results(generated_sequence, user_guess, order_matters)
