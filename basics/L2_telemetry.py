import L1_ina
import L1_log
import time
if __name__ == "__main__":
    while True:
        vols = L1_ina.readVolts()
        time.sleep(0.2)
        L1_log.tmpFile(vols, "data")