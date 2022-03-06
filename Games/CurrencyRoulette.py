import requests
from HelperMethods import get_verified_value_from_user, print_with_delay, print_faces, check_if_user_ready
from time import sleep
from HelperMethods import generate_random_int_between


def get_current_shekel_rate():
    response = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=fe181140-5a5a-11ec-8b0e-b1cca86f3e7e"
                            "&base_currency=USD")
    response.raise_for_status()
    json_response = response.json()
    json_data_response = json_response["data"]
    return float(json_data_response["ILS"])


def get_money_interval(difficulty):
    curr_rate = get_current_shekel_rate()
    rand_value = generate_random_int_between(1, 100)
    print_with_delay("The random USD amount for which you need to calculate it's current value in ILS is...", 8, 2.5)
    print_with_delay(str(rand_value), 8, 1)
    real_amount = int(round(curr_rate * rand_value, 1))
    return real_amount - (5 - difficulty), real_amount + (5 - difficulty)


def get_guess_from_user():
    print_with_delay("Now give me you best guess!", 15, 1)
    user_guess = get_verified_value_from_user(3, "int", "Your guess for the value in ILS is: ", 9999)
    sleep(2.5)
    return user_guess


def check_result(num_range, number):
    print_with_delay(f"The actual value in ILS is: ", 8, 4)
    print_with_delay(f"{int((num_range[0] + num_range[1]) / 2)}...", 4, 3)
    if int(num_range[0]) <= int(number) <= int(num_range[1]):
        print_with_delay("WOW!!!", 10, 1.5)
        print_with_delay("You've made it!!!", 10, 1)
        print_faces("happy")
        return True
    else:
        print_with_delay("Sorry :(", 10, 1)
        print_with_delay("You didn't quite get it right", 6, 1)
        print_with_delay("Better luck next time!", 6, 0.5)
        print_faces("sad")
        return False


def play(difficulty):
    print_with_delay("You are about to be presented with a random number between 1 and 100.\n"
                     "You will be asked to guess its value in ILS based on the current USD to ILS exchange rate."
                     "\n", 10, 3)
    print_with_delay("\nGOOD LUCK!", 10, 1)
    check_if_user_ready()
    money_interval = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    return check_result(money_interval, user_guess)
