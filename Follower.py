import machine
L_sensor = machine.Pin(13, machine.Pin.IN,machine.Pin.PULL_UP) #D7
R_sensor = machine.Pin(5, machine.Pin.IN,machine.Pin.PULL_UP)  #D1
L_F_motor2=machine.PWM(machine.Pin(2),freq=500,duty=300)  #D4
R_F_motor1=machine.PWM(machine.Pin(0),freq=500,duty=300)  #D3
def Forword():
    R_F_motor1.duty(300)
    L_F_motor2.duty(300)
def stop():
    R_F_motor1.duty(0)
    L_F_motor2.duty(0)
def Right():
    R_F_motor1.duty(300)
    L_F_motor2.duty(0)
def Left():
    R_F_motor1.duty(0)
    L_F_motor2.duty(300)

print("Done")
while(1):

    if R_sensor.value() == 0 and L_sensor.value() == 0:
        Forword()
        print("Forword")

    elif R_sensor.value() == 0:
        Left()
        print("Left")

    elif L_sensor.value() == 0:
        Right()
        print("Right")

    elif R_sensor.value() == 1 and L_sensor.value() == 1:
        stop()
        print("Stop")





