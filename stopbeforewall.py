# Preliminary requisites
import RoboPiLib as RPL

# Move forward
RPL.servoWrite(0,1000)
RPL.servoWrite(1,2000)

# Stop moving
if RPL.digitalRead(16) == 0:
    RPL.servoWrite(0,0)
    RPL.servoWrite(1,0)
