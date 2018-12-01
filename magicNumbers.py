import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
magic_number = random.randint(1, 5)


def ask_user_and_check_number():
    user_number = int(input("Enter magic number: "))
    if user_number in magic_numbers:
        print("You got it right")
    if user_number not in magic_numbers:
        print("Nope")


def run_program(chances):
    for attempt in range(chances):
        print("This is attempt {}".format(attempt))
        ask_user_and_check_number()

        
try:
    run_program(magic_number)
    print("The program ran ", magic_number, " times.")
except:
    print("You were supposed to enter a number - run the program again")



