import machine
from machine import I2C
from lcdi2c import LCDI2C
from time import sleep

moyenneTemp = 18.0023
moyenneHumid = 40.2563

i2c = machine.I2C(scl = machine.Pin(0), sda = machine.Pin(2), freq=10000)

# Initialise l'ecran LCD
lcd = LCDI2C( i2c, cols=16, rows=2 )
lcd.backlight()

# Clear the LCD
lcd.clear()

# Write "Hello, World!" to the LCD
def afficheEcran(text, x, y):
    lcd.print(text, (x, y))

def clearScreen():
    lcd.clear()


clearScreen()
afficheEcran("Temp : " + str(round(moyenneTemp, 2)) + " C", 0, 0)
afficheEcran("Humid : " + str(round(moyenneHumid, 2)) + " %", 0, 1)

time.sleep(3)



clearScreen()
afficheEcran("Adresse IP : ", 0, 0)
afficheEcran("192.168.137.187", 0, 1)

time.sleep(3)



temps = time.localtime()
clearScreen()
afficheEcran("Date : " + str(temps[2]) + "/" + str(temps[1]) + "/" + str(temps[0]), 0, 0)
afficheEcran("Time : " + str(temps[3]) + ":" + str(temps[4]), 0, 1)

time.sleep(3)

