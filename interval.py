import threading

def susume():
    print "Susume!"
    RPL.servoWrite(1,1000)
    RPL.servoWrite(2,2000)
    threading.Timer(3, matte).start()

def matte():
    print "Matte!"
    RPL.servoWrite(1,0)
    RPL.servoWrite(2,0)
    threading.Timer(3, susume).start()

susume()
