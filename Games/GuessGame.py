from HelperMethods import generate_random_int_between, print_with_delay, get_verified_value_from_user


def generate_number(difficulty):
    return generate_random_int_between(1, difficulty + 1)


def get_guess_from_user(difficulty):
    return get_verified_value_from_user(3, "int", "Your guess for the number is: ", difficulty + 1)


def compare_results(secret, guess):
    if secret == guess:
        print_with_delay("You are correct!!!", 5, 0)
        return True
    else:
        print_with_delay(f"Sorry, the secret number was {secret}.\nBetter luck next time!", 15, 0)
        return False


def play(difficulty):
    print_with_delay(f"You will now choose a number between 1 - {difficulty + 1} "
                     f"trying to guess the secret number...", 10, 1)
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)
