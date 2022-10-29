

try:
    user = input("-> ")
    numbers = 0
    for sign in user:
        if sign.isdigit():
            numbers += 1
    print(f"Цифри:{numbers}, Букви:{len(user)}")
except Exception as e:
    print(e)