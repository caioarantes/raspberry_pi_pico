# Temperatue Alarm with Buzzer and LED Set the an alam off for a temperature treashold. 
# Ajust the threshold tempetarure, alam will stop when temperute is below threshold again.

import time
from machine import Pin, PWM
from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)

#PWM frequency.
pwm = PWM(Pin(16)) #Buzzer at Pin 16 and any groud.
pwm_2 = PWM(Pin(25)) #Built-in LED Pin 25
pwm.freq(800)
pwm_2.freq(800)

def my_function(): # PWM function from the documentation, to turn on and off with fade both the Buzzer and LED a few times.
    duty = 0
    direction = 1
    for _ in range(8 * 256):
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        pwm_2.duty_u16(duty * duty)
        time.sleep(0.001)

while True:
    reading = sensor_temp.read_u16()*conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721 #actual reading in Cº, see pag 571 of the data sheet
    if temperature > 36: #threshold tempetarure
        print("temperature:",temperature)
        my_function()
    else: 
        print("temperature:",temperature)
        time.sleep(1)
