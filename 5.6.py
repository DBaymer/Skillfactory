# Поле:
m = [[" ", " ", " "],
     [" ", " ", " "],
     [" ", " ", " "]]


def show():
    print(f"   0 1 2")
    for i in range(3):
        print(f" {i} {m[i][0]} {m[i][1]} {m[i][2]}")


# def show():
#     print(f"     0    1    2")
#     for i in range(len(m)):
#         print(f" {i} {m[i][0:3]}")
#         print()


def hod():
    while True:
        i, j = input("Ввести координаты через пробел:").split()
        i, j = int(i), int(j)

        if 0 > i or i > 2 or 0 > j or j > 2:
            print("Координаты вне диапазона!")
            continue

        if m[i][j] != " ":
            print("Клетка занята!")
            continue

        return i, j


def win():
    if m[0][0] == "X" and m[0][1] == "X" and m[0][2] == "X":
        print("Win X")
        return True
    if m[1][0] == "X" and m[1][1] == "X" and m[1][2] == "X":
        print("Win X")
        return True
    if m[2][0] == "X" and m[2][1] == "X" and m[2][2] == "X":
        print("Win X")
        return True
    if m[0][0] == "X" and m[1][0] == "X" and m[2][0] == "X":
        print("Win X")
        return True
    if m[0][1] == "X" and m[1][1] == "X" and m[2][1] == "X":
        print("Win X")
        return True
    if m[0][2] == "X" and m[1][2] == "X" and m[2][2] == "X":
        print("Win X")
        return True
    if m[0][0] == "X" and m[1][1] == "X" and m[2][2] == "X":
        print("Win X")
        return True
    if m[0][2] == "X" and m[1][1] == "X" and m[2][0] == "X":
        print("Win X")
        return True
    if m[0][0] == "0" and m[0][1] == "0" and m[0][2] == "0":
        print("Win 0")
        return True
    if m[1][0] == "0" and m[1][1] == "0" and m[1][2] == "0":
        print("Win 0")
        return True
    if m[2][0] == "0" and m[2][1] == "0" and m[2][2] == "0":
        print("Win 0")
        return True
    if m[0][0] == "0" and m[1][0] == "0" and m[2][0] == "0":
        print("Win 0")
        return True
    if m[0][1] == "0" and m[1][1] == "0" and m[2][1] == "0":
        print("Win 0")
        return True
    if m[0][2] == "0" and m[1][2] == "0" and m[2][2] == "0":
        print("Win 0")
        return True
    if m[0][0] == "0" and m[1][1] == "0" and m[2][2] == "0":
        print("Win 0")
        return True
    if m[0][2] == "0" and m[1][1] == "0" and m[2][0] == "0":
        print("Win 0")
        return True


count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Крестик")
    else:
        print("Нолик")

    x, y = hod()

    if count % 2 == 1:
        m[x][y] = "X"
    else:
        m[x][y] = "0"

    if win():
        show()
        break

    if count == 9:
        print("Ничья!")
        break
