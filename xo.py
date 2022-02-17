board = list(range(1, 10))
print('Добро пожаловать в игру крестики- нолики! ')
print("Игрок 1 ходит 'х', Игрок 2 ходит 'о'.")
print('Перед Вами поле с девятью цифрами, нужно выбрать номер ячейки, куда Вы хотите сделать ход.')

win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def creat_board():
    for i in range(3):
        print(" ", board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])
    print(' ')


def make_move(type):
    while True:
        creat_board()
        hod = int(input('Куда вы сделаете ход? ' + type + ' '))
        if not 1 <= hod <= 9:
            print('Не допустимое значение')
            continue

        if board[hod - 1] == 'x' or board[hod - 1] == 'o':
            print('Ячейка занята')
            continue
        else:
            board[hod - 1] = type
        break


def finish():
    for each in win:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return True
    else:
        return False


xo = 'x'
counter = 1
while True:
    make_move(xo)

    if finish() == True:
        print('Вы выйграли!')
        break
    if xo == 'x':
        xo = 'o'
    else:
        xo = 'x'

    counter = counter + 1

    if counter > 9:
        print('У вас ничья')
        break
creat_board()
