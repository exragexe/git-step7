

try:
    text = input("Введіть текст: ")
    slow = input("Введіть слово яке ви шукаєте: ")

    search = text.count(slow)
    print(f"Кількість {slow} у тексті - {search}")


except Exception as e:
    print(e)

