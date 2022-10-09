
# Написать программу, удаляющие из текста содержащие "абв"
str_text = 'я люблю морковьабв, мороженное иабв в стаканчике'
list_str = str_text.split(' ')
new_str = ''

for i in list_str:
    if('абв' not in i):
        new_str += i + " "


print(new_str)


print([new_str for new_str  in list_str if ('абв' not in new_str)]) #list comprehension

