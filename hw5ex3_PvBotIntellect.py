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
            while (not str(a) in possible_moves) or dictionary[a] == 'X' or dictionary[a] == 'O':
                a = int(input('Невозможно сделать ход на эту позицию, т.к. она занята или не существует! Ход игрока А: '))
            else:
                possible_moves.remove(str(a))
                dictionary[a] = 'X'
                graphics(dictionary)
            if win_check(dictionary) == True:
                break
            # Ход компьютера
            if len(possible_moves) > 0:
                computer_move(possible_moves, dictionary, count)
                graphics(dictionary)
                if win_check(dictionary) == True:
                    break
            count += 1
        else:
            print('Ничья!')
    else:
        # Ход компьютера
        while len(possible_moves) > 0:
            computer_move(possible_moves, dictionary, count)
            graphics(dictionary)
            if win_check(dictionary) == True:
                break
            # Ход игрока
            if len(possible_moves) > 0:
                a = int(input('Ход игрока: '))
                while not str(a) in possible_moves or dictionary[a] == 'X' or dictionary[a] == 'O':
                    a = int(input('Невозможно сделать ход на эту позицию, т.к. она занята или не существует! Ход игрока А: '))
                else:
                    possible_moves.remove(str(a))
                    dictionary[a] = 'X'
                    graphics(dictionary)
                if win_check(dictionary) == True:
                    break
        else:
            print('Ничья!')

