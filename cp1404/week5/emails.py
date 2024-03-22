"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""


def get_name_from_email(email):
    email_segments = email.split('@')
    name_components = email_segments[0].split('.')
    total_name = " ".join(part.title() for part in name_components)

    return total_name


def main():
    email_dictionary = {}
    email_address = input("Email: ").strip()

    while email_address:
        user_name = get_name_from_email(email_address)
        check = input(f"Is your name {user_name}? (Y/n) ").strip().lower()
        if check != 'n' and check != 'no':
            email_dictionary[user_name] = email_address
        else:
            user_name = input("Name: ").strip().title()
            email_dictionary[user_name] = email_address
        email_address = input("Email: ").strip()

    for user_name, email_address in email_dictionary.items():
        print(f"{user_name} ({email_address})")


main()


