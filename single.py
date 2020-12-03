from machine import I2C, Pin
import mpu6050

def value():
	i2c = I2C(scl=Pin(22), sda=Pin(21))
	acc = mpu6050.accel(i2c)
	return acc.get_values()
