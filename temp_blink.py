  
from machine import Pin
from time import sleep
import utime

led = Pin(25, Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)

reading = sensor_temp.read_u16()*conversion_factor
temperature = 27 - (reading - 0.706)/0.001721 #actual reading in Cº, see pag 571 of the data sheet

while True:
    led.toggle()
    reading = sensor_temp.read_u16()*conversion_factor
    a = 27 - (reading - 0.706)/0.001721
    #frequency as a function of the change in temperture since turned on, change model and parameters at will
    dx = 4 + 2*(a - temperature)
    dy =((1/dx)**4)*150
    frequency_Hz = (1/dy)
    utime.sleep(dy)
    print("temperature:", a, "frequency_Hz:", frequency_Hz)