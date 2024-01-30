"""Генератор випадкових історій"""

# Вступ

"""Ця програма на мові Python читає сюжет із файлу, визначає заповнювачі, заключені в `<` та `>` дужки,
надає користувачеві можливість вказати заміщення для кожного заповнювача і, нарешті, виводить сюжет із внесеними замінами."""

# Читання Сюжету

"""Програма відкриває файл з ім'ям "story.txt" у режимі читання (`"r"`) та зчитує його вміст. Сюжет зберігається у змінній `story`."""

with open("story.txt", "r") as f:
    story = f.read()

# Визначення слів-заповнювачів

"""Програма визначає заповнювачі в сюжеті, шукаючи підстроки, оточені < та > дужками. Вони зберігаються у множині з назвою words."""

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Слова для заміни введені користувем

"""Програма вимагає від користувача ввести заміщення для кожного визначеного заповнювача та зберігає відповіді у словнику з назвою answers."""

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# Заміна слів заповнювачів у сюжеті
"""Програма проходить крізь кожен заповнювач у сюжеті та замінює його відповідним користувацьким відповіддю."""

for word in words:
    story = story.replace(word, answers[word])

print(story)