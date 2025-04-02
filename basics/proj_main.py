import numpy as np                                  # for array handling
import pysicktim as lidar                           # required for communication with TiM561 lidar sensor
import time
import L1_lidar
import L1_motor as motor
import L2_vector
import threading # only used for threading functions
import math
import csv
import L2_speed_control as sc # closed loop control. Import speed_control for open-loop
import L2_inverse_kinematics as inv #calculates wheel parameters from chassis
import L2_kinematics as kin    # calculates chassis parameters from wheels
import L1_log as log # log live data to local files
#import L1_gamepad as gp # for accessing gamepad directly

def detect():#look for metals, return true when found.
    pass

def drive(): #threshold of distance
    
        
    
if __name__ == "__main__":
    while True:
        dataset = L2_vector.getNearest()
        dist = dataset[0]
        angle = dataset[1]
        coord = L2_vector.polar2cart(dist, angle)
        x = coord[0]
        y = coord[1]
        speedL = 0.8
        speedR = 0.8
        print(x,y)
        '''Robot sweeps down to up from left to right. Once object is detected, 
        the robot will turn to the right 90, move forward, and turn 90 again'''
        
        if (x<=-0.200 and y<0.286):
            print("Turn!")
            #turn right
            motor.sendLeft(0.0)
            motor.sendRight(0.4)
            time.sleep(1)
        else:
            detect()
            motor.sendLeft(speedL)
            motor.sendRight(speedR)
            if (detect() == True):
                motor.sendLeft(0.0)
                motor.sendRight(0.0)
                #get location
                #pick up object
                motor.sendLeft(0.4)
                motor.sendRight(0.4)