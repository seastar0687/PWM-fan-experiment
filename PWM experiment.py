from itertools import count
import spidev
import time
import os
import RPi.GPIO as GPIO
import signal
import sys

# open(bus, device) : open(X,Y) will open /dev/spidev-X.Y
spi = spidev.SpiDev()
spi.open(0,0)

# Read SPI data from MCP3008, Channel must be an integer 0-7
def ReadADC(ch):
    if ((ch > 7) or (ch < 0)):
       return -1
    adc = spi.xfer2([1,(8+ch)<<4,0])
    data = ((adc[1]&3)＜＜8) + adc[2]
    return data

# Convert data to voltage level
def ReadVolts(data,deci):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,deci)
    return volts

# Define sensor channels
light_ch = 0

# Define delay between readings
delay = 3

#-------------------------------------------------------------------------------------------------------------------------------------
FAN_PIN = 18            # PWM 控制腳位，設定成你想接的位置即可，注意是 BCM 編號
WAIT_TIME = 1           # 每次控制的更新頻率，單位為秒
PWM_FREQ = 50           # PWM 頻率，這邊根據 Noctua 規格使用 25kHz，其他風扇弄個 50 之類即可，若動作怪怪的可以在自行測試

FAN=10 #duty cycle
blades= #葉片個數
count=0
time_count=0
status=1
critical= #只要電壓值的臨界值

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
    fan = GPIO.PWM(FAN_PIN,PWM_FREQ)
    setFanSpeed(FAN)
    while time_count<6000:

        # Read the light sensor data
        light_data = ReadADC(light_ch)
        light_volts = ReadVolts(light_data,2)
        if light_volts>critical and status=1:
            count+=1
            status=0
        elif light_volts < critical and status=0:
            status=1
        time.count+=1
        time.sleep(0.001)
    print(count/blades) 

    # Print out results
    print "~C    Light : ",light_data," (",light_volts,"V)"

    # Delay seconds
    #time.sleep(delay)
