"""
CONSTANT PASSWORD_LENGTH_THRESHOLD = 6

FUNCTION main():
    password = get_password()
    min_length = INPUT("Enter password minimum length (press Enter to use PASSWORD_LENGTH_THRESHOLD): ")
    IF min_length is empty:
        min_length = PASSWORD_LENGTH_THRESHOLD
    ELSE:
        min_length = CONVERT min_length TO INTEGER

    WHILE LENGTH(password) < min_length:
        PRINT "Non Conformance"
        password = get_password()

    PRINT "*" repeated LENGTH(password)

FUNCTION get_password():
    RETURN CONVERT INPUT("Enter your password: ") TO STRING


main()

"""



PASSWORD_LENGTH_THRESHOLD = 6


def main():
    password = get_password()
    min_length = int(input(
        f"Enter password minimum length (press Enter to use {PASSWORD_LENGTH_THRESHOLD}): ") or PASSWORD_LENGTH_THRESHOLD)

    while len(password) < min_length:
        print("Non Conformance")
        password = get_password()

    print("*" * len(password))


def get_password():
    return str(input("Enter your password: "))


main()
