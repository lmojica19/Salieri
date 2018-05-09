import threading
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def runner():
    while True:
        RPL.servoWrite(1,1000)
        RPL.servoWrite(2,2000)
        threading.Timer(5.0, printit).start()
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,0)
        RPL.servoWrite(2,0)
        runner()

runner()

"""

ssh student@192.168.21.121

ctrl c to cease

"""
