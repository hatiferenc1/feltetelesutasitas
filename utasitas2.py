'''2 Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan, hogy kiderüljön páros-e? Ebben az esetben mennyi lesz a maradék? '''
i = int(input('Adjon meg egy számot! '))
if i % 2 == 0 :
    print('Ez a szám páros! ')
else:
    print('Ez a szám páratlan! ')
