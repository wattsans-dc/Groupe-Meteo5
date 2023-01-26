import smbus2

# Adresse I2C de l'écran LCD
I2C_ADDR = 0x27

# Initialisation de la communication I2C
bus = smbus2.SMBus(1)

# Fonction pour envoyer des commandes à l'écran LCD
def send_command(cmd):
    bus.write_byte(I2C_ADDR, cmd)

# Fonction pour envoyer des données à l'écran LCD
def send_data(data):
    bus.write_byte(I2C_ADDR, 0x40 | data)

# Initialisation de l'écran LCD
send_command(0x33) # Initialisation
send_command(0x32) # Initialisation
send_command(0x28) # 4 bits mode
send_command(0x0C) # Écran allumé, curseur invisible
send_command(0x06) # Incrément automatique, pas de déplacement du curseur

# Envoi des données "Hello World!" à l'écran LCD
send_data("Hello World!")
