#IMPORT RELATED LIBRARY
from machine import Pin, ADC
import time

#CONSTANT

#GLOBAL VAR
ledTick = 0
adcTick = 0

#USER DEFINE CLASS

#USER DEFINE FUNCTION
start_time = time.ticks_ms()
def millis():
    return time.ticks_ms() - start_time

#SETUP SECTION
led = Pin(2, Pin.OUT)
pot = ADC(Pin(34))
'''
ADC.ATTN_0DB — the full range voltage: 1.2V
ADC.ATTN_2_5DB — the full range voltage: 1.5V
ADC.ATTN_6DB — the full range voltage: 2.0V
ADC.ATTN_11DB — the full range voltage: 3.3V
'''
pot.atten(ADC.ATTN_11DB)

'''
ADC.WIDTH_9BIT = 9 - full range ADC: 512
ADC.WIDTH_10BIT = 10 - full range ADC: 1024
ADC.WIDTH_11BIT = 11 - full range ADC: 2048
ADC.WIDTH_12BIT = 12 - full range ADC: 4096
'''
pot.width(ADC.WIDTH_12BIT)	#optional

#LOOP SECTION
while True:    
    if millis() >= ledTick:
        ledTick = millis()+1000
        led.value(not led.value())
    if millis() >= adcTick:
        adcTick = millis()+1000
        raw_adc = pot.read_u16()  # read a raw analog value in the range 0-65535
        adc_value = pot.read()
        microVolt = pot.read_uv()   # read an analog value in microvolts
        message_str = "RAW analog (0-65535): {}, ADC Value (0-4095): {}, MicroVolt: {:.3f}V".format(raw_adc,adc_value, float(microVolt)/1000000)
        print(message_str)