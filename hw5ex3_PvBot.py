import random

def game():
    possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    dictionary = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    graphics(dictionary)
    count = 0
    if first_move() == 0:
        # Ход игрока
        while len(possible_moves) > 0:
            a = int(input('Ход игрока: '))
            while not str(a) in possible_moves:
                a = int(input('Невозможно сделать ход на эту позицию, т.к. она занята или не существует! Ход игрока А: '))
            else:
                possible_moves.remove(str(a))
                dictionary[a] = 'X'
                graphics(dictionary)
            if win_check(dictionary) == True:
                break
            # Ход компьютера
            if len(possible_moves) > 0:
                computer_move(possible_moves, dictionary)
                graphics(dictionary)
                if win_check(dictionary) == True:
                    break
            count += 1
        else:
            print('Ничья!')
    else:
        # Ход компьютера
        while len(possible_moves) > 0:
            computer_move(possible_moves, dictionary)
            graphics(dictionary)
            if win_check(dictionary) == True:
                break
            # Ход игрока
            if len(possible_moves) > 0:
                a = int(input('Ход игрока: '))
                while not str(a) in possible_moves:
                    a = int(input('Невозможно сделать ход на эту позицию, т.к. она занята или не существует! Ход игрока А: '))
                else:
                    possible_moves.remove(str(a))
                    dictionary[a] = 'X'
                    graphics(dictionary)
                if win_check(dictionary) == True:
                    break
        else:
            print('Ничья!')

def computer_move(moves, dict):
    b = random.randint(1, 9)
    while not str(b) in moves:
        b = random.randint(1, 9)
    moves.remove(str(b))
    dict[b] = 'O'
    print(f'Ход компьютера - позиция {b}!')

def graphics(dict):
    print('-------------')
    print(f'| {dict[1]} | {dict[2]} | {dict[3]} |')
    print('-------------')
    print(f'| {dict[4]} | {dict[5]} | {dict[6]} |')
    print('-------------')
    print(f'| {dict[7]} | {dict[8]} | {dict[9]} |')
    print('-------------')

def first_move():
    first = random.randint(0, 1)
    return first

def win_check(dict):  
    if dict[1] == dict[2] == dict[3] \
        or dict[4] == dict[5] == dict[6] \
            or dict[7] == dict[8] == dict[9] \
                or dict[1] == dict[4] == dict[7] \
                    or dict[2] == dict[5] == dict[8] \
                        or dict[3] == dict[6] == dict[9] \
                            or dict[1] == dict[5] == dict[9] \
                                or dict[3] == dict[5] == dict[7]:
                                    print('Победа!')
                                    return True

game()

