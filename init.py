import sys
from variables import PLAYER1, PLAYER2, AI

""" 
verify the correctness of the input given from keyboard
"""
if len(sys.argv) < 4:
    print("Sablon rulare: 4inaROW.py <player> <RowNumber> <ColumnNumber> [firstPlayer] ")
    exit()

"""
verify the correctness of the first parameter - who are you playing against
"""
if sys.argv[1] == "player":
    enemy = PLAYER2
elif sys.argv[1] == "AI":
    enemy = AI
else:
    print("Ati introdus gresit primul argument! Trebuie player sau AI!")
    exit()

"""
verify the correctness of the second and third parameter - number of rows and columns
"""
try:
    ROW_COUNT = int(sys.argv[2])
    COLUMN_COUNT = int(sys.argv[3])
    if ROW_COUNT < 6 or ROW_COUNT > 9 or COLUMN_COUNT < 6 or COLUMN_COUNT > 9:
        print("Numarul de linii si coloane intre 6 si 10")
        exit()
except TypeError as e:
    print("Numarul de randuri/coloane trebuie sa fie un numar intreg!")
    exit()


"""
verify the correctness of the forth parameter - who is the first to play
"""
if sys.argv[4] == "player1":
    turn = PLAYER1
elif sys.argv[4] == "player2":
    turn = PLAYER2
elif sys.argv[4] == "AI":
    turn = AI
else:
    print("Ati introdus gresit al 4 lea argument! Trebuie player1/player2/AI")
    exit()
