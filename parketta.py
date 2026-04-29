hossz = float(input('Adja meg a szoba hosszát méterben: '))
szelesseg = float(input('Adja meg a szoba szélességét méterben: '))
csomag = int(input('Hány csomag parkettával rendelkezik? '))

terulet = hossz * szelesseg

csomagmennyiseg = csomag * 2


igen = 'Van elegendő parketta'

nem = 'Nincs elegendő parketta'

print(f'A szoba területe {terulet} négyzetméter')
print(f'A csomagok {csomagmennyiseg} négyzetmétert fednek le')

if csomagmennyiseg >= terulet:
    print(f'{igen}')
else:
    print(f'{nem}')