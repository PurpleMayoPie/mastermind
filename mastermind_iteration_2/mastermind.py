import random

turns = 0
correct = False
# TODO: Decompose into functions
"""Generate_code creates a code for the user to crack in the run gae function."""
def generate_code():
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code
    

def run_game():
    code = generate_code()
    #print(code)
    turns = 0
    correct = False
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) != 4:
            print("Please enter exactly 4 digits.")
            continue
        if not answer.isdigit():
            print("Please enter exactly 4 digits.")
            continue
        if "0" in answer or "9" in answer:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1    
        if correct_digits_and_position == 4 and turns < 12:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))
            continue
    print("The code was:", code)


if __name__ == "__main__":
   
    run_game()
