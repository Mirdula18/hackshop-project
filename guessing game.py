import random

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == "exit":
        print("Exiting the game")
        exit()
    return user_input

def get_validated_input(prompt, expected_type=int, default=None, allowed_values=None):
    while True:
        user_input = get_input(prompt)
        if not user_input and default is not None:
            return default
        
        if allowed_values and user_input.lower() in allowed_values:
            return user_input.lower()
        
        if expected_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Enter a valid number or type 'exit' to quit.")
        else:
            print(f"Enter one of the following options:{','.join(allowed_values)} or type 'exit' to quit.") 

def value_range():
    global start,end
    start = get_validated_input("Enter the start value of the range( or type 'exit' to quit):")
    end=get_validated_input("Enter the end value of the range(or  type 'exit' to quit):")
    if start > end:
        print("Invalid range. The start value must be less than the end value.")
    random_num = random.randint(start,end)    
    return random_num
    
def guess_user(random_num,tries):
    for i in range(tries):
        user_guess_num = get_validated_input("Enter a number you guess(or type 'exit' to quit):")
        if user_guess_num == random_num:
            print("Your guess is right!")
            break
        elif user_guess_num < start or user_guess_num > end:
            print("Invalid range number.")
        else:
            print("Better luck next time:)")
    else:
        print("You're out of tries. The correct number is:",random_num)

def guess_computer(random_num,tries):
    user_num = 0
    user_num = get_validated_input("Enter your number(or type 'exit' to quit):")
    low = start
    high = end
    while True:
        mid = (low+high)//2
        guess = input(f"Is {mid} the number you guessed (yes/no):").lower()          
        if guess == "yes":
            print("Computer won!")
            break
        elif guess == "no":
            high_or_low = input(f"Is the number hight or low than {mid} (high/low):").lower()

            if high_or_low == "high":
                low = mid + 1
            elif high_or_low == "low":
                high = mid - 1
            else:
                print("Invalid input. Type high or low:")
        else:
            print("Invalid input. Type high or low:")                              

def guess_game():
    print(open("rules.md").read())
    game_type = get_validated_input("Choose game type(User/Computer/type 'exit' to quit):",
          expected_type = str,allowed_values = ("user","computer"))
    tries = get_validated_input("Enter the number of tries(or type'exit' to quit):")
    random_num = value_range()
    if game_type == "user":
        guess_user(random_num,tries)
    elif game_type == "computer":
        guess_computer(random_num,tries)  

guess_game()