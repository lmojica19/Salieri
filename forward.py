import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.servoWrite(1,1000)
RPL.servoWrite(2,2000)

"""

ssh student@192.168.21.121

"""
