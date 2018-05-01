import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.servoWrite(1,2000)
RPL.servoWrite(2,1000)
