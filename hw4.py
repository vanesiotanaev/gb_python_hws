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

def accurate_value(value, accuracy):
    decimal_places = 0
    while accuracy < 1:
        accuracy *= 10
        decimal_places += 1
    value = round(float(value), decimal_places)
    
    return value


user_value = -3.14159265
user_accuracy = float(input('Введите желаемую точность d (от 0.1 до 0.0000000001): '))
print(accurate_value(user_value, user_accuracy))