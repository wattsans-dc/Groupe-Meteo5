import machine, time, ssd1306
from ssd1306 import SSD1306_I2C
i2c = machine.I2C(scl = machine.Pin(0), sda = machine.Pin(2), freq=400000)

#sensor = HTU21D(i2c)
#print("\nTemperature: %0.1f C" % sensor.temperature)

oled = SSD1306_I2C(128, 64, i2c, 0x27)
oled.fill(0)
oled.text("Hello World", 0, 0)
oled.show()
print("Hello World")
