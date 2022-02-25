from time import sleep
from random import random, randint
import sys

from UtilsFile import SCORES_FILE_PATH, BAD_RETURN_CODE

game_map = {
    "1": "Memory Game",
    "2": "Guess Game",
    "3": "Currency Roulette"
}

difficulty_map = {
    "1": "Piece of cake",
    "2": "Two pieces of cake",
    "3": "Getting serious",
    "4": "Challenges lover",
    "5": "Good luck dude"
}


def select_a_game(repeat_instructions):
    game_value = None
    if repeat_instructions:
        print_with_delay(f"Please choose a game to play by typing its number:\n", 8, 0.5)
        print_values_map(game_map, "game", 15)
    while game_value is None:
        game_value = get_verified_value_from_user(3, "int", "\nYour game selection is: ", len(game_map))
        if game_value is not None:
            print_with_delay(f"Great choice! You have selected {game_map.get(str(game_value))}.\n"
                             "Now choose the level of difficulty.", 8, 1)
    return game_value


def select_difficulty(repeat_instructions):
    difficulty_value = None
    if repeat_instructions:
        print_with_delay(f"Please choose the difficulty level to play by typing its number:\n", 8, 0.5)
        print_values_map(difficulty_map, "difficulty", 15)
    while difficulty_value is None:
        difficulty_value = get_verified_value_from_user(3, "int", "\nYour difficulty selection is: ",
                                                        len(difficulty_map))
        if difficulty_value is not None:
            print_with_delay(f"Awesome!!\nYour difficulty selection is: {difficulty_map.get(str(difficulty_value))}."
                             "\nI believe we are ready to roll!\n\n\n", 8, 3)
    return difficulty_value


def print_values_map(map_to_use, type_of_map, speed):
    if type_of_map == "game":
        print_with_delay(f"1. {map_to_use.get('1')} - a sequence of numbers will appear for 0.7 second and you have to "
                         f"guess it back.\n2. {map_to_use.get('2')} - guess a number and see if you chose like the "
                         f"computer.\n3. {map_to_use.get('3')} - try and guess the value of a random amount of USD in "
                         "ILS.", speed, 1)
    elif type_of_map == "difficulty":
        for key in map_to_use:
            print_with_delay(f"{key}. {map_to_use.get(key)}", speed, 0.3)
            sleep(1)
        print("")


def print_with_delay(text, writing_pace, end_sleep_time):
    for letter in text:
        rnd = random()
        if letter != " ":
            rnd = rnd / writing_pace
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(rnd)
        elif letter == "\n":
            sys.stdout.write(letter)
            sleep(rnd * 1)
        else:
            sys.stdout.write(letter)
    print("")
    sleep(end_sleep_time)


def input_with_delay(text, writing_pace):
    print_with_delay(text, writing_pace, 0)
    return input("")


def turn_num_into_counter(num):
    if num == 1:
        return "1st"
    elif num == 2:
        return "2nd"
    elif num == 3:
        return "3rd"
    else:
        return str(num) + "th"


def assert_for_right_value(input_value, input_type_expected, limit, last_attempt):
    if input_type_expected.lower() == "int" or input_type_expected.lower() == "float":
        try:
            if "." in input_value:
                try:
                    input_value = float(input_value)
                    if input_type_expected.lower() == "float":
                        input_value = round(input_value, 2)
                        return input_value
                    else:
                        input_value = round(input_value, 1)
                    print_with_delay("Decimal number will be converted to a whole number.", 8, 1)
                except ValueError:
                    print_with_delay(f"{input_value} is not a valid input. You must only enter numbers.", 8, 1)
                    return None
            int(input_value)
            if 1 <= int(input_value) <= limit:
                return int(input_value)
            else:
                print_with_delay(f"The numbers you enter should be between 1 and {limit}.", 10, 1)
                return None
        except ValueError:
            print_with_delay(f"'{input_value}' is not a valid input. ", 8, 0.5)
            if not last_attempt:
                print_with_delay(f"You must enter only numbers.", 8, 0)
            return None
    else:
        return input_value


def get_verified_value_from_user(max_attempts, value_type, user_input_message, limit):
    user_value = None
    attempts_count = 0
    while attempts_count < max_attempts and user_value is None:
        if attempts_count != 0:
            print_with_delay("Try again.", 15, 0.5)
            if attempts_count == max_attempts - 1:
                if "game" in user_input_message:
                    print_with_delay("You entered a wrong value AGAIN!!!\nThis will be your last chance for "
                                     "redemption!\nPlease enter one of the FOLLOWING:", 10, 1)
                    print_values_map(game_map, "game", 30)
                elif "difficulty" in user_input_message:
                    print_values_map(difficulty_map, "difficulty", 30)
                else:
                    print_with_delay("You have 1 more attempt left before quiting the game", 15, 1)
            else:
                if "game" in user_input_message or "difficulty" in user_input_message:
                    print_with_delay("You entered a wrong value.\nPlease select one of the following values:", 8, 0.5)
                    if "game" in user_input_message:
                        print_values_map(game_map, "game", 30)
                    else:
                        print_values_map(difficulty_map, "difficulty", 30)
                else:
                    print_with_delay(f"You have {max_attempts - attempts_count} more attempts left before quiting "
                                     f"the game", 15, 1)
        attempts_count += 1
        user_value = assert_for_right_value(input_with_delay(f"{user_input_message}", 15),
                                            f"{value_type}", limit, (max_attempts - attempts_count) == 0)
    if user_value is not None:
        return user_value
    else:
        print_with_delay("You entered too many wrong values.", 10, 1)
        print_with_delay("The game ended.", 10, 1)
        print_with_delay("ADIOS\n", 1, 2)
        print_faces("sad")
        exit(1)
    return user_value


