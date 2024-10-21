#PYTHON QUIZ GAME
#consisting of tuples and lists using a 2D collection
#questions,answers,options,guesses,score

questions = (("1. Which is the biggest number: "),
    ("2. What is the first alphabet in the English alphabet: "),
    ("3. How much is 8*9: "),
    ("4. Which animal lays the largest egg: "),
    ("5. Which is the national bird of India: "),
    ("6. Which is the national animal of India: "),
    ("7. What is the national dish of India: "),
    ("8. Who is the best comedian of Tollywood: "),
    ("9. How many bones are in the human body: "),
    ("10. How many elements are in the periodic table: "))

options = (("A.10", "B. 11", "C. 13", "D. 15"),
    ("A. A", "B. B", "C. C", "D. Z"),
    ("A. 56", "B. 72", "C. 78", "D. 22"),
    ("A. Elephant", "B. Ostrich", "C. Whale", "D. Peacock"),
    ("A. Peacock", " B. Crow", "C. Owl", "D. Pigeon"),
    ("A. Zebra", "B. Lion", "C. Snake", "D. Tiger"),
    ("A. Chicken Tikka Masala", "B. Bisi Bele Bath", "C. Pongal", "D. Chitranna"),
    ("A. Brahmanandam", "B. Sunil", "C. Satya", "D. Ali"),
    ("A. 206", "B. 209", "C. 310", "D. 255"),
    ("A. 119", "B. 115", "C. 118", "D. 110"))

answers = ("D", "A", "B", "B", "A", "D", "B", "A", "A", "C")

guesses = []
score = 0
question_num = 0

reply = input("Interested to play a quiz game? (Y/N)").upper()
if not reply == "Y":
    print("Alright! Play when your mood is on.")
else:
    for question in questions:
        print("--------------------")
        print()
        print(question)
        print()

        for option in options[question_num]:
            print(option)

        guess = input("Enter your guess: (A,B,C,D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score+=1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f" Option {answers[question_num]} is the correct answer to this question")
        question_num += 1

    print("-----------------------------")
    print("          RESULTS            ")
    print("-----------------------------")

    print("answers: ", end = "")
    for answer in answers:
        print(answer,end = " ")
    print()

    print("guesses: ", end = "")
    for guess in guesses:
        print(guess,end = " ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")
