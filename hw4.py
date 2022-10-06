# 1. Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# Первый (точный, но громоздкий) вариант

# def accurate_value(value, accuracy):
#     list = ['0.1', '0.01', '0.001', '0.0001', '0.00001', '0.000001', '0.0000001', '0.00000001', '0.000000001', '0.0000000001']
#     possible_accuracy = set(list)
#     while not accuracy in possible_accuracy:
#         accuracy = str(input('Вы ввели недопустимую точность d. Введите точность d от 0.1 до 0.0000000001 ! : '))
#     accuracy = len(accuracy[2:])
#     value = str(value)
#     multiplier = 0
#     if value[0] == '-':
#         value = value[1:]
#         multiplier = -1
#     value = float(value)
#     first_half = str(int(value))
#     second_half = str(value % 1)[1:2+accuracy]
#     full_accurate_value = float(first_half + second_half)
#     if multiplier == -1:
#         full_accurate_value *= multiplier
    
#     return full_accurate_value

# Второй вариант

# def accurate_value(value, accuracy):
#     decimal_places = 0
#     while accuracy < 1:
#         accuracy *= 10
#         decimal_places += 1
#     value = round(float(value), decimal_places)
    
#     return value


# user_value = -3.14159265
# user_accuracy = float(input('Введите желаемую точность d (от 0.1 до 0.0000000001): '))
# print(accurate_value(user_value, user_accuracy))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def prime_factors(N):
#     while N <= 0:
#         N = int(input(f'"{N}" не является натуральным числом! Введите натуральное число: ')) 
#     while N == 1:
#         N = int(input(f'"1" нельзя разложить на простые множители, т.к. у него всего один делитель! Введите натуральное число != 1: '))
#     list1 = []
#     for i in range(2, N+1):
#         list1.append(i)
#     list2 = []
#     for item in list1:
#         count = 0
#         for i in range(1, item+1):
#             if item % i == 0:
#                 count += 1
#         if count == 2:
#             list2.append(item)
#     prime_factors = frozenset(list2)
#     list3 = []
#     for i in range(2, N+1):
#         if i in prime_factors and (N % i == 0):
#             list3.append(i)
            
#     return list3



# user_value = int(input("Введите натуральное число, которое нужно разложить на простые множители: "))
# print(f'У числа {user_value} есть простые множители: {prime_factors(user_value)}')

# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# def unique_elements_sequence(sequence):
#     list_sequence = list(str(sequence))
#     unique_sequence_list = list(set(list_sequence))
#     final_unique_list = []
#     for item in unique_sequence_list:
#         count = 0
#         for element in list_sequence:
#             if element == item:
#                 count += 1
#         if count == 1:
#             final_unique_list.append(int(item))
#     final_unique_list.sort()

#     return final_unique_list


# user_sequence = 1113384455229
# print(f"Неповторяющиеся цифры в последовательности [{user_sequence}]: {unique_elements_sequence(user_sequence)}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# import random

# def degree(a):
    
#     indexes = {"0": "\u2070",
#            "1": "\u00B9",
#            "2": "\u00B2",
#            "3": "\u00B3",
#            "4": "\u2074",
#            "5": "\u2075",
#            "6": "\u2076",
#            "7": "\u2077",
#            "8": "\u2078",
#            "9": "\u2079",
#            "-": "\u207B"
#            }

#     degrees = ""
#     temp = str(a)
#     for char in temp:
#         degrees += indexes[char] or ""
#     return degrees

# def generate_equation(k):
#     power_keys = []
#     for i in range(k, -1, -1):
#         power_keys.append(i)
    
#     equation = ''
#     dictionary = dict.fromkeys(power_keys)
#     plus_minus = ['-', '+']
#     for key in dictionary:
#         dictionary[key] = random.randint(0, 5)
#         if dictionary[key] > 1 and key > 1:
#             equation += f'{str(dictionary[key])}x{degree(key)}{random.choice(plus_minus)}'
#         elif dictionary[key] == 1 and key > 1:
#             equation += f'x{degree(key)}{random.choice(plus_minus)}'
#         elif dictionary[key] > 1 and key == 1:
#             equation += f'{str(dictionary[key])}x{random.choice(plus_minus)}'
#         elif dictionary[key] == 1 and key == 1:
#             equation += f'x{random.choice(plus_minus)}' 
#         elif dictionary[key] > 1 and key == 0:
#             equation += f'{str(dictionary[key])}'
#         elif dictionary[key] == 0:
#             key -= 1
#     if equation[-1] == '0':
#         equation = equation[:-1]
#     elif equation[-1] == '+' or equation[-1] == '-':
#         equation = equation[:-1]              
#     equation += '=0'

#     return equation

# user_k = int(input("Введите натуральную степень k: "))
# user_equation = generate_equation(user_k)
# print(user_equation)

# # !!! Как записать в файл закодированную в UTF-8 строку !!!
# path = 'file4_1.txt'
# file = open(path, 'w', encoding='utf-8') 
# file.write(user_equation)
# file.close()

# path = 'file4_2.txt'
# file = open(path, 'w', encoding='utf-8') 
# file.write(user_equation)
# file.close()

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079"
           }
# Делаем из словаря список со значениями (без ключей)

list_indexes = list(indexes.values())
print(list_indexes)

# Открываем файл, но, чтобы он правильно считывался, имеем в виду кодировку

path = 'file4_1.txt'
file = open(path, 'r', encoding='utf-8')
char_list = ''
for line in file:
    for item in line:
        char_list += item
print(char_list)

# Пройдемся по каждому элементу строки
new_char_string = ''
for item in range(0, len(char_list)):
    if char_list[item] in list_indexes:
        for j in range(0, len(list_indexes)):
            if list_indexes[j] == char_list[item]:
                new_char_string += str(j)
    else:
        new_char_string += char_list[item]
print(new_char_string)

