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
#import Lab7Template

def detect():#look for metals, return true when found.
    pass

def marker():#capture coordinates and log location of metals on nodeRed
    pass
    
if __name__ == "__main__":
    '''#ask for manual or automatic control
    t0 = 0  # time sample
    t1 = 1  # time sample
    e00 = 0 # error sample
    e0 = 0  # error sample
    e1 = 0  # error sample
    dt = 0  # delta in time
    de_dt = np.zeros(2) # initialize the de_dt
    pdTargets = np.array([9.7, 9.7]) # Input requested PhiDots (radians/s)
    #pdTargets = inv.getPdTargets() # populates target phi dots from GamePad
    kin.getPdCurrent() # capture latest phi dots & update global var
    pdCurrents = kin.pdCurrents # assign the global variable value to a local var
            
    # THIS BLOCK UPDATES VARIABLES FOR THE DERIVATIVE CONTROL
    t0 = t1  # assign t0
    t1 = time.time() # generate current time
    dt = t1 - t0 # calculate dt
    e00 = e0 # assign previous previous error
    e0 = e1  # assign previous error
    e1 = pdCurrents - pdTargets # calculate the latest error
    de_dt = (e1 - e0) / dt # calculate derivative of error

    # CALLS THE CONTROL SYSTEM TO ACTION
    #sc.driveOpenLoop(pdTargets)  # call on open loop
    #sc.driveClosedLoop(pdTargets, pdCurrents, de_dt)  # call on closed loop
    #time.sleep(0.05) # this time controls the frequency of the controller
    '''
    while True:
        dataset = L2_vector.getNearest()
        dist = dataset[0]
        angle = dataset[1]
        coord = L2_vector.polar2cart(dist, angle)
        x = coord[0]
        y = coord[1]
        speedL = 0.8
        speedR = 0.8
        rturn = True
        print(dist,angle,x,y)
        '''Robot sweeps down to up from left to right. Once object is detected, 
        the robot will turn to the right 90, move forward, and turn 90 again'''
        
        if (dist<=0.6 and -10.0<=angle<=10.0):
            print("Turn!")
            if (rturn == True):#turn right
                motor.sendLeft(0.5)
                motor.sendRight(-0.5)
                time.sleep(3)
                rturn = False
            else:#turn left
                motor.sendLeft(-0.5)
                motor.sendRight(0.5)
                time.sleep(3)
                rturn = True
        else:
            detect()
            #sc.driveOpenLoop(pdTargets)
            motor.sendLeft(speedL)
            motor.sendRight(speedR)
            if (detect() == True):
                motor.sendLeft(0.0)
                motor.sendRight(0.0)
                #get location of metal and drop marker
                marker()
                motor.sendLeft(speedL)
                motor.sendRight(speedR)