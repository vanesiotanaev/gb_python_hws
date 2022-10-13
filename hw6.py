# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Использовал comprehension и lambda.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11
    
value = input("Введите любое вещественное число: ")
result = lambda user_value: [int(user_value[i]) for i in range(len(str(user_value))) if user_value[i].isdigit()]
print(f'Сумма цифр в введенном числе равна {sum(result(value))}!')
print(result)

# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# (использовал map и list comperhension)

# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# a = list(str(input('Введите последоавтельность цифр: ')).strip())
# res = list(map(a.count, a))
# print([int(a[i]) for i in(range(len(res))) if res[i] == 1 and a[i].isdigit()])

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# (Использовал lambda)

result = lambda xa, ya, xb, yb: round(((xa-xb)**2) + ((ya-yb)**2)) ** 0.5
print(result(int(input("Введите координату Х точки А: ")),int(input("Введите координату Y точки А: ")),\
int(input("Введите координату Х точки B: ")), int(input("Введите координату Y точки B: "))))

# Дополнительная задача с CodeWars.

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    q = min(len(i) for i in s.split())
    
    return q

find_short("fdgfdg dfgdf   123fg g ")

# Дополнительная задача с CodeWars.

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    if number < 0:
        return 0
    else:
        return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution(10))