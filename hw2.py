# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def SumValueNumbers(value):
#     if value == 0:
#         return 0
#     if value < 0:
#         value *= (-1)
#     if value % 1 != 0:
#         first_half = int(value - value%1)
#         multiplicator = len(str(value)) - len(str(first_half)) - 1
#         value = int(round(value * (10**multiplicator), multiplicator))
#     sum = 0
#     while not value < 10:
#         sum = int(sum + value%10)
#         value = int(value/10)
#     sum = sum + value
    
#     return sum
    
# user_value = float(input("Введите любое вещественное число: "))
# user_sum = SumValueNumbers(user_value)
# print(f'Сумма цифр в введенном числе равна {user_sum}!')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def Factorial(n):
#     list = []
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#         list.append(fact)
    
#     return list

# user_n = int(input("Введите число N: "))
# user_list = Factorial(user_n)
# print(user_list)

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# def NumbersList(n):
#     sum = 0
#     list = []
#     for i in range(n):
#         list.append(round(((1+1/n)**n), 2))
#         sum = round(sum + ((1+1/n)**n), 2)
#     print(list)
#     print(sum)

# NumbersList(5)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

def CreateList(n):
    list = []
    for i in range(n):
        list.append(random.randint(-n, n))

    print(list)
    
    return list

def FindElements(list):
    multiplication = 1
    file = open('file.txt', 'r')
    for line in file:
        a = int(str(line))
        if a < len(list):
            print(f"Под индексом {a} в списке находится элемент {list[a]}!")
            multiplication *= list[a]
        else:
            print(f"Элемента с индексом {a} не существует в списке размером {len(list)}!")
            
    print(f"Произведение найденных элементов равно {multiplication}!")

user_n = int(input('Введите число N: '))
user_list = CreateList(user_n)
FindElements(user_list)

# # 5. Реализуйте алгоритм перемешивания списка.

# import random

# def MixList(list):
#     new_list = []
#     while len(new_list) < len(list):
#         rand = random.choice(list)
#         while not rand in new_list:
#             new_list.append(rand)
        
#     return new_list



# user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print()
# print(f"Default-список выглядит так: {user_list}")
# print()
# new_user_list = MixList(user_list)
# print(f"Перемешанный список выглядит так: {new_user_list}")
# print()