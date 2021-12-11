# Versions

## Version 4.4 - 5 11.12.2021 - Finished(1:31 AM - 3:10 AM)
>Am implementat algoritmul MinMax cu alpha beta prunning.

>O consecinta ar fi ca daca rulez acum algoritmul cu depth-ul egal cu o valoare mai mare(de exemplu 5), AI-ul face alegerile mult mai rapid datorita retazarii arborelui in timpul algoritmului.

>Am refactorizat codul conform PEP Documentation.

>Am adaugat parte grafica pentru alegerea tipului de AI.(nivel easy - random AI, nivel medium - minmax cu depth = 3 si nivel hard - minmax cu alpha_beta prunning cu depth = 5).

>Am pregatit si un gif cum functioneaza acum AI cu algoritmul MinMax:
![gif](https://media.giphy.com/media/OGkCRiWB4BvHwzIBEL/giphy.gif)
## Version 4.2 11.12.2021 - Finished(1:12 AM)
>Am implementat algoritmul MinMax pentru joc.

### Version 4.2.1 10.12.2021 - Resolved Bugs Problem (~1:07 PM)
> Bug1: Algoritmul minmax nu returneaza doar o valoare, ci o tupla de 2 valori: cea mai buna coloana aleasa + scorul aferent operatiei facute.
> Daca faceam doar column = minmax(...) imi dadea eroare. Astfel, trebuie facut conform urm. sintaxe: score, column = minmax(...)
> Linia 118 din 4inaRow.py

> Bug2: Eu in algoritm, in pasii de maximizare si minimizare initializez valoarea val cu + si - infinit(depinde de nivel).
> Return-ul de la liniile 223 respectiv 236(din algoritmul minmax, functions.py) era indentat cu un tab mai in fata, astfel el se executa in instructiunea for.
> Fiind clar din prima o valoare mai mica/mai mare se dadea return dupa prima iteratie, astfel se alege prima pozitie, ceea ce era gresit.
> Ca sa rezolv acest lucru, am identat cu un tab in spate asa cum este acum, iar return-ul se efectueaza dupa instructiunea for.

> Bug3: La minimizing level, am uitat sa schimb semnul din > in < si algoritmul mergea prost.

>Am pregatit si un gif cum functioneaza acum AI cu algoritmul MinMax:
![gif](https://media.giphy.com/media/YZEiu6ltYXFpic7tVx/giphy.gif)
## Version 4.1 10.12.2021 - Finished(9:31 PM)
>Am implementat un sistem de scoring pentru alegerea AI-ului(orizontal, vertical si pe ambele diagonale: stg+drpt)

>In principiu, sistemul cauta iterativ pe toate coloane disponibile toate randurile libere disponibile si calculeaza un scor pentru fiecare alegere.

>Daca se gaseste o secventa de 3inaRow, scorul este adunat cu o valoare mica(5). Insa daca gasim o secventa castigatoarem, 4inaRow, scorul creste cu 50. 

>Astfel, daca am compara cele 2 alegeri, AI-ul o alege pe a2a, ca are un scor mai bun.

>In caz ca nu se gaseste nici 3 si nici 4 in a Row, se face alegerea random.

### Version 4.1.1 10.12.2021 - Resolved Bug Problem (9:20 PM)
>In principiu, bug-urile care mi-au dat cele mai mari batai de cap au fost cele pentru determinarea scorului sistemului pe diagonale. 

>De exemplu, initial pentru diagonala secundara, cand determinam index-ul ma foloseam de dimensiunea maxima a tablei, dar era gresit pentru ca in problema dimensiunea tablei de joc este variabila.
 
>Asa ca am ales sa reprezint in functie de index-ul curent.(linia 161 din functions, metoda score_possible_position)

>Am pregatit si 2 gif-urile cum functioneaza acum AI:

![gif](https://media.giphy.com/media/qaQiej0GJkBwwRHKmy/giphy.gif)

![gif](https://media.giphy.com/media/bCLZ45HVcX5ACfPxm8/giphy.gif)
## Version 3 09.12.2021 - Finished(12:35 PM)
>Am implementat primul nivel de AI(se face o alegere random a coloanei pe care se pune piesa)

>Am implementat pentru input-ul de la tastatura ca un jucator sa poata joace cu un AI.


### Version 3.1 09.12.2021 - Resolved Bug Problem (12:15 PM)
> Am rezolvat un bug legat punerea pieselor pe tabla de joc de catre AI. Problema era ca valoarea din spatele a pieselor trebuie sa fie diferite la AI fata de la jucatorii simplii, acum se detecteaza diferenta si se pune piesa AI-ul pe tabla de joc.

> Am modificat liniile 121 si 123 din 4inaROW.py . (schimbat valoarea din instructiunile if si put_piece() )

>Am pregatit si un gif in care prezint parcursul pana acum:

 ![gif](https://media.giphy.com/media/VPt5zEpLcikH3SgCiU/giphy.gif)

## Version 2 06.12.2021 - FINISHED (6:24 PM) ---> 7:05PM
>Am implementat functionalitatea jocului pentru 2 jucatori normali.

>Am implementat initializarea input-ului de la tastatura. 

>Se va utiliza sintaxa: 4inaROW.py player RowNumber ColumnNumber FirstPlayerToPlay

>Am documentat codul scris conform standardului PEP.

### Version 2.1 06.12.2021 - Resolved Bug Problem (7:05 PM)
> Am rezolvat un bug legat de detectarea diagonalei stanga ca win condition.
> Am modificat linia 103. (schimbat parametrii din instructiunea for)

>Am pregatit si un gif in care prezint parcursul pana acum:

 ![gif](https://media0.giphy.com/media/wKZ8mxVbx3YQzuOMHD/giphy.gif)

 
## Version 1 04.12.2021 - FINISHED
> Am implementat partea grafica din joc(tabla de joc + cum se pun obiectele in board dupa ce apesi).

> Am implementat ideea de turn pentru ambii playeri(unul asteapta dupa celalalt).

> Am descoperit un mic bug pe care trebuie sa il rezolv la nivel de parte grafica: in momentul in care un player isi pune pe tabla de joc piesa aceasta nu se coloreaza imediat in culoare celui de-al doilea jucator.

> Am pregatit si un gif in care prezint parcursul pana acum:

![gif](https://media.giphy.com/media/N4nuDvxDuzZs05AkDQ/giphy.gif)



# Python Project  - 4 in a ROW

## Cerințe
>Se va crea o interfata grafica ce va oferi utilizatorului posibilitatea sa joace o partidă de 4 in
ROW, atat cu calculatorul, cât și cu un alt opponent. Calculatorul va avea 3 nivele (slab,
mediu si avansat). La initializare se va seta și dimensiunea tablei de joc, respectiv cine începe
primul (calculator sau human) dacă jucăm cu un AI.

## Echipa
- Constantinescu George-Gabriel ([@iceeye7gabi](https://github.com/iceeye7gabi))
