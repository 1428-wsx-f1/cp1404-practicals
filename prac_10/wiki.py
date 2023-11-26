"""
Wikipedia API
Estimate: 45 minutes
Actual: 54 minutes
"""

import wikipedia


def main():
    """Search wikipedia with user input and get page summary"""
    user_input = input("> ")
    while user_input != "":
        try:
            wikipedia_page = wikipedia.page(user_input, auto_suggest=False)
            print(f"{wikipedia_page.title}\n{wikipedia_page.summary}\n{wikipedia_page.url}")
        except wikipedia.exceptions.DisambiguationError:
            print("Disambiguation Error")
        except wikipedia.exceptions.PageError:
            print("Page Error")
        user_input = input("")


main()
