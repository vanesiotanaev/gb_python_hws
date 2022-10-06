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
dictionary = {}

# Открываем файл, но, чтобы он правильно считывался, имеем в виду кодировку

path = 'file4_1.txt'
file = open(path, 'r', encoding='utf-8')
char_list = ''
for line in file:
    for item in line:
        char_list += item

# Пройдемся по каждому элементу строки
new_char_string = ''
for item in range(0, len(char_list)):
    if char_list[item] in list_indexes:
        dictionary[char_list[item]] = None
print(dictionary)

digits = ''
for i in range(len(char_list)):
    if (char_list[i] == 'x' and (char_list[i-1] == '+')):
        digits += '1'
    if (char_list[i].isdigit() == True and (not char_list[i] in list_indexes)) or (char_list[i] == '-'):
        digits += char_list[i]
    else:
        digits += ' '
print(digits)

digits_list = digits.split(' ')
digits_list.remove('0')

coefficients = []
for element in digits_list:
    if element != '':
        coefficients.append(element)
for i in range(0, len(coefficients)):
    if coefficients[i] == '-':
        coefficients[i] = -1
for i in range(0, len(coefficients)):
    coefficients[i] = int(coefficients[i])
print(coefficients)
count = 0
for i in dictionary:
    for j in range(count, len(coefficients)):
        dictionary[i] = coefficients[j]
        count += 1
        break
        
print(dictionary)
# Конвертация
# for item in range(0, len(char_list)):
#   if char_list[item] in list_indexes:
        # for j in range(0, len(list_indexes)):
        #     if list_indexes[j] == char_list[item]:
        #         new_char_string += str(j) # Перезаписываем в новую строку
    # else:
    #     new_char_string += char_list[item] 
# print(new_char_string)