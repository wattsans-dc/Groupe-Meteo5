moyenne = 0
Valeur = 0
Valeur1 = sonde.value
i = 0

while i < 4:
    i =+ 1
    Valeur = Valeur + Valeur1
    time.sleep(2)
    Valeur1 = sonde.value
moyenne = Valeur / 5


