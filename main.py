# CandyCrush
import random

# Initialize matrice(a)
a = [[0 for x in range(11)] for y in range(11)]

scor_t = 0
scor_l = 0
scor_linia_5 = 0
scor_linia_4 = 0
scor_linia_3 = 0

for x in range(11):
    for y in range(11):
        a[x][y] = random.randrange(1, 5)

# Afisare matrice initiala:
print("Matricea initiala este: ")


def afisare():
    for g in range(11):
        print(a[g])
    print("\n")


def linia_de_3():
    global scor_linia_3
    for i in range(9):
        for j in range(10):
            if a[i][j] == a[i + 1][j + 1] == a[i + 2][j]:
                a[i + 1][j], a[i + 1][j + 1] = a[i + 1][j + 1], a[i + 1][j]
                scor_linia_3 += 5

    for i in range(9):
        for j in range(10):
            if a[i][j + 1] == a[i + 1][j] == a[i + 2][j + 1]:
                a[i + 1][j], a[i + 1][j + 1] = a[i + 1][j + 1], a[i + 1][j]
                scor_linia_3 += 5

    for i in range(10):
        for j in range(9):
            if a[i][j + 1] == a[i + 1][j] == a[i + 1][j + 2]:
                a[i + 1][j + 1], a[i][j + 1] = a[i][j + 1], a[i + 1][j + 1]
                scor_linia_3 += 5

    for i in range(10):
        for j in range(9):
            if a[i][j] == a[i][j + 2] == a[i + 1][j + 1]:
                a[i + 1][j + 1], a[i][j + 1] = a[i][j + 1], a[i + 1][j + 1]
                scor_linia_3 += 5

def linie_de_4():
    global scor_linia_4
    # pe orizontala
    for i in range(8):
        for j in range(6):
            if a[i][j + 1] == a[i + 1][j] == a[i + 1][j + 2] == a[i + 1][j + 3]:
                a[i][j + 1], a[i + 1][j + 1] = a[i + 1][j + 1], a[i][j + 1]
                scor_linia_4 += 10

    for i in range(8):
        for j in range(7):
            if a[i][j + 2] == a[i + 1][j] == a[i + 1][j + 1] == a[i + 1][j + 3]:
                a[i][j + 2], a[i + 1][j + 2] = a[i + 1][j + 1], a[i][j + 1]
                scor_linia_4 += 10

    for i in range(8):
        for j in range(7):
            if a[i][j] == a[i][j + 2] == a[i][j + 3] == a[1 + 1][j + 1]:
                a[i][j + 1], a[i + 1][j + 1] = a[i + 1][j + 1], a[i][j + 1]
                scor_linia_4 += 10

    for i in range(8):
        for j in range(6):
            if a[i][j] == a[i][j + 1] == a[i][j + 3] == a[1 + 1][j + 1]:
                a[i][j + 2], a[i + 1][j + 2] = a[i + 1][j + 2], a[i][j + 2]
                scor_linia_4 += 10

    # verticala
    for i in range(6):
        for j in range(8):
            if a[i][j] == a[i + 1][j + 1] == a[i + 2][j] == a[i + 3][j]:
                a[i + 1][j], a[i + 1][j + 1] = a[i + 1][j + 1], a[i + 1][j]
                scor_linia_4 += 10

    for i in range(6):
        for j in range(8):
            if a[i][j + 1] == a[i + 1][j] == a[i + 2][j + 1] == a[i + 3][j + 1]:
                a[i + 1][j], a[i + 1][j + 1] = a[i + 1][j + 1], a[i + 1][j]
                scor_linia_4 += 10

    for i in range(7):
        for j in range(8):
            if a[i][j] == a[i + 1][j] == a[i + 2][j + 2] == a[i + 3][j]:
                a[i + 2][j], a[i + 2][j + 1] = a[i + 2][j + 1], a[i + 2][j]
                scor_linia_4 += 10

    for i in range(6):
        for j in range(8):
            if a[i][j + 1] == a[i + 1][j + 1] == a[i + 2][j] == a[i + 3][j + 1]:
                a[i + 2][j], a[i + 2][j + 1] = a[i + 2][j + 1], a[i + 2][j]
                scor_linia_4 += 10


