from machine import Pin, I2C

def run_check():
	
    from machine import Pin, I2C
    i2c = I2C(scl=Pin(22), sda=Pin(21))
    print(i2c.scan())
    print(hex(i2c.scan()[0]))