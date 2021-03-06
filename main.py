import network
import time
import arm 
import os
import PWM
import machine
import kinematics

Arm =arm.arm()
Arm.begin()
buff=bytearray(1)

i2c = machine.I2C(scl=machine.Pin(12),sda=machine.Pin(14))

if i2c.scan()==[57]:
	buff[0]=0
	i2c.writeto_mem(57,0x80,buff)
	buff[0]=219
	i2c.writeto_mem(57,0x81,buff)
	buff[0]=246
	i2c.writeto_mem(57,0x83,buff)
	buff[0]=0x60
	i2c.writeto_mem(57,0x8D,buff)
	buff[0]=1
	i2c.writeto_mem(57,0x8F,buff)
	buff[0]=3
	i2c.writeto_mem(57,0x80,buff)

def readcolor():
	color=bytearray(8)
	i2c.readfrom_mem_into(57,0x94,color)
	amb = color[0]+((int)(color[1])<<8)
	R = color[2]+((int)(color[3])<<8)
	G = color[4]+((int)(color[5])<<8)
	B = color[6]+((int)(color[7])<<8)
	print("amb: ",amb," R: ",R," G: ",G," B: ",B)


echo = machine.Pin(13,machine.Pin.IN)
trig = machine.Pin(15,machine.Pin.OUT)

def ultra():
	trig.low()
	time.sleep_ms(2)
	trig.high()
	time.sleep_ms(10)
	trig.low()
	while echo.value() == 0:
		pass
	t1 = time.ticks_us()
	while echo.value() == 1:
		pass
	t2 = time.ticks_us()
	cm = (t2 - t1) / 58.0
	print(cm)

	