from HelperMethods import print_with_delay, select_a_game, select_difficulty, user_play_again, \
    get_verified_value_from_user, check_user_exist, checkToRepeatInstructions
from Games.GuessGame import play as play_guess_game
from Games.MemoryGame import play as play_memory_game
from Games.CurrencyRoulette import play as play_currency_roulette_game
from scores_calc import add_score_with_user


def welcome():
    global user_name
    user_name = get_verified_value_from_user(3, "string", "Hi there! Please enter your name to continue:", 1)
    if check_user_exist(user_name):
        print_with_delay(f"Hi {user_name}! It's great having you back.", 8, 1)
        repeat_instructions = checkToRepeatInstructions()
    else:
        repeat_instructions = True
        print_with_delay(f"Hello {user_name} and welcome to the World of Games (WoG)!\n"
                         "Here you can find many cool games to play.\n", 7, 1)
    return repeat_instructions


def load_game(repeat_instructions):
    want_to_play = True
    while want_to_play:
        win_game = False
        game_value = select_a_game(repeat_instructions)
        difficulty_value = select_difficulty(repeat_instructions)
        if game_value == 1:
            win_game = play_memory_game(difficulty_value)
        elif game_value == 2:
            win_game = play_guess_game(difficulty_value)
        elif game_value == 3:
            win_game = play_currency_roulette_game(difficulty_value)
        if win_game:
            add_score_with_user(difficulty_value, user_name)
        want_to_play = user_play_again()
        if want_to_play:
            repeat_instructions = checkToRepeatInstructions()
