import wikipedia

while True:
    search_query = input("Please enter the page title or search phrase (enter blank to exit)：")
    if not search_query.strip():
        break

    try:
        page = wikipedia.page(search_query, auto_suggest=False)
        print("Title:", page.title)
        print("Abstract:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Unable to obtain")
        options = e.options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input(" Enter the number of the option：")
        try:
            choice = int(choice)
            page = wikipedia.page(options[choice - 1], auto_suggest=False)
            print("Title:", page.title)
            print("Abstract:", page.summary)
            print("URL:", page.url)
        except (ValueError, IndexError):
            print("Try again。")
    except wikipedia.exceptions.PageError:
        print("Try again。")
