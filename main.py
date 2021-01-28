'''3 Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.'''

i = int(input('Gondolt szám. '))
a = int(input('Adjon meg egy számot! '))
if i == a:
    print('A szám egyenlő')

elif a < i:
    print('kissebb')
else:
    print('Nagyobb')   