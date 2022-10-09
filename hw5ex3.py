def game():
    possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    graphics(dict)

    while len(possible_moves) > 0:
        if dict[1] == dict[2] == dict[3] \
            or dict[4] == dict[5] == dict[6] \
                or dict[7] == dict[8] == dict[9] \
                    or dict[1] == dict[4] == dict[7] \
                        or dict[2] == dict[5] == dict[8] \
                            or dict[3] == dict[6] == dict[9] \
                                or dict[1] == dict[5] == dict[9] \
                                    or dict[3] == dict[5] == dict[7]:
                                        print('Победа!')
        a = int(input('Ход игрока А: '))
        if str(a) in possible_moves:
            possible_moves.remove(str(a))
            dict[a] = 'X'
            graphics(dict)
        if len(possible_moves) > 0:
            b = int(input('Ход игрока B: '))
            if str(b) in possible_moves:
                possible_moves.remove(str(b))
                dict[b] = 'O'
                graphics(dict)


def graphics(dictionary):
    print('-------------')
    print(f'| {dictionary[1]} | {dictionary[2]} | {dictionary[3]} |')
    print('-------------')
    print(f'| {dictionary[4]} | {dictionary[5]} | {dictionary[6]} |')
    print('-------------')
    print(f'| {dictionary[7]} | {dictionary[8]} | {dictionary[9]} |')
    print('-------------')
    # for item in field:
    #     print(item)
    #     for i in item:
    #         possible_moves.append(i)
    # possible_moves_set = set(possible_moves)
    # print(f'Возможные ходы: {possible_moves_set}')
    # while len(possible_moves_set) != 0:
    #     a = str(input('Ход игрока А: '))
    #     if a in possible_moves_set:
    #         for item in field:
    #             index = item.index(a)
    #             item[index] = 'X'
    #         possible_moves_set.remove(a)
                
    #     b = str(input('Ход игрока B: '))
    #     if b in possible_moves_set:
    #         for item in field:
    #             index = item.index(b)
    #             item[index] = 'O'
    #         possible_moves_set.remove(b)

game()
