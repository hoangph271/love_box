from machine import Pin

IN1 = Pin(6, Pin.OUT)
IN2 = Pin(7, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(3, Pin.OUT)

def right_forward():
    IN1.high()
    IN2.low()
def right_backward():
    IN1.low()
    IN2.high()
def stop_right():
    IN1.low()
    IN2.low()

def left_forward():
    IN3.high()
    IN4.low()
def left_backward():
    IN3.low()
    IN4.high()
def stop_left():
    IN3.low()
    IN4.low()

def stop_all():
    stop_right()
    stop_left()
