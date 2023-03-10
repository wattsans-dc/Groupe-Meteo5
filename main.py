from micropython import const
import ustruct
import sys
import urequests as requests
import time
from ecran import afficheEcran, clearScreen

_HUMID_NOHOLD = const(0xf5)
_TEMP_NOHOLD = const(0xf3)
_RESET = const(0xfe)
_READ_USER1 = const(0xe7)
_USER1_VAL = const(0x3a)


def _crc(data):
    crc = 0
    for byte in data:
        crc ^= byte
        for i in range(8):
            if crc & 0x80:
                crc <<= 1
                crc ^= 0x131
            else:
                crc <<= 1
    return crc


class SI7021:

    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.init()
        self._measurement = 0

    def init(self):
        self.reset()

        while True:

            try:
                value = self.i2c.readfrom_mem(self.address, _READ_USER1, 1)[0]
            except OSError as e:
                if e.args[0] != 19:
                    raise
            else:
                break

    def _command(self, command):
        self.i2c.writeto(self.address, ustruct.pack('B', command))

    def _data(self):
        data = bytearray(3)
        data[0] = 0xff
        while True:

            try:
                self.i2c.readfrom_into(self.address, data)
            except OSError as e:
                if e.args[0] != 19:
                    raise
            else:
                if data[0] != 0xff:
                    break
        value, checksum = ustruct.unpack('>HB', data)
        if checksum != _crc(data[:2]):
            raise ValueError("CRC mismatch")
        return value

    def reset(self):
        self._command(_RESET)

    def humidity(self, raw=False, block=True):

        if not self._measurement:
            self._command(_HUMID_NOHOLD)
        elif self._measurement != _HUMID_NOHOLD:
            raise RuntimeError("other measurement in progress")
        if not block:
            self._measurement = _HUMID_NOHOLD
            return None
        self._measurement = 0
        value = self._data()
        if raw:
            return value
        return value * 125 / 65536 - 6

    def temperature(self, raw=False, block=True):

        if not self._measurement:
            self._command(_TEMP_NOHOLD)
        elif self._measurement != _TEMP_NOHOLD:
            raise RuntimeError("other measurement in progress")
        if not block:
            self._measurement = _TEMP_NOHOLD
            return None
        self._measurement = 0
        value = self._data()
        if raw:
            return value
        return value * 175.72 / 65536 - 46.85


if __name__ == "__main__":
    import machine

    i2c = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(2), freq=400000)
    s = SI7021(i2c)

    while True:

        ValeurTemp = 0
        ValeurHumid = 0
        moyenneTemp = 0
        moyenneHumid = 0

        for i in range(0, 5):
            ReceptionTemp = s.temperature()
            ReceptionHumid = s.humidity()
            ValeurTemp = ValeurTemp + ReceptionTemp
            ValeurHumid = ValeurHumid + ReceptionHumid
        moyenneTemp = ValeurTemp / 5
        moyenneHumid = ValeurHumid / 5

        url = 'http://192.168.137.187:5000/data_from_sonde'

        data = {'degre': moyenneTemp, 'teaux_humidite': moyenneHumid}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)

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


