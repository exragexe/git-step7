

try:
    text = input("Введіть текст: ")
    slowo = input("Введіть слово яке ви хочете замінити: ")
    substitute = input(f"Введіть слово яким ви хочете замінити {slowo}: ")

    res = text.replace(slowo, substitute)
    if slowo not in text:
        print("Такого слова немає в тексті")
    else:
        print(res)

except Exception as e:
    print(e)