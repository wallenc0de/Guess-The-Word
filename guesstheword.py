# Simple 'Guess The Word' game that can be used for practice purpose]

Questions = [
    ["1) What's the name of the animal that has a long neck?: ", "Giraffe"],
    ["2) Whats the name of the fruit that Steve Jobs used for his company?: ", "Apple"],
    ["3) What is the name of the company that makes operational systems in C++?: ", "Microsoft"]
]

a = 0

def y_n():
    while True:
        yes_no = input('Are you ready? (Y/N): ')
        if yes_no == 'Y':
            print('\n')
            start_game(a)
            break;
        elif yes_no == 'N':
            print('Okay, ending the program.')
            break;
        else:
            print('Error.')

def start_game(a):
    while a <= 2:
        if a == 0:
            word = input(Questions[0][0])
            if word == Questions[0][1]:
                print('You guessed the word. The word was: ' + Questions[0][1] + '.\n')
                a += 1
            else:
                end_game()
                break;

        if a == 1:
            word = input(Questions[1][0])
            if word == Questions[1][1]:
                print('You guessed the word. The word was: ' + Questions[1][1] + '.\n')
                a += 1
            else:
                end_game()
                break;

        if a == 2:
            word = input(Questions[2][0])
            if word == Questions[2][1]:
                print('You guessed the word. The word was: ' + Questions[2][1] + '.\n\nYOU WON THE GAME.')
                break;
            else:
                end_game()
                break;

def end_game():
    print('You did not guess the word. Game Over.')

y_n()
