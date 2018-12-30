# Simple 'Guess The Word' game that can be used for practice purpose]

Questions = [
    ["1) What's the name of the animal that has a long neck?: ", "Giraffe"],
    ["2) Whats the name of the fruit that Steve Jobs used for his company?: ", "Apple"],
    ["3) What is the name of the company that makes operational systems in C++?: ", "Microsoft"]
]


def y_n():
    while True:
        yes_no = input('Are you ready? (Y/N): ')
        if yes_no == 'Y':
            print('\n')
            start_game()
            break
        elif yes_no == 'N':
            print('Okay, ending the program.')
            break
        else:
            print('Error.')

def start_game():
    for question, answer in Questions:
            word = input(question)
            if word == answer:
                print('You guessed the word.\n')
            else:
                end_game()
                break    

def end_game():
    print('You did not guess the word. Game Over.')

y_n()
