# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


list_numbers= [1, 1, 2, 3, 4, 5, 5]
clear_list = []



for i in list_numbers:
    if(list_numbers.count(i) < 2):
        clear_list.append(i)
   
print(clear_list)

print([i for i in list_numbers if list_numbers.count(i) < 2]) #list comprehension