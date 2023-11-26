"""Get user command."""
import wikipedia

page_title = str(input("Page Title: "))

"""Read the user's command until "" is entered."""
while page_title.upper() != "":
    try:
        print(wikipedia.page(page_title, auto_suggest=False).title)
        print(wikipedia.summary(page_title, auto_suggest=False))
        print(wikipedia.page(page_title, auto_suggest=False).url)
    except wikipedia.exceptions.PageError:
        print("Page not found. Please try again.")
    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple pages match this title. Please be more specific. Options include:")
        print(e.options)

    """Get user command."""
    page_title = str(input("Page Title: "))
