GJ = 13.25
RG = 16
RaM = 22
KK = 13
LD = 15
SN = 20
JL = 30
LG = 17
CC = 13.25
KL = 16
e = []
f = []
r = []
p = []
s = []
for i in range(10):
    if i > 0:
        x = input('Anything else? ')
    else:
        print('Available sweets:\nGulab Jamun,\nRasgulla,\nLaddu,\nKalakand,\nLengcha,\nCham Cham,\nKaju'
              ' Katli,\nSandesh,\nand Ras Malai')
        x = input('Add an item to your order: ')
    if x == 'Gulab Jamun':
        r.append(x)
        x = GJ
        p.append(x)
        y = str(input("Tins or Pieces: "))
        if y == 'Tins':
            s.append(y)
            a = int(input('Tins: '))
            y = 20 * a
            f.append(a)
        else:
            s.append(y)
            y = int(input('Pieces: '))
            f.append(y)
        z = GJ * y
        e.append(z)
    elif x == 'Rasgulla':
        r.append(x)
        x = RG
        p.append(x)
        y = int(input("Pieces: "))
        s.append('Pieces')
        z = RG * y
        e.append(z)
        f.append(y)
    elif x == 'Ras Malai':
        r.append(x)
        x = RaM
        p.append(x)
        y = str(input("Containers or Pieces: "))
        if y == 'Containers':
            s.append(y)
            a = int(input('Containers: '))
            y = 5 * a
            f.append(a)
        else:
            s.append(y)
            y = int(input('Pieces: '))
            f.append(y)
        z = RaM * y
        e.append(z)
    elif x == 'Kaju Katli':
        r.append(x)
        x = KK
        p.append(x)
        y = str(input("Pieces or Kilograms: "))
        if y != 'Kilograms':
            s.append(y)
            y = int(input('Pieces: '))
            f.append(y)
        else:
            s.append(y)
            a = int(input('Kilograms: '))
            y = 80 * a
            f.append(a)
        z = KK * y
        e.append(z)
    elif x == 'Laddu':
        r.append(x)
        x = LD
        p.append(x)
        y = str(input("Pieces or Kilograms: "))
        if y == 'Kilograms':
            s.append(y)
            a = int(input('Kilograms: '))
            y = 35 * a
            f.append(a)
        else:
            s.append(y)
            y = int(input('Pieces: '))
            f.append(y)
        z = LD * y
        e.append(z)
    elif x == 'Sandesh':
        r.append(x)
        x = SN
        p.append(x)
        y = int(input("Pieces: "))
        s.append('Pieces')
        z = SN * y
        e.append(z)
        f.append(y)
    elif x == 'Lengcha':
        r.append(x)
        x = LG
        p.append(x)
        y = str(input("Pieces or Tins: "))
        if y == 'Tins':
            s.append(y)
            a = int(input('Tins: '))
            y = 16 * a
            f.append(a)
        else:
            s.append(y)
            y = int(input('Pieces:'))
            f.append(y)
        z = LG * y
        e.append(z)
    elif x == 'Jalebi':
        r.append(x)
        x = JL
        p.append(x)
        y = int(input("Pieces: "))
        s.append('Pieces')
        z = JL * y
        e.append(z)
        f.append(y)
    elif x == 'Cham Cham':
        r.append(x)
        x = CC
        p.append(x)
        y = str(input("Pieces or Tins: "))
        if y == 'Tins':
            s.append(y)
            a = int(input('Tins: '))
            y = 20 * a
            f.append(a)
        else:
            s.append(y)
            y = int(input('Pieces: '))
            f.append(y)
        z = CC * y
        e.append(z)
        f.append(y)
    elif x == 'Kalakand':
        r.append(x)
        x = KL
        p.append(x)
        y = int(input("Pieces: "))
        s.append('Pieces')
        z = KL * y
        e.append(z)
        f.append(y)
    elif x == 'No':
        break
if sum(e) >= 300:
    o = 0.9 * float(sum(e))
    d = 0.9
if sum(e) >= 500:
    o = 0.8 * float(sum(e))
    d = 0.8
if sum(e) >= 750:
    o = 0.7 * float(sum(e))
    d = 0.7
if sum(e) >= 1000:
    o = 0.65 * float(sum(e))
    d = 0.65
if sum(e) >= 2000:
    o = 0.60 * float(sum(e))
    d = 0.60
if sum(e) >= 5000:
    o = 0.55 * float(sum(e))
    d = 0.55
if sum(e) >= 10000:
    o = 0.5 * float(sum(e))
    d = 0.5
o = 1.08 * o
print('Order --> S.no: Item | Rate | Quantity | Total')
for i in range(len(e)):
    print(f'{i + 1}: Item: {r[i]} | Rate: {p[i]} | Quantity: {f[i]} {s[i]} | Total: {e[i]}')
print(f'Total                {sum(e)}')
print(f'Discount             -{int(100 - (d * 100))}%')
print('ST.                  +8%')
print(f'Grand Total         {int(o)}')
