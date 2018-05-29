# Preliminary requisites
import threading
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

# Move forward
def forward():
    while RPL.digitalRead(17) == 1:
        RPL.servoWrite(1,1000)
        RPL.servoWrite(2,2000)
        if RPL.digitalRead(17) == 0:
            sokomade()


# Stop moving
def sokomade():
    RPL.servoWrite(1,1000)
    RPL.servoWrite(2,1000)
    threading.Timer(0.2, forward).start()

# plan B
def mattete():
    while RPL.digitalRead(17) == 0:
        RPL.servoWrite(1,1000)
        RPL.servoWrite(2,1000)
        if RPL.digitalRead(17) == 1:
            forward()

forward()

"""

ssh student@192.168.21.121

ctrl c to cease

"""
