#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3

# Local Imports
import tutorial as tutorial
import utilities
import openLoopControl as olc

print ('Welcome to ev3')

#ev3.Sound.speak('Welcome to e v 3').wait()

#g = ev3.GyroSensor()
#while True:
#    #print g.value()

m = ev3.LargeMotor('outA')
m.connected
m.run_timed(time_sp=3000, duty_cycle_sp=75)
m.position()

#gs.mode = 'GYRO-ANG'

# Step a Basic open driving
#tutorial.operateWheelsBasic()

# Step b Turn on an off an LED using a switch
#tutorial.makeLightSwitch()

# Step c Use switches to drive robot back and forward
#tutorial.makeLightAndMotorSwitch()


# Step d Use a class to develop a bigger program with a state
#o = olc.openLoopControl()
## execute (with default params)
#o.operateWheels()
#
## update parameters
#o.time_to_spin = 1.0
#o.duty_cycle_sp = 50
#
## execute again
#o.operateWheels()


# remove this if you want it to exit as soon as its done:
print "wait 10sec, then end"
time.sleep(10)