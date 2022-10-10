# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random
def game():
    candies = 150
    first_move = random.randint(0,1)
    print(f"Есть {candies} конфет.")
    if first_move == 0:
        while candies != 0:
            candies = human(candies)
            if candies != 0:
                candies = computer(candies)
            else:
                print("Игра окончена!")
    else:
        while candies != 0:
            candies = computer(candies)
            if candies != 0:
                candies = human(candies)
            else:
                print("Игра окончена!")


def human(sweets):
    recommended = sweets % 29
    if not recommended == 0:
        a = int(input(f"Введите количество конфет (1-28). Может быть, {recommended}?: "))
    else:
        a = int(input(f"Введите количество конфет (1-28): "))
    while a > 28 or a < 1:
        a = int(input("Вы ввели недопустимое кол-во. Введите количество конфет (1-28): "))
    sweets -= a
    if sweets == 0:
        print("Игрок победил!")
    else:
        print(f"Игрок забрал {a} конфет. Осталось {sweets}.")

    return sweets

def computer(sweets):
    b = sweets % 29
    while b < 1 or b > 28:
        b = random.randint(1, 28)
    else:
        sweets -= b
    if sweets == 0:
        print("Компьютер победил!")
    else:
        print((f"Компьютер забрал {b} конфет. Осталось {sweets}."))

    return sweets
    
game()