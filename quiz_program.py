# define the dictionary that stores the questions and answers we want to show the user
# define a variable that tracks the score of the user
# loop through the dictionary using the key/value pairs
# display each question to the user and allow them to answer
# tell the user if they selected the right or wrong answer
# show the final result when the quiz is complete ie all questions have been asked

quiz_questions_answers = {
    "Question#1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "Question#2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "Question#3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "Question#4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "Question#5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "Question#6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "Question#7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}


def quiz_program_run():
    score = 0

    for key, value in quiz_questions_answers.items():
        print(value['question'])
        answer = input("What is your answer?: ")

        if answer.lower() == value['answer'].lower():
            print("That is correct!")
            score += 1
            print("Your score is: " + str(score) + "/" + str(len(quiz_questions_answers)))
        else:
            print("That is incorrect, sorry!")
            print("The correct answer is: " + value['answer'])
            print("Your score is: " + str(score) + "/" + str(len(quiz_questions_answers)))

    print("Congratulations! You have finished this quiz!")


quiz_program_run()
