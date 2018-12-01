# User can pick six numbers
# Lottery chooses six random
# Match choices to lottery numbers
# Calculate winnings

import random

def menu():
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You guessed {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))
    

def get_player_numbers():
    number_csv = input("Enter six numbers, separated by comms: ")
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set



def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values
        

menu()
