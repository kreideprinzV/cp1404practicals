# languages.py
from programming_language import ProgrammingLanguage

def main():
    """Main program to demonstrate the use of the ProgrammingLanguage class."""
    # Create instances of ProgrammingLanguage
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print(f"\nTesting the __str__ method:")
    for language in languages:
        print(language)

main()
