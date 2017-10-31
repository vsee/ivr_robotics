# example of a class - for storing your robot's state
# you can change the variables to store state in the class

import time
import math
import ev3dev.ev3 as ev3

class openLoopControl():
    def __init__(self):
        # time in seconds
        self.time_to_spin = 0.5
        # Speed in degrees per second
        self.speed_sp = 360

    def operateWheels(self):
        print("spin the wheels")
        print(str(self.time_to_spin) + " sec ")
        print(str(self.speed_sp) + " degrees/sec")
        print(" ")

        motor =ev3.LargeMotor('outA')
        motor.connected

        # run_time takes milliseconds
        motor.run_timed(speed_sp=self.speed_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) ) 
        motor.run_timed(speed_sp=-self.speed_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) )
