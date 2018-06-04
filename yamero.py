import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def forward():
    while RPL.digitalRead(17) == 1:
        RPL.servoWrite(1,1000)
        RPL.servoWrite(2,2000)
        if RPL.digitalRead(17) == 0:
            stoppu()

def stoppu():
    RPL.servoWrite(0,0)
    RPL.servoWrite(1,0)
    RPL.servoWrite(2,0)
    RPL.servoWrite(3,0)
    RPL.servoWrite(4,0)
    RPL.servoWrite(5,0)

forward()

"""

ssh student@192.168.21.121

ctrl c to cease

"""
