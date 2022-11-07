from machine import Pin

led = Pin('LED', Pin.OUT)

def led_on():
  led.on()

def led_off():
  led.off()
