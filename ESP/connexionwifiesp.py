import network

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
sta_if.connect("meteo-groupe", "meteogroupe")

while not sta_if.isconnected():
    pass

print("Connecté à WiFi avec l'adresse IP :", sta_if.ifconfig()[0])