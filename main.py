try:
    user = "Hello world!"
    test = user.split()
    resList = []
    temp = ""
    for item in test:
        
        if item[0].isalpha() and item[0].islower():
            temp = item[0].upper() + item[1:]
        if item[0].isalpha() and item[0].isupper():
            temp = item[0].lower() + item[1:]
        resList.append(temp)
    resList.reverse()
    res = " ".join(resList)
    print(res)
except Exception as e:
    print(e)
