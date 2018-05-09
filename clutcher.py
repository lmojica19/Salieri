import threading
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def susume():
    RPL.servoWrite(1,1000)
    RPL.servoWrite(2,2000)
    threading.Timer(3, matte).start()

def matte():
    RPL.servoWrite(0,0)
    RPL.servoWrite(1,0)
    RPL.servoWrite(2,0)
    threading.Timer(3, susume).start()

susume()
