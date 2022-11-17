from machine import Pin
import uasyncio

async def setup_motors():
    IN1 = Pin(2, Pin.OUT)
    IN2 = Pin(3, Pin.OUT)

    IN1.low()
    IN2.high()

    await uasyncio.sleep(1.25)
