import random

print("Hello world!")
random.seed()
losowaliczba = random.randint(0,100)

zgadles = False
while not zgadles:
    print("Zgadnij liczbe:")
    mojaliczba = int(input())
    if (losowaliczba < mojaliczba):
        print("Nie zgadles - szukana liczba jest mniejsza")
    if (losowaliczba > mojaliczba):
        print("Nie zgadles - szukana liczba jest wieksza")
    if (losowaliczba == mojaliczba):
        print("Zgadles")
        zgadles = True
