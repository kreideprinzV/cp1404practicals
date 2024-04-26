

import wikipedia

def get_page_summary(title):
    """Fetches and prints the Wikipedia page summary, title, and URL based on the given title."""
    try:
        # Fetch the page with autosuggest turned off to get exact matches if possible
        page = wikipedia.page(title, auto_suggest=False)
        print("\nTitle:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("\nDisambiguationError: The title refers to multiple entries.")
        print("Some suggestions are:", e.options[:5])  # Show top 5 suggestions
    except wikipedia.exceptions.PageError:
        print("\nPageError: The page could not be found.")
    except Exception as e:
        print("\nAn error occurred:", str(e))

def main():
    while True:
        title = input("Enter a Wikipedia page title or search phrase (or just hit enter to quit): ")
        if not title.strip():
            break
        get_page_summary(title)

if __name__ == "__main__":
    main()
