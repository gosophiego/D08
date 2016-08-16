import sys, random

def guess_game():
    # Generate a random number based of the length of sys.argv[1]
    try:
        length = len(sys.argv[1])
    except IndexError:
        length = 1
    finally:
        answer = random.randint(000, (10**length-1))

    # Print welcome message and let the user guess his/her first guess
    print ('Let\'s play the mimsmind0 game.')
    n = 0
    user_input = input('Guess a {}-digit number: '.format(length))


    while True:
        # Validate the user's guess is an interger
        try:
            user_input = int(user_input)
        except ValueError:
            print ('Please enter an integer instead.')
            user_input = input('Guess a {}-digit number: '.format(length))

        # Evaluate the guess, whether correct, and if incorrect, provide a hinter(higher/lower)    
        else:
            if user_input == answer:
                return print('Congratulations! You guessed the correct number in {} tries.'.format(n))
            else:
                if user_input < answer:
                    user_input = input('Try again. Guess a higher number: ')
                elif user_input > answer:
                    user_input = input('Try again. Guess a lower number: ')
        finally:
            n += 1


def main(): 
    guess_game()

if __name__ == '__main__':
    main()