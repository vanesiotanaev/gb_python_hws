# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

# Функция для открытия файла (чтобы он правильно считывался, имеем в виду кодировку)

def open_encoded_file(path):
    file = open(path, 'r', encoding='utf-8')
    char_list = ''
    for line in file:
        for item in line:
            char_list += item
    
    return char_list

def create_code_values_list():
    # Делаем из словаря список со значениями (без ключей)
    code_values_dict = {"0": "\u2070",
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
    code_values_list = list(code_values_dict.values())

    return code_values_list

def create_dictionary_keys(char_list, check_list):
    dictionary = {}
    # Пройдемся по каждому элементу строки
    for item in range(0, len(char_list)):
        if char_list[item] in check_list:
            dictionary[int(reverse_degree(char_list[item]))] = None
    
    return dictionary

def create_primary_coeff_string(char_list, check_list):
    primary_coeff_string = ''
    for i in range(len(char_list)):
        if (i == 0 and char_list[i] == 'x'):
            primary_coeff_string += '1'
        if (char_list[i] == 'x' and (char_list[i-1] == '+')):
            primary_coeff_string += '1'
        if (char_list[i].isdigit() == True and (not char_list[i] in check_list)) or (char_list[i] == '-'):
            primary_coeff_string += char_list[i]
        else:
            primary_coeff_string += ' '
    
    return primary_coeff_string

def create_secondary_coeff_list(coeff_string):
    coeff_list = coeff_string.split(' ')
    coeff_list.remove('0')
    secondary_coefficients_list = []
    for element in coeff_list:
        if element != '':
            secondary_coefficients_list.append(element)
    for i in range(0, len(secondary_coefficients_list)):
        if secondary_coefficients_list[i] == '-':
            secondary_coefficients_list[i] = -1
    for i in range(0, len(secondary_coefficients_list)):
        secondary_coefficients_list[i] = int(secondary_coefficients_list[i])
    
    return secondary_coefficients_list

def create_complete_dict(dictionary, coefficients):
    count = 0
    for i in dictionary:
        for j in range(count, len(coefficients)):
            dictionary[i] = coefficients[j]
            count += 1
            break
        
    return dictionary

def sum_dicts(dict_1, dict_2):
    general_dict = dict_1
    for key, value in dict_2.items():
        if key in dict_1:
            general_dict[key] += value
        else:
            general_dict.update({key: value})
    
    return general_dict

def reverse_degree(a):
    indexes = {"\u2070": "0",
           "\u00B9": "1",
           "\u00B2": "2",
           "\u00B3": "3",
           "\u2074": "4",
           "\u2075": "5",
           "\u2076": "6",
           "\u2077": "7",
           "\u2078": "8",
           "\u2079": "9"
           }

    degrees = ""
    temp = str(a)
    for char in temp:
        degrees += indexes[char] or ""
    
    return degrees           

def dict_sort(dict):

    sorted_dict = {k: v for k, v in sorted(dict.items())}
    items = list(sorted_dict.items())
    sorted_dict2 = {k: v for k, v in reversed(items)}
    print(sorted_dict2)
    
    return sorted_dict2

char_list_1 = open_encoded_file('file4_1.txt')
char_list_2 = open_encoded_file('file4_2.txt')

special_list = create_code_values_list()

dictionary_keys_1 = create_dictionary_keys(char_list_1, special_list)
dictionary_keys_2 = create_dictionary_keys(char_list_2, special_list)

primary_coefficients_1 = create_primary_coeff_string(char_list_1, special_list)
primary_coefficients_2 = create_primary_coeff_string(char_list_2, special_list)

secondary_coefficients_1 = create_secondary_coeff_list(primary_coefficients_1)
secondary_coefficients_2 = create_secondary_coeff_list(primary_coefficients_2)

full_dict_1 = create_complete_dict(dictionary_keys_1, secondary_coefficients_1)
full_dict_2 = create_complete_dict(dictionary_keys_2, secondary_coefficients_2)
print(full_dict_1)
print(full_dict_2)

summed_dict = sum_dicts(full_dict_1, full_dict_2)
print(summed_dict)

sorted_dictionary = dict_sort(summed_dict)
print(sorted_dictionary)


# Конвертация
# for item in range(0, len(char_list)):
#   if char_list[item] in list_indexes:
        # for j in range(0, len(list_indexes)):
        #     if list_indexes[j] == char_list[item]:
        #         new_char_string += str(j) # Перезаписываем в новую строку
    # else:
    #     new_char_string += char_list[item] 
# print(new_char_string)