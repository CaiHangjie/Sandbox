import random
SCORE_LOWER_BOUND = 0
SCORE_UPPER_BOUND = 100
PASS_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90


def main():
    score = get_score("Enter score: ")
    result = check_score(score)

    generated_score = random.randint(SCORE_LOWER_BOUND, SCORE_UPPER_BOUND)
    generated_score_result = check_score(generated_score)
    print(f"Your score is {generated_score}, and it is {generated_score_result}")


def get_score(prompt):
    score = float(input(prompt))
    while score < SCORE_LOWER_BOUND or score > SCORE_UPPER_BOUND:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def check_score(score):
    if score < SCORE_LOWER_BOUND or score > SCORE_UPPER_BOUND:
        return "Invalid score"
    elif score < PASS_THRESHOLD:
        return "Bad"
    elif score < EXCELLENT_THRESHOLD:
        return "Pass"
    else:
        return "Excellent"


main()
