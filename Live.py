from HelperMethods import print_with_delay, select_a_game, select_difficulty, user_play_again
from Games.GuessGame import play as play_guess_game
from Games.MemoryGame import play as play_memory_game
from Games.CurrencyRoulette import play as play_currency_roulette_game


def welcome(user_name):
    print_with_delay(f"Hello {user_name} and welcome to the World of Games (WoG)!\n"
                     "Here you can find many cool games to play.\n", 7, 1)


def load_game():
    want_to_play = True

    while want_to_play:
        game_value = select_a_game()
        difficulty_value = select_difficulty()
        if game_value == 1:
            play_memory_game(difficulty_value)
        if game_value == 2:
            play_guess_game(difficulty_value)
        if game_value == 3:
            play_currency_roulette_game(difficulty_value)
        want_to_play = user_play_again()
