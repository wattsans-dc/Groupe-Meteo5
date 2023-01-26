import sys
import machine

sys.path.append('D:\PROJETS\Projet CESI 01 - Météo\repo git\Groupe-M-t-o-5')

i2c = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(2), freq=400000)
s = SI7021(i2c)
print(f"Temperature : {s.temperature()}")
print(f"Humidite : {s.humidity()}")
