def open_file(path):
    file_text = ''
    with open(path, 'r') as file:
        for line in file:
            file_text += line
        file_text_list = file_text.split()
        
    return file_text_list

def letters_work(text):
    count = 0
    temp = text[0]
    string = ''
    for i in range(0, len(text)):
        if text[i] == temp:
            count += 1
        else:
            part_string = str(count) + temp
            count = 1
            temp = text[i]
            string += part_string
    string = string + str(count) + temp
    
    return string

def complex_work(text):
    string = ''
    number = ''
    for i in range(0, len(text)):
        if text[i].isdigit():
            number = str(number) + text[i]
        else:
            number = int(number)
            part_string = text[i] * number
            string += part_string
            number = ''
    
    return string

def file_transformation(file):
    for i in range(0, len(file)):
        if file[i][0].isdigit():
            file[i] = complex_work(file[i])
        else:
            file[i] = letters_work(file[i])
    
    return file

def file_write(path, text):
    with open(path, 'w') as file:
        for item in text:
            file.write(item + '\n')

path_1 = ('file5_4_1.txt')
path_2 = ('file5_4_result.txt')
file_1 = open_file(path_1)
print(f'ДО преобразования: {file_1}')
file_result = file_transformation(file_1)
print(f'ПОСЛЕ преобразования: {file_result}')
file_write(path_2, file_result)
print()
print('См. файлы "file5_4_1" и "file5_4_result" ! ')
print()

