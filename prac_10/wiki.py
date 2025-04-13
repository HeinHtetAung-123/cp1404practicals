import wikipedia
def main():
    """Prompting the user to search on Wikipedia """
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title)
            print(page.title)
            print(wikipedia.summary(title, sentences=1))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)
        except wikipedia.exceptions.PageError as error:
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print(f"Error: {error}")
        title = input("\nEnter page title: ").strip()
    print("You entered the blank one.")
    print("Thank you.")

main()
