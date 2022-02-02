from Utils.HelperMethods import print_with_delay, select_a_game, select_difficulty, user_play_again, \
    get_verified_value_from_user, input_with_delay, check_user_exist
from Games.GuessGame import play as play_guess_game
from Games.MemoryGame import play as play_memory_game
from Games.CurrencyRoulette import play as play_currency_roulette_game
from Scores.scores_calc import add_score_with_user
from Utils.UtilsFile import IS_USER_EXIST
from time import sleep


def welcome():
    global user_name
    user_name = get_verified_value_from_user(3, "string", "Hi there! Please enter your name to continue:", 1)
    if check_user_exist():
        print_with_delay(f"Hi {user_name}! It's great having you back.", 8, 1)
        get_verified_value_from_user(3, "string", f"Do you need a refresh of your choices?", 8)
    # elif:
    # print_with_delay(f"Hello {user_name} and welcome to the World of Games (WoG)!\n"
    #                      "Here you can find many cool games to play.\n", 7, 1)


def load_game():
    # want_to_play = True
    # while want_to_play:
    #     game_value = select_a_game()
    #     difficulty_value = select_difficulty()
    #     if game_value == 1:
    #         if play_memory_game(difficulty_value):
    #             add_score(difficulty_value, user_name)
    #     if game_value == 2:
    #         if play_guess_game(difficulty_value):
    #             add_score(difficulty_value, user_name)
    #     if game_value == 3:
    #         if play_currency_roulette_game(difficulty_value):
    #             add_score(difficulty_value, user_name)
    #     want_to_play = user_play_again()
    add_score_with_user(3, user_name)
