from machine import Pin

IN1 = Pin(6, Pin.OUT)
IN2 = Pin(7, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(3, Pin.OUT)

def forward_right():
    IN1.high()
    IN2.low()
def backward_right():
    IN1.low()
    IN2.high()
def stop_right():
    IN1.low()
    IN2.low()

def forward_left():
    IN3.high()
    IN4.low()
def backward_left():
    IN3.low()
    IN4.high()
def stop_left():
    IN3.low()
    IN4.low()

def stop_both():
    stop_right()
    stop_left()
