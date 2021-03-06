import RoboPiLib as RPL
import sys, tty, termios, signal
motorL = 0
motorR = 1

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

try:
  RPL.pinMode(motorL,RPL.SERVO)
  RPL.servoWrite(motorL,1500)
  RPL.pinMode(motorR,RPL.SERVO)
  RPL.servoWrite(motorR,1500)
except:
  pass

def stopAll():
  try:
    RPL.servoWrite(motorL,1500)
    RPL.servoWrite(motorR,1500)
  except:
    print "error except"
    pass

def forward():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,motorR_forward)

def reverse():
  RPL.servoWrite(motorL,motorL_backward)
  RPL.servoWrite(motorR,motorR_backward)

 def interrupted(signum, frame): # this is the method called at the end of the alarm
   stopAll()

 signal.signal(signal.SIGALRM, interrupted) # this calls the 'interrupted' method when the alarm goes off
 tty.setraw(sys.stdin.fileno()) # this sets the style of the input

 print "Ready To Drive! Press * to quit.\r"
 ## the SHORT_TIMEOUT needs to be greater than the press delay on your keyboard
 ## on your computer, set the delay to 250 ms with `xset r rate 250 20`
 SHORT_TIMEOUT = 0.255 # number of seconds your want for timeout
 while True:
   signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) # this sets the alarm
   ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
   signal.setitimer(signal.ITIMER_REAL,0) # this turns off the alarm
   if ch == '*': # pressing the asterisk key kills the process
    stopAll() # stops everything from moving
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # this resets the console settings
    break # this ends the loop
   else:
     if ch == 'w':
       forward()
     elif ch == "a":
       left()
     elif ch == "s":
       reverse()
     elif ch == "d":
       right()
     elif ch == "e":
       forward_right()
     elif ch == "q":
       forward_left()
     elif ch == "z":
       backward_left()
     elif ch == "c":
       backward_right()
     elif ch == "]":
       forwardSpeedChanges(100)
     elif ch == "[":
       backwardSpeedChanges(-100)
     elif ch == "}":
       forwardSpeedChanges(-100)
     elif ch == "{":
       backwardSpeedChanges(100)
     elif ch == "1":
       forwardLeftSpeedChange(100)
     elif ch == "!":
       forwardLeftSpeedChange(-100)
     elif ch == "2":
       forwardRightSpeedChange(100)
     elif ch == "@":
       forwardRightSpeedChange(-100)
     elif ch == "3":
       backwardLeftSpeedChange(-100)
     elif ch == "#":
       backwardLeftSpeedChange(100)
     elif ch == "4":
       backwardRightSpeedChange(-100)
     elif ch == "$":
       backwardRightSpeedChange(100)
     else:
       stopAll()

#Start with this
"""
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

#Sensor
RPL.digitalRead()
# The arg depends on which port the wire's in

# Move forward
RPL.servoWrite(0,1000)
RPL.servoWrite(1,2000)

# Move backward
RPL.servoWrite(0,2000)
RPL.servoWrite(1,1000)

# Pivot around left wheel
RPL.servoWrite(0,1500)
RPL.servoWrite(1,2000)

# Pivot around right wheel
RPL.servoWrite(0,1000)
RPL.servoWrite(1,1500)

# Spin left
RPL.servoWrite(0,2000)
RPL.servoWrite(1,2000)

#Spin right
RPL.servoWrite(0,1000)
RPL.servoWrite(1,1000)

# Stop
RPL.servoWrite(0,0)
RPL.servoWrite(1,0)

"""
