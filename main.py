

try:
    text = "The majority of the victims were Jews, but many other people were killed as well, \n including Poles" \
           " Gypsies, Soviet prisoners of war and tens of thousands of men and women who were killed because they were gay."
    print(text)
    str_text = text.split(" ")

    print(len(str_text)-1) #віднімаю 1 через те що спліт добавляє \n в масив і лен його бачить а це не частина тексту


except Exception as e:
    print(e)
