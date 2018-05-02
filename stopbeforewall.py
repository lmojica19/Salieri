# Preliminary requisites
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

# Move forward
RPL.servoWrite(1,1000)
RPL.servoWrite(2,2000)

# Stop moving
if RPL.digitalRead(17) == 0:
    RPL.servoWrite(1,0)
    RPL.servoWrite(2,0)

"""

ssh student@192.168.21.121

"""
