

try:
    user = input("Введіть рядок: ")
    if user[::1] == user[::-1]:
        print(f"{user} - є паліндромом")
    else:
        print("не є паліндромом")


except Exception as e:
    print(e)