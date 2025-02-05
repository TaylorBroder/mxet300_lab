import L2_compass_heading
import L1_log
import time

def lab():
    return L2_compass_heading.get_heading()

def postlab(value):
    if value > -30 and value < 30:
        return "North"
    elif value > 30 and value < 60:
        return "North East"
    elif value > 60 and value < 120:
        return "East"
    elif value > 120 and value < 150:
        return "South East"
    elif value > 150 and value <-150:
        return "South"
    elif value > -150 and value < -120:
        return "South West"
    elif value > -120 and value < -60:
        return "West"
    else:
        return "North West"
        
if __name__ == "__main__":
    while True:
        value = lab()
        heading = postlab(value)
        print(value, heading)
        time.sleep(0.2)
        L1_log.tmpFile(value, "value.txt")
        L1_log.stringTmpFile(heading, "heading.txt")