import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.servoWrite(0,0)
RPL.servoWrite(1,0)
RPL.servoWrite(2,0)
