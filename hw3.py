# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# def sum_odd_indices(list):
#     sum = 0
#     for i in range(0, len(list), 2):
#         sum += list[i]
    
#     return sum

# user_list = [3, 0, 0, 7, 1, 9]
# result = sum_odd_indices(user_list)
# print(f"Сумма элементов, стоящих на нечетных позициях в списке {user_list} равна {result}.")

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def multiply_pairs(list):
    new_list = []
    multiplication = 0
    i = 0
    j = len(list)-1
    while i < j:
        multiplication = list[i] * list[j]
        new_list.append(multiplication)
        i += 1
        j -= 1
    if len(list) % 2 != 0:
        new_list.append(list[i]*list[i])

    return new_list

user_list = [2, 3, 4, 5, 6]
result = multiply_pairs(user_list)
print(f"Список, состоящий из произведений пар чисел списка {user_list} выглядит так: {result}.")