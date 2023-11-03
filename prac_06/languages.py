"""
Intermediate Exercise, Programming Languages
Estimate: 30 minutes
Actual: 34 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(f"|{python}| |{ruby}|, |{visual_basic}|")

languages = [python, ruby, visual_basic]

print("Dynamic Languages Are:")
for language in languages:
    if language.is_dynamic():
        print(language.language_name)