def check_if_user_ready():
    user_ready = False
    num_of_ready_attempts = 3
    while not user_ready and num_of_ready_attempts > 0:
        user_answer = input_with_delay("Are you ready? y/n: ", 8)
        if user_answer.lower() in ["y", "yes"]:
            print_with_delay("Awesome!!!", 5, 1)
            return True
        elif user_answer.lower() in ["n", "no"]:
            if num_of_ready_attempts == 3:
                print_with_delay("Ok..... Take a few more seconds...", 5, 8)
            elif num_of_ready_attempts == 2:
                print_with_delay("Oh that's a bit awkward /:", 3, 3)
            else:
                print_with_delay("I guess you are not made of what you claimed to be. good bye", 4, 2)
        elif num_of_ready_attempts == 3:
            print_with_delay("You entered a wrong value.\n\nPlease type 'yes' or 'no'.", 5, 1)
        elif num_of_ready_attempts == 2:
            print_with_delay("You entered a wrong value.\nYou have one more attempt to get yourself together!!!", 5, 1)
            print_with_delay("\nPlease type 'yes' or 'no'.", 5, 1)
        else:
            print_with_delay("What an @$$ hole!!!", 3, 3)
            print_with_delay("\nBye...", 3, 0)
        num_of_ready_attempts -= 1
    exit(1)


def user_play_again():
    num_of_answering_attmp = 3
    while num_of_answering_attmp > 0:
        user_answer = input_with_delay("Would you like to play again? y/n: ", 8)
        if user_answer.lower() in ["y", "yes"]:
            print_with_delay("Great!!!\nLet's start over.", 5, 1)
            return True
        elif user_answer.lower() in ["n", "no"]:
            print_with_delay("OK. It was great playing with you.\n", 5, 2)
            print_with_delay("Bye.", 5, 2)
            return False
        elif num_of_answering_attmp > 1:
            print_with_delay("You entered a wrong value.\n\nPlease type 'yes' or 'no'.", 5, 1)
        else:
            print_with_delay("What an @$$ hole!!!", 3, 3)
            print_with_delay("\nBye...", 3, 0)
        num_of_answering_attmp -= 1
    return False


def count_down(starting_number):
    for i in range(starting_number, 0, -1):
        print_with_delay(str(i), 5, 1)


def generate_random_int_between(num1, num2):
    return randint(num1, num2)


def print_faces(expression):
    if expression.lower() == "happy":
        print("")
        print("O   O")
        print("  |  ")
        print("\\   /")
        print(" --- ")
    else:
        print("")
        print("O   O")
        print("  |  ")
        print(" ___ ")
        print("/   \\")


def check_user_exist(user_name):
    try:
        with open(SCORES_FILE_PATH, 'r') as file_rw:
            data = file_rw.readlines()
            count = 0
            if len(data) > 0:
                for data_item in data:
                    count += 1
                    existing_user = str(data_item.split(" : ")[0])
                    if user_name.upper() == existing_user.upper():
                        return True
        return False
    except FileNotFoundError:
        print(FileNotFoundError.with_traceback())


def checkToRepeatInstructions():
    available_answers = ["yes", "y", "no", "n"]
    num_attempts = 3
    user_answer = ""
    while not user_answer in available_answers and num_attempts > 0:
        user_answer = input_with_delay("Do you need a refresh of your choices? y/n: ", 8)
        if user_answer.lower() in ["y", "yes"]:
            print_with_delay("Sure", 5, 1)
            return True
        elif user_answer.lower() in ["n", "no"]:
            print_with_delay("Perfect", 5, 1)
            return False
        else:
            if num_attempts == 3:
                print_with_delay("Please answer solly with 'yes' or 'no'.", 4, 2)
            if num_attempts == 2:
                print_with_delay("Come on.... Please type only 'yes' or 'no'.", 4, 2)
            if num_attempts == 1:
                print_with_delay("Ok. I will repeat choices and instructions.", 4, 2)
                return True
        num_attempts -= 1


def get_user_score(user_name):
    try:
        with open(SCORES_FILE_PATH, 'r') as file_rw:
            data = file_rw.readlines()
            count = 0
            if len(data) > 0:
                for data_item in data:
                    count += 1
                    user_name_score = {
                        "USER_NAME": str(data_item.split(" : ")[0]),
                        "USER_SCORE": str(data_item.split(" : ")[1])
                    }
                    if user_name_score.get("USER_NAME").upper() == user_name.upper():
                        return user_name_score.get("USER_SCORE")
                print(f"User {user_name} is not found in 'scores.txt' file.")
                return BAD_RETURN_CODE
    except FileNotFoundError:
        print(FileNotFoundError.with_traceback())


def get_repaired_name(name):
    name_ = ""
    for letterNum in range(len(name)):
        if letterNum == 0:
            name_ += name[letterNum].upper()
        else:
            name_ += name[letterNum].lower()
    return name_

