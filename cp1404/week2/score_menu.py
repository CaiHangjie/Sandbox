MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_score("Enter your score: ")
    print(MENU)
    choice = get_choice("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score("Enter your score: ")
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = get_choice("Enter your choice: ").upper()
    print("Thank you!")


def get_choice(prompt):
    choice = input(prompt)
    return choice


def get_score(prompt):
    score = float(input(prompt))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


def print_result(score):
    result = check_score(score)
    print(f"Your result is {result}")


def show_stars(score):
    print("*" * int(score))


main()

