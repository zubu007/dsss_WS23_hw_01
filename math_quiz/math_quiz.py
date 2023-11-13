import random


def generate_num1(min, max):
    """
    Returns a random integer from the range [min, max].
    """
    return random.randint(min, max)


def generate_operation():
    """
    Returns a random operator from the set {+, -, *}.
    """
    return random.choice(['+', '-', '*'])


def operation(a, b, o):
    """
    Returns a tuple (p, a), where p is a string representing the problem
    and a is the answer to the problem.
    """
    problem = f"{a} {o} {b}"
    if o == '+': 
        a = a + b   # sum of a and b
    elif o == '-': 
        a = a - b   # difference of a and b
    else: 
        a = a * b   # product of a and b

    return problem, a

def math_quiz():
    """
    Runs a math quiz program that asks the user to solve simple math problems.
    """
    score = 0   # number of correct answers
    task = 3   # number of problems

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(task):
        n1 = generate_num1(1, 10)
        n2 = generate_num1(1, 5.5)
        o = generate_operation()

        PROBLEM, ANSWER = operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")   # ask user for answer
        useranswer = int(useranswer)   # convert useranswer to integer

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1   # increment score by 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{task}")


if __name__ == "__main__":
    math_quiz()
