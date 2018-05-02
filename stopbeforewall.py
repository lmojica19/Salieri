# Preliminary requisites
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

# Move forward
while RPL.digitalRead(17) == 1:
    RPL.servoWrite(1,1000)
    RPL.servoWrite(2,2000)
else:
    break

# Stop moving
while RPL.digitalRead(17) == 0:
    RPL.servoWrite(1,0)
    RPL.servoWrite(2,0)
else:
    break

"""

ssh student@192.168.21.121

"""
