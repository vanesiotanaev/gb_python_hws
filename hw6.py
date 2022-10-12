# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def SumValueNumbers(value):
    return sum(int(value[i]) for i in range(len(str(value))) if value[i].isdigit())
    
user_value = input("Введите любое вещественное число: ")
print(f'Сумма цифр в введенном числе равна {SumValueNumbers(user_value)}!')