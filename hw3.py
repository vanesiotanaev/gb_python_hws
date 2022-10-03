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

# def multiply_pairs(list):
#     new_list = []
#     multiplication = 0
#     i = 0
#     j = len(list)-1
#     while i < j:
#         multiplication = list[i] * list[j]
#         new_list.append(multiplication)
#         i += 1
#         j -= 1
#     if len(list) % 2 != 0:
#         new_list.append(list[i]*list[i])

#     return new_list

# user_list = [2, 3, 4, 5, 6]
# result = multiply_pairs(user_list)
# print(f"Список, состоящий из произведений пар чисел списка {user_list} выглядит так: {result}.")

# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем)

# def max_min_difference(list):
#     new_list = []
#     difference = 0
#     for item in list:
#         a = str(int(item // 1))
#         b = str(item)
#         round_len = len(b) - len(a) - 1
#         if item % 1 != 0:
#             new_list.append(round(item % 1, round_len))
#     difference = find_max(new_list) - find_min(new_list)

#     return difference

# def find_min(list):
#     min = list[0]
#     for item in list:
#         if item <= min:
#             min = item
    
#     return min

# def find_max(list):
#     max = list[0]
#     for item in list:
#         if item >= max:
#             max = item
    
#     return max

# user_list = [1.1, 1.2, 3.1, 5, 10.01]
# result = max_min_difference(user_list)
# print(f'Разница между максимальным и минимальным значением дробной части элементов списка {user_list} равна {result}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def decimal_to_binary(value):
#     binary_list = []
#     while value > 0:
#         binary_list.append(value % 2)
#         value //= 2
#     i = 0
#     j = len(binary_list) - 1
    
#     while i < j:
#         temp = binary_list[i]
#         binary_list[i] = binary_list[j]
#         binary_list[j] = temp
#         i += 1
#         j -= 1
#         binary_string = ''
#     for item in binary_list:
#         binary_string += str(item)

#     return binary_string

# print(decimal_to_binary(75))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def also_negative_fibonacci(value):
    if value != 0:
        positive_list = [0, 1]
        for n in range(2, value + 1):
            positive_list.append(positive_list[n - 1] + positive_list[n - 2])
        negative_list = list(positive_list) # Важно! Чтобы списки не были связаны и не содержали одно и то же, нужно скопировать
                                            # в negative_list содержимое positive_list через list() !!!!!!!!!!!!!!!!!!!!!!!!!!!
        for n in range (2, len(negative_list), 2):
            negative_list[n] *= (-1)
        negative_list.pop(0)

        i = 0
        j = len(negative_list) - 1
        while i < j:
            temp = negative_list[i]
            negative_list[i] = negative_list[j]
            negative_list[j] = temp
            i += 1
            j -= 1

        full_list = negative_list + positive_list
        print(full_list)

        return full_list
    else:
        print("Последовательности Фибоначчи для 0 элементов не существует! ")




user_value = int(input("Введите число: "))
also_negative_fibonacci(user_value)