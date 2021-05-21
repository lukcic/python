suma_blokow = int(input("Wprowadź liczbę bloków: "))
wysokosc = 0
blokow = 0

while suma_blokow > blokow:
    wysokosc = wysokosc + 1
    blokow = blokow + 1
    suma_blokow = suma_blokow - blokow

print("Wysokość piramidy wynosi:", wysokosc)

"""
blokow = 0
suma_blokow = 0
wysokosc = int(input("Podaj wysokość: "))

while wysokosc:
    blokow = blokow + 1
    wysokosc = wysokosc -1
    suma_blokow = suma_blokow + blokow

print("Ilość bloków wynosi: ",suma_blokow)
"""