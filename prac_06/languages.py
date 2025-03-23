from prac_06.programming_language import ProgrammingLanguage
def main():
    """Demo test code to show how to use the ProgrammingLanguage class."""
    Python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    Ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    Visual_Basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(Python)
    print(Visual_Basic)
    print(Ruby)
    print()

    languages =  [Python, Ruby, Visual_Basic]

    print("The dynamically typed languages are:")
    dynamic_language = [language.name for language in languages if language.is_dynamic() ]
    for lang in dynamic_language:
        print(lang)
main()