import string
import random

QUESTIONS = {
    "When was the first known use of the word 'quiz'": ["1781", "1771", "1871", "1881"],
    "Which built-in function can get information from the user": [
        "input",
        "get",
        "print",
        "write",
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for",
        "while",
        "each",
        "loop",
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}
num_correct = 0
for question, answers in QUESTIONS.items():
    correct = answers[0]
    random.shuffle(answers)

    coded_answers = dict(zip(string.ascii_lowercase, answers))
    valid_answers = sorted(coded_answers.keys())

    for code, answer in coded_answers.items():
        print(f"  {code}) {answer}")

    while (user_answer := input(f"\n{question} ")) not in valid_answers:
        print(f"Please answer one of {', '.join(valid_answers)}")

    if coded_answers[user_answer] == correct:
        print(f"Correct, the answer is {user_answer!r}\n")
        num_correct += 1
    else:
        print(f"No, the answer is {correct!r}\n")

print(f"You got {num_correct} correct out of {len(QUESTIONS)} questions")