def linia_5():
    global scor_linia_5
    for i in range(8):
        for j in range(7):
            if a[i][j] == a[i][j + 1] == a[i + 1][j + 2] == a[i][j + 3] == a[i][j + 4]:
                a[i + 1][j + 2], a[i][j + 2] = a[i][j + 2], a[i + 1][j + 2]
                scor_linia_5 += 50

    for i in range(8):
        for j in range(7):
            if a[i][j] == a[i][j + 1] == a[i - 1][j + 2] == a[i][j + 3] == a[i][j + 4]:
                a[i - 1][j + 2], a[i - 1][j + 2] = a[i - 1][j + 2], a[i - 1][j + 2]
                scor_linia_5 += 50

    for i in range(6):
        for j in range(7):
            if a[i][j] == a[i + 1][j] == a[i + 2][j - 1] == a[i + 3][j] == a[i + 4][j]:
                a[i + 2][j - 1], a[i + 2][j] = a[i + 2][j], a[i + 2][j - 1]
                scor_linia_5 += 50

    for i in range(7):

        for j in range(10):
            if a[i][j] == a[i + 1][j] == a[i + 2][j + 1] == a[i + 3][j] == a[i + 4][j]:
                a[i + 2][j + 1], a[i + 2][j] = a[i + 2][j], a[i + 2][j + 1]
                scor_linia_5 += 50

def L_1():
    global scor_l
    for i in range(8):
        for j in range(7):
            if a[i][j] == a[i + 1][j] == a[i + 2][j - 1] == a[i + 2][j + 1] == a[i + 2][j + 2]:
                a[i + 2][j - 1], a[i + 2][j] = a[i + 2][j], a[i + 2][j - 1]
                scor_l += 20

    for i in range(7):
        for j in range(7):
            if a[i][j] == a[i + 1][j] == a[i + 3][j] == a[i + 2][j + 1] == a[i + 2][j + 2]:
                a[i + 3][j], a[i + 2][j] = a[i + 2][j], a[i + 3][j]
                scor_l += 20


def L_2():
    global scor_l
    for i in range(7):
        for j in range(8):
            if a[i][j] == a[i + 1][j + 1] == a[i + 1][j + 2] == a[i + 2][j] == a[i + 3][j]:
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                scor_l += 20

    for i in range(7):
        for j in range(8):
            if a[i][j] == a[i][j + 2] == a[i][j + 3] == a[i + 1][j + 1] == a[i + 2][j + 1]:
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
                scor_l += 20


def L_3():
    global scor_l
    for i in range(8):
        for j in range(8):
            if a[i][j] == a[i + 1][j] == a[i + 3][j] == a[i + 2][j - 1] == a[i + 2][j - 2]:
                a[i + 2][j], a[i + 3][j] = a[i + 3][j], a[i + 2][j]
                scor_l += 20

    for i in range(8):

        for j in range(8):
            if a[i][j] == a[i + 1][j] == a[i + 2][j - 1] == a[i + 2][j - 2] == a[i + 2][j + 1]:
                a[i + 2][j], a[i + 2][j + 1] = a[i + 2][j + 1], a[i + 2][j]
                scor_l += 20


def L_4():
    global scor_l
    for i in range(6):
        for j in range(8):
            if a[i][j] == a[i + 1][j - 1] == a[i + 1][j - 1] == a[i + 2][j] == a[i + 3][j]:
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                scor_l += 20

    for i in range(8):
        for j in range(8):
            if a[i][j] == a[i][j + 1] == a[i][j + 3] == a[i + 1][j + 2] == a[i + 2][j + 2]:
                a[i][j + 2], a[i][j + 3] = a[i][j + 3], a[i][j + 2]
                scor_l += 20


# T
def T_1():
    global scor_t
    for i in range(8):
        for j in range(8):
            if a[i][j] == a[i + 1][j - 1] == a[i + 1][j + 1] == a[i + 2][j] == a[i + 3][j]:
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                scor_t += 30


def T_2():
    global scor_t
    for i in range(6):
        for j in range(7):
            if a[i][j] == a[i + 1][j] == a[i + 2][j - 1] == a[i + 2][j + 1] == a[i + 3][j]:
                a[i + 3][j], a[i + 2][j] = a[i + 2][j], a[i + 3][j]
                scor_t += 30

def T_3():
    global scor_t
    for i in range(7):

        for j in range(6):
            if a[i][j] == a[i + 1][j - 1] == a[i + 1][j + 1] == a[i + 1][j + 2] == a[i + 2][j]:
                a[i + 1][j - 1], a[i + 1][j] = a[i + 1][j], a[i + 1][j - 1]
                scor_t += 30


def T_4():
    global scor_t
    for i in range(7):
        for j in range(6):
            if a[i][j] == a[i + 1][j - 1] == a[i + 1][j - 2] == a[i + 1][j + 1] == a[i + 2][j]:
                a[i + 1][j + 1], a[i + 1][j] = a[i + 1][j], a[i + 1][j + 1]
                scor_t += 30


def eliminare3():
    for i in range(11):
        for j in range(8):
            if (a[i][j] == a[i][j + 1] == a[i][j + 2]):
                a[i][j] = 0
                a[i][j + 1] = 0
                a[i][j + 2] = 0

    for i in range(8):
        for j in range(11):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0


def eliminare4():
    for i in range(11):
        for j in range(7):
            if (a[i][j] == a[i][j + 1] == a[i][j + 2] == a[i][j + 3]):
                a[i][j] = 0
                a[i][j + 1] = 0
                a[i][j + 2] = 0
                a[i][j + 3] = 0

    for i in range(7):
        for j in range(11):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i + 3][j]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 3][j] = 0


def eliminare5():
    for i in range(11):
        for j in range(6):
            if (a[i][j] == a[i][j + 1] == a[i][j + 2] == a[i][j + 3] == a[i][j + 4]):
                a[i][j] = 0
                a[i][j + 1] = 0
                a[i][j + 2] = 0
                a[i][j + 3] = 0
                a[i][j + 4] = 0

    for i in range(6):
        for j in range(11):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i + 3][j] == a[i + 4][j]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 3][j] = 0
                a[i + 4][j] = 0


def eliminare_L1():
    for i in range(9):
        for j in range(9):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i + 2][j + 1] == a[i + 2][j + 2]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 2][j + 1] = 0
                a[i + 2][j + 2] = 0


def eliminare_L2():
    for i in range(9):
        for j in range(9):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i][j + 1] == a[i][j + 2]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i][j + 1] = 0
                a[i][j + 2] = 0


def eliminare_L3():
    for i in range(9):
        for j in range(11):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i + 2][j - 1] == a[i + 2][j - 2]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 2][j - 1] = 0
                a[i + 2][j - 2] = 0


def eliminare_L4():
    for i in range(11):
        for j in range(9):
            if (a[i][j] == a[i][j + 1] == a[i][j + 2] == a[i - 1][j + 2] == a[i - 2][j + 2]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i][j + 1] = 0
                a[i - 1][j + 2] = 0
                a[i - 2][j + 2] = 0


def elimina_T1():
    for i in range(8):
        for j in range(8):
            if (a[i][j] == a[i][j + 1] == a[i][j + 2] == a[i + 1][j + 1] == a[i + 2][j + 1]):
                a[i][j] = 0
                a[i][j + 1] = 0
                a[i][j + 2] = 0
                a[i + 1][j + 1] = 0
                a[i + 2][j + 1] = 0


def elimina_T2():
    for i in range(9):
        for j in range(9):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i + 2][j + 1] == a[i + 2][j - 1]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 2][j + 1] = 0
                a[i + 2][j - 1] = 0


def elimina_T3():
    for i in range(9):
        for j in range(9):
            if (a[i][j] == a[i + 1][j] == a[i + 2][j] == a[i + 1][j + 1] == a[i + 1][j + 2]):
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 1][j + 1] = 0
                a[i + 1][j + 2] = 0


def elimina_T4():
    for i in range(9):
        for j in range(9):
            if (a[i][j] == a[i][j + 1] == a[i][j + 2] == a[i + 1][j + 2] == a[i - 1][j + 2]):
                a[i][j] = 0
                a[i][j + 1] = 0
                a[i][j + 2] = 0
                a[i + 1][j + 2] = 0
                a[i - 1][j + 2] = 0


def muta():
    for j in range(11):
        for k in range(11):
            for i in range(10, 0, -1):
                if a[i][k] == 0:
                    a[i][k], a[i - 1][k] = a[i - 1][k], a[i][k]


def randomize():
    for j in range(11):
        for i in range(11):
            if a[i][j] == 0:
                a[i][j] = random.randrange(1, 5)

afisare()
iteratii = 0
while (iteratii < 1000):
    iteratii +=1
    #L
    L_1()
    eliminare_L1()
    muta()
    afisare()
    randomize()
    L_2()
    eliminare_L2()
    muta()
    afisare()
    randomize()
    L_3()
    eliminare_L3()
    muta()
    afisare()
    randomize()
    L_4()
    eliminare_L4()
    muta()
    afisare()
    randomize()
    #T
    T_1()
    elimina_T1()
    muta()
    afisare()
    randomize()
    T_2()
    elimina_T2()
    muta()
    afisare()
    randomize()
    T_3()
    elimina_T3()
    muta()
    afisare()
    randomize()
    T_4()
    elimina_T4()
    muta()
    afisare()
    randomize()
    #Linia de 5
    linia_5()
    eliminare5()
    muta()
    afisare()
    randomize()
    linie_de_4()
    eliminare4()
    muta()
    afisare()
    randomize()
    linia_de_3()
    eliminare3()
    muta()
    afisare()
    randomize()

    print("Scorul pentru linia de 3 este:", scor_linia_3)
    print("Scorul pentru linia de 4 este:", scor_linia_4)
    print("Scorul pentru linia de 5 este:", scor_linia_5)
    print("Scorul pentru T este:", scor_t)
    print("Scorul pentru L este:", scor_l)
    print("Scorul total este: ", scor_linia_3 + scor_linia_4 + scor_linia_5 + scor_l + scor_t)