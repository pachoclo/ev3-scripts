#!/usr/bin/env python3
#from ev3dev.ev3 import *

import ev3dev.ev3 as ev3

welcome_msg = 'Welcome to this crazy town bitches!'

print('\tRobot> ' + welcome_msg)

ev3.Sound.speak(welcome_msg).wait()


