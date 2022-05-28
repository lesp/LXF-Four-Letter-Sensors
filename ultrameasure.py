from gpiozero import DistanceSensor
from time import sleep
from w1thermsensor import W1ThermSensor
import fourletterphat

sensor = W1ThermSensor()
ultra = DistanceSensor(17, 27)

while True:
    distance = str(round(ultra.distance * 100,1))
    fourletterphat.print_str("DIST")
    fourletterphat.show()
    sleep(20)
    print('Distance to nearest object is', distance, 'CM')
    fourletterphat.clear()
    fourletterphat.print_str(distance)
    fourletterphat.show()
    sleep(1)
    fourletterphat.print_str("TEMP")
    fourletterphat.show()
    sleep(2)
    temp = str(sensor.get_temperature())
    print('The Temperature is', temp, 'C')
    fourletterphat.clear()
    fourletterphat.print_str(temp)
    fourletterphat.show()
    sleep(1)

