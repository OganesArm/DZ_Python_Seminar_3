# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:   [2, 3, 4, 5, 6] => [12, 15, 16];   [2, 3, 5, 6] => [12, 15]

num = [2, 3, 4, 5, 6]
def sum_odd_index(num):
    sum = 0
    j=-1
    result = []
    for i in range(len(num)):
        if i<len(num)/2:
            sum = num[i] *num[j-i]
            result.append(sum)       
    print(f"Сумма на нечётных позициях: {result}")

sum_odd_index(num)
