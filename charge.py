import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.servoWrite(0,1000)
RPL.servoWrite(1,2000)
RPL.servoWrite(2,2000)
RPL.servoWrite(3,1000)

"""

ssh student@192.168.21.121

"""
