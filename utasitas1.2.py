'''1.2 Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"'''

a = input('jó napod van? ')
if a == 'igen' :
    print("az fasza")
elif a == 'nem':
    print('Az nem jó tes')
else:
    print("Nem értem a válaszod")