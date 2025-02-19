import L2_kinematics
import L2_inverse_kinematics
import L2_speed_control
import L1_log
import L1_ina

if __name__ == "__main__":
    while True:
        speedL = L2_kinematics.getMotion()[0]
        speedR = L2_kinematics.getMotion()[1]
        xdot= L2_kinematics.getPdCurrent()[0]
        thetadot= L2_kinematics.getPdCurrent()[1]
        volts = L1_ina.readVolts()
        L1_log.tmpFile(volts, "voltage.txt")
        L1_log.tmpFile(speedL, "speedL.txt")
        L1_log.tmpFile(speedR, "speedR.txt")
        L1_log.tmpFile(xdot, "xdot.txt")
        L1_log.tmpFile(thetadot, "thetadot.txt")
        print(f"Voltage: {volts}    Chassis speed: {speedL,speedR}   [xdot, thetadot]: {xdot, thetadot}")
        