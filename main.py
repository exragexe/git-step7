

try:
    text = input("Ведіть текст:")
    znak = input("Введіть знак який ви шукаєте:")
    def check (text, znak):
        if not text:
            return 0
        elif text[0] == znak:
            return 1 + check(text[1:], znak)
        else:
            return check(text[1:], znak)

    print(f"Кількість {znak} в тексті - {check(text, znak)}")

except Exception as e:
    print(e)
