import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

while True:
    print RPL.digitalRead(15)
