import machine, time
i2c = machine.I2C(scl = machine.Pin(0), sda = machine.Pin(2), freq=400000)

while True:

    print(" Scanne du bus i2c… ")

    i2c_peripheriques = i2c.scan()

    if len(i2c_peripheriques) == 0:

        print("Aucun périphériques i2c détectés !")

    else:

        print(len(i2c_peripheriques),  " périphériques i2c trouvés ")

        for i2c_peripherique in i2c_peripheriques: 

            print(hex(i2c_peripherique))

    time.sleep(10)

