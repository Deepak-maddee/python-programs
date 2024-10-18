import random

words = ["chethan", "deepak", "harish", "jeevan"]

def game():
    c_word = random.choice(words)
    attempt = 5
    guessed = False
    guess: list[str] = []

    while not guessed and attempt > 0 :

        progress = "".join([l if l in guess else "_" for l in c_word])
        print(progress)
        if progress == c_word:
            guessed = True
            break

        ltr = input("Enter you guess :")

        if not ltr.isalpha() :
            print("invalid character")
            attempt -= 1
        elif ltr in guess:
            print("you have already guessed the letter")
        elif ltr in c_word:
            guess.append(ltr)
        else:
            print("incorred character")
            attempt -= 1
        print("remaining attempts : ", attempt)

    if guessed:
        print('You guessed the word correctly!')
    else:
        print("You ran out of attempt, better luch next time!")

if __name__ == "__main__":
    game()

"""


"""
