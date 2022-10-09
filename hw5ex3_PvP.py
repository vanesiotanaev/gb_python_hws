def game():
    possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    dictionary = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    graphics(dictionary)

    while len(possible_moves) > 0:
        a = int(input('Ход игрока А: '))
        while not str(a) in possible_moves:
                a = int(input('Невозможно сделать ход на эту позицию, т.к. она занята или не существует! Ход игрока А: '))
        else:
            possible_moves.remove(str(a))
            dictionary[a] = 'X'
            graphics(dictionary)
        if win_check(dictionary) == True:
            break
        if len(possible_moves) > 0:
            b = int(input('Ход игрока B: '))
            while not str(b) in possible_moves:
                    b = int(input('Невозможно сделать ход на эту позицию, т.к. она занята или не существует! Ход игрока B: '))
            else:
                possible_moves.remove(str(b))
                dictionary[b] = 'O'
                graphics(dictionary)
            if win_check(dictionary) == True:
                break
    else:
        print('Ничья!')


def graphics(dict):
    print('-------------')
    print(f'| {dict[1]} | {dict[2]} | {dict[3]} |')
    print('-------------')
    print(f'| {dict[4]} | {dict[5]} | {dict[6]} |')
    print('-------------')
    print(f'| {dict[7]} | {dict[8]} | {dict[9]} |')
    print('-------------')

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