def computer_move(moves, dict, iter):
    print()
    if dict[5] == 'X' and iter == 0:
        list = [1, 3, 7, 9]
        bot_move = random.choice(list)
    elif dict[5] != 'X' and dict[5] != 'O':
        bot_move = 5
    else:
        if dict[1] == dict[4] == 'O' and (dict[7] != 'X' and dict[7] != 'O'):
            bot_move = 7
        elif dict[4] == dict[7] == 'O' and (dict[1] != 'X' and dict[1] != 'O'):
            bot_move = 1
        elif dict[2] == dict[5] == 'O' and (dict[8] != 'X' and dict[8] != 'O'):
            bot_move = 8
        elif dict[5] == dict[8] == 'O' and (dict[2] != 'X' and dict [2] != 'O'):
            bot_move = 2
        elif dict[3] == dict[6] == 'O' and (dict[9] != 'X' and dict[9] != 'O'):
            bot_move = 9
        elif dict[6] == dict[9] == 'O' and (dict[3] != 'X' and dict[3] != 'O'):
            bot_move = 3
        elif dict[1] == dict[2] == 'O' and (dict[3] != 'X' and dict[3] != 'O'):
            bot_move = 3
        elif dict[2] == dict[3] == 'O' and (dict[1] != 'X' and dict[1] != 'O'):
            bot_move = 1
        elif dict[4] == dict[5] == 'O' and (dict[6] != 'X' and dict[6] != 'O'):
            bot_move = 6
        elif dict[5] == dict[6] == 'O' and (dict[4] != 'X' and dict[4] != 'O'):
            bot_move = 4
        elif dict[7] == dict[8] == 'O' and (dict[9] != 'X' and dict[9] != 'O'):
            bot_move = 9
        elif dict[8] == dict[9] == 'O' and (dict[7] != 'X' and dict[7] != 'O'):
            bot_move = 7
        elif dict[1] == dict[5] == 'O' and (dict[9] != 'X' and dict[9] != 'O'):
            bot_move = 9
        elif dict[5] == dict[9] == 'O' and (dict[1] != 'X' and dict[1] != 'O'):
            bot_move = 1
        elif dict[3] == dict[5] == 'O' and (dict[7] != 'X' and dict[7] != 'O') :
            bot_move = 7
        elif dict[5] == dict[7] == 'O' and (dict[3] != 'X' and dict[3] != 'O'):
            bot_move = 3
        elif dict[1] == dict[3] == 'O' and (dict[2] != 'X' and dict[2] != 'O'):
            bot_move = 2
        elif dict[4] == dict[6] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5
        elif dict[7] == dict[9] == 'O' and (dict[8] != 'X' and dict[8] != 'O'):
            bot_move = 8
        elif dict[1] == dict[7] == 'O' and (dict[4] != 'X' and dict[4] != 'O'):
            bot_move = 4
        elif dict[2] == dict[8] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5
        elif dict[3] == dict[9] == 'O' and (dict[6] != 'X' and dict[6] != 'O'):
            bot_move = 6
        elif dict[1] == dict[9] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5
        elif dict[3] == dict[7] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5                      
        if dict[1] == dict[4] == 'X' and (dict[7] != 'X' and dict[7] != 'O'):
            bot_move = 7
        elif dict[4] == dict[7] == 'X' and (dict[1] != 'X' and dict[1] != 'O'):
            bot_move = 1
        elif dict[2] == dict[5] == 'X' and (dict[8] != 'X' and dict[8] != 'O'):
            bot_move = 8
        elif dict[5] == dict[8] == 'X' and (dict[2] != 'X' and dict [2] != 'O'):
            bot_move = 2
        elif dict[3] == dict[6] == 'X' and (dict[9] != 'X' and dict[9] != 'O'):
            bot_move = 9
        elif dict[6] == dict[9] == 'X' and (dict[3] != 'X' and dict[3] != 'O'):
            bot_move = 3
        elif dict[1] == dict[2] == 'X' and (dict[3] != 'X' and dict[3] != 'O'):
            bot_move = 3
        elif dict[2] == dict[3] == 'X' and (dict[1] != 'X' and dict[1] != 'O'):
            bot_move = 1
        elif dict[4] == dict[5] == 'X' and (dict[6] != 'X' and dict[6] != 'O'):
            bot_move = 6
        elif dict[5] == dict[6] == 'X' and (dict[4] != 'X' and dict[4] != 'O'):
            bot_move = 4
        elif dict[7] == dict[8] == 'X' and (dict[9] != 'X' and dict[9] != 'O'):
            bot_move = 9
        elif dict[8] == dict[9] == 'X' and (dict[7] != 'X' and dict[7] != 'O'):
            bot_move = 7
        elif dict[1] == dict[5] == 'X' and (dict[9] != 'X' and dict[9] != 'O'):
            bot_move = 9
        elif dict[5] == dict[9] == 'X' and (dict[1] != 'X' and dict[1] != 'O'):
            bot_move = 1
        elif dict[3] == dict[5] == 'X' and (dict[7] != 'X' and dict[7] != 'O') :
            bot_move = 7
        elif dict[5] == dict[7] == 'X' and (dict[3] != 'X' and dict[3] != 'O'):
            bot_move = 3
        elif dict[1] == dict[3] == 'X' and (dict[2] != 'X' and dict[2] != 'O'):
            bot_move = 2
        elif dict[4] == dict[6] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5
        elif dict[7] == dict[9] == 'X' and (dict[8] != 'X' and dict[8] != 'O'):
            bot_move = 8
        elif dict[1] == dict[7] == 'X' and (dict[4] != 'X' and dict[4] != 'O'):
            bot_move = 4
        elif dict[2] == dict[8] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5
        elif dict[3] == dict[9] == 'X' and (dict[6] != 'X' and dict[6] != 'O'):
            bot_move = 6
        elif dict[1] == dict[9] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5
        elif dict[3] == dict[7] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
            bot_move = 5                  
        else:
            choice = random.choice(moves)
            bot_move = int(choice)
        
    moves.remove(str(bot_move))
    dict[bot_move] = 'O'
    print(f'Ход компьютера - позиция {bot_move}!')  

def graphics(dict):
    print('=============')
    print(f'| {dict[1]} | {dict[2]} | {dict[3]} |')
    print('-------------')
    print(f'| {dict[4]} | {dict[5]} | {dict[6]} |')
    print('-------------')
    print(f'| {dict[7]} | {dict[8]} | {dict[9]} |')
    print('=============')

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

