import L1_ina
import L1_log
import time
if __name__ == "__main__":
    #volSet = []
    while True:
        vols = L1_ina.readVolts()
        #volSet.append(vols)
        time.sleep(0.2)
        L1_log.uniqueFile(vols, "data")