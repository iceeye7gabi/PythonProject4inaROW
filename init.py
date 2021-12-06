import sys

PLAYER1 = 1
PLAYER2 = 2

# verify the correctness of the input given from keyboard
if len(sys.argv) < 4:
    print("Sablon rulare: 4inaROW.py <player> <RowNumber> <ColumnNumber> [firstPlayer] ")
    exit()

# verify the correctness of the first parameter
if sys.argv[1] == "player":
    enemy = PLAYER2
else:
    print("Ati introdus gresit primul argument! Trebuie player!")
    exit()

# verify the correctness of the second and third parameter
try:
    ROW_COUNT = int(sys.argv[2])
    COLUMN_COUNT = int(sys.argv[3])
except TypeError as e:
    print("Numarul de randuri/coloane trebuie sa fie un numar intreg!")
    exit()

# verify the correctness of the forth parameter
if sys.argv[4] == "player1":
    turn = PLAYER1
elif sys.argv[4] == "player2":
    turn = PLAYER2
else:
    print("Ati introdus gresit al 4 lea argument! Trebuie player1/player2")
