
def operateWheels():
    print("spin the wheels")

    motor =ev3.LargeMotor('outA')
    motor.connected

    motor.run_timed(speed_sp=720, time_sp=500)
    time.sleep(1)
    motor.run_timed(speed_sp=-720, time_sp=500)

    print('sleeping for 3 seconds')
    time.sleep(3)
