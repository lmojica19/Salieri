"""import threading

def printit():
  threading.Timer(2.0, printit).start()
  print "Hello, World!"
  threading.Timer(2.0, printit).start()
  print "Second time"

printit()
"""
import threading

def susume():
    print "Susume!"
    threading.Timer(3, matte).start()

def matte():
    print "Matte!"
    threading.Timer(3, susume).start()

susume()
