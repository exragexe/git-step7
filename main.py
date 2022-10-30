

try:
    text = input("Введіть текст: ")
    znak = input("Введіть слово: ")

    if znak not in text:
        print("Слова немає в тексті")
    else:
        res = text.replace(znak, znak.upper())
        print(res)


except Exception as ex:
    print(ex)