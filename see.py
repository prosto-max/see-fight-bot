import time
import random
import os

def create_board():
    return [["□" for _ in range(10)] for _ in range(10)]

def show_board(tip):
    print("  1 2 3 4 5 6 7 8 9 10")
    n = 0
    for row in tip:
        print(letters[n] + " " + str(row)[1:-1].replace("'", "").replace(",", ""))
        n += 1

def random_xod_let():
    return letters[random.randint(0, 9)] + str(random.randint(1, 10))

def random_xod_1(bo):
    return bo[random.randint(0, 9)][random.randint(0, 9)]


#случайная расстановка
def random_place(bo, count):
    print("Установка корабля:", count)
    g1 = 0
    cou = "X"
    while g1 != count:
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        print(x, y, g1)
        g1 = 0
        #выбор направления
        g = 1
        while g != 0:
            c = random.randint(1, 4)
            if c == 1 and y - count > -2:
                g = 0
                y -= count + 1
                p1 = 0
                p2 = -1
            elif c == 2 and y + count < 11:
                g = 0
                p1 = 0
                p2 = 1
                y += count - 1
            elif c == 3 and x - count > -2:
                g = 0
                p1 = -1
                p2 = 0
                x -= count + 1
            elif c == 4 and x + count < 11:
                g = 0
                p1 = 1
                p2 = 0
                x += count - 1
        for i in range(count):
            x1 = x + p2 * i
            y1 = y + p1 * i
            if x1 > 9 or x1 < 0 or y1 < 0 or y1 > 9:
                g1 = -10
                break
            print(x1, y1, c, g1)
            g1 += 1
            if bo[x1][y1] != "□":
                g1 = -10
            else:
                if x1 < 9:
                    if bo[x1 + 1][y1] != "□":
                        g1 = -10
                        break
                    if y1 < 9:
                        if bo[x1 + 1][y1 + 1] != "□":
                            g1 = -10
                            break
                    if y1 > 0:
                        if bo[x1 + 1][y1 - 1] != "□":
                            g1 = -10
                            break
                if x1 > 0:
                    if bo[x1 - 1][y1] != "□":
                        g1 = -10
                        break
                    if y1 < 9:
                        if bo[x1 - 1][y1 + 1] != "□":
                            g1 = -10
                            break
                    if y1 > 0:
                        if bo[x1 - 1][y1 - 1] != "□" :
                            g1 = -10
                            break
                if y1 < 9:
                    if bo[x1][y1 + 1] != "□":
                        g1 = -10
                        break
                if y1 > 0:
                    if bo[x1][y1 - 1] != "□":
                        g1 = -10
                        break
        if g1 == count:
            for i in range(count):
                bo[x + p2 * i][y + p1 * i] = cou



def check_xod(xod1):
    return (xod[0] in letters and int(xod[1:]) < 11 and int(xod[1:]) > 0)


# итог хода для игрока
def xody(xod1, bo1, bo2): #вердикт хода ход, доска показа, реальная доска
    if bo1[letters.find(xod1[0])][int(xod1[1:]) - 1] == "□":
        if bo2[letters.find(xod1[0])][int(xod1[1:]) - 1] == "□":
            print("Вы промахнулись, ход переходит боту")
            bo1[letters.find(xod1[0])][int(xod1[1:]) - 1] = "*"
            bo2[letters.find(xod1[0])][int(xod1[1:]) - 1] = "*"
        else:
            p = bo2[letters.find(xod1[0])][int(xod1[1:]) - 1]
            bo1[letters.find(xod1[0])][int(xod1[1:]) - 1] = "■"
            bo2[letters.find(xod1[0])][int(xod1[1:]) - 1] = "■"
            if p not in str(bo2):
                print("Вы убили корабль бота размером:", "count")
                return 1
            else:
                print("Вы ранили корабль бота, ход переходит боту")
    else:
        print("Удар в эту точку ранее уже был произведен, ход переходит боту")
    return 0



# итог хода для бота
def xody_bot(xod1, bo1, bo2): #вердикт хода ход, доска показа, реальная доска
    if bo1[letters.find(xod1[0])][int(xod1[1:]) - 1] == "□":
        if bo2[letters.find(xod1[0])][int(xod1[1:]) - 1] == "□":
            print("Бот промахнулся, ход переходит Вам")
            bo1[letters.find(xod1[0])][int(xod1[1:]) - 1] = "*"
            bo2[letters.find(xod1[0])][int(xod1[1:]) - 1] = "*"
        else:
            p = bo2[letters.find(xod1[0])][int(xod1[1:]) - 1]
            bo1[letters.find(xod1[0])][int(xod1[1:]) - 1] = "■"
            bo2[letters.find(xod1[0])][int(xod1[1:]) - 1] = "■"
            if p not in str(bo2):
                print("Вы убили корабль бота размером:", "count")
                return 1
            else:
                print("Вы ранили корабль бота, ход переходит боту")
    else:
        print("Удар в эту точку ранее уже был произведен, ход переходит боту")
    return 0

letters = "abcdefghij"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

board_bot = create_board()
board_my = create_board()

board_bot_show = create_board()
board_my_show = create_board()

score_bot = 0
score_my = 0
turn = 1



#расстановка кораблей
flot = [2, 3, 3, 4, 5] #для изменения конфигурации ввести новые длины. Если нужны несколько одинаковых, то писать дробные, пример 3.1, 3.2, 3.3... Допускается написание двух одинаковых чисел (только дробных)
print("Давайте расставим корабли, напишите начальную и конечную клетку для корабля")
for i in flot:
    random_place(board_bot, i)




#игра
while score_bot < 5 and score_my < 5:
    print("поле бота:")
    show_board(board_bot)
    print("мое поле:")
    show_board(board_my)
    print("поле бота:")
    show_board(board_bot_show)
    print("мое поле:")
    show_board(board_my_show)
    print("Сделайте ход (буква + цифра с поля, пример " + random_xod_let() + "):")

    #ход мой
    while turn != 0:
        xod = input("")
        os.system('cls')
        if check_xod(xod):
            score_my += xody(xod, board_bot_show, board_bot)
            turn = 0
        else:
            print("поле бота:")
            show_board(board_bot)
            print("мое поле:")
            show_board(board_my)
            print("поле бота:")
            show_board(board_bot_show)
            print("мое поле:")
            show_board(board_my_show)
            print("невозможный ход: ", xod)
            print("Сделайте ход (буква + цифра с поля, например " + random_xod_let() + "):")
    print("Вы успешно сделали ход: ", xod)
    
        




    
    #os.system('cls')
    turn = 1






"""n = n + 0.01
    time.sleep(0.01)
    os.system('cls')
    print("time:", n, "score:", score)
    for row in board:
        print(str(row)[1:-1].replace("'", "").replace(", ", ""))"""
    
