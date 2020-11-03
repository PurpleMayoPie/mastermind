import random
import re

def random_code():
    code = [0, 0, 0, 0]
    for i in range(0, 4):
        random_number = random.randint(1, 8)        
        code[i] = str(random_number)
    return "".join(code)

def check_repeating_numbers(code):
    list_code = list(code)
    if len(list_code) == len(set(list_code)):
        return False
    else:
        return True

def check_user_guess():
    user_guess = input("Input 4 digit code: ")
    if len(user_guess) != 4 or user_guess.isdecimal() == False:
        print("Please enter exactly 4 digits.")    
        return check_user_guess()
    user_guess = list(user_guess)
    for i in range(len(user_guess)):
        if int(user_guess[i]) == 9 or int(user_guess[i]) == 0:
             print("Please enter exactly 4 digits.")    
             return check_user_guess()
        if user_guess[i].isdecimal() == False:
            print("Please enter exactly 4 digits.")    
            return check_user_guess()
    return "".join(user_guess)

def compare_code(user_guess, code, turns_left):
    correct_np = 0
    count = set(user_guess) & set(code)
    correct_n = ''.join(count)
    guess = list(user_guess)
    numbers = list(code)
    count = set(user_guess) & set(code)
    for i in range(len(code)):
        if numbers[i] == guess[i]:
            correct_np += 1
    if user_guess == code:
          print("Number of correct digits in correct place:    ", correct_np)
          print("Number of correct digits not in correct place:", len(correct_n) - correct_np)
          print("Congratulations! You are a codebreaker!")
          print("The code was: " + code)
          turns_left = 0
          return turns_left
     #pass
    else:
         print("Number of correct digits in correct place:    ", correct_np)
         print("Number of correct digits not in correct place:", len(correct_n) - correct_np)
         print("Turns left:", turns_left)
         return turns_left

def run_game():
    """
    TODO: implement Mastermind code here
    """
    #code = str(1234)

    code = random_code()
    while check_repeating_numbers(code) == True:
        code = random_code()
    #print(code)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    turns_left = 12
    while turns_left > 0:
         user_guess = check_user_guess()
         turns_left -= 1
         compare_code(user_guess, code, turns_left)
         if user_guess == code:
             #  print("Congratulations! You are a codebreaker!")
             #  print("The code was: " + code)
             #  turns_left = 0
             break
    pass


if __name__ == "__main__":
    run_game()
