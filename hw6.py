# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Использовал comprehension и lambda.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11
    
# value = input("Введите любое вещественное число: ")
# result = lambda user_value: [int(user_value[i]) for i in range(len(str(user_value))) if user_value[i].isdigit()]
# print(f'Сумма цифр в введенном числе равна {sum(result(value))}!')
# print(result)

# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# (использовал map и list comperhension)

# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

a = list(str(input('Введите последоавтельность цифр: ')).strip())
res = list(map(a.count, a))
print([int(a[i]) for i in(range(len(res))) if res[i] == 1 and a[i].isdigit()])
