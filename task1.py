# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:       [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

num = [2, 3, 5, 9, 3]
def sum_odd_index(num):
    sum = 0
    for i in range(len(num)):
        if i % 2 != 0:
            sum += num[i]
    print(f"Сумма на нечётных позициях: {sum}")

sum_odd_index(num)
