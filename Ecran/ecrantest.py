from lcdi2c import lcdi2c

# Initialise l'écran LCD
lcd = lcdi2c.lcd()

# Affiche du texte sur la première ligne
lcd.lcd_display_string("Hello, World!", 1)
