import L1_log
import L1_lidar
import L2_vector

if __name__ == "__main__":
    while True:
        dataset = L2_vector.getNearest()
        dist = dataset[0]
        angle = dataset[1]
        coord = L2_vector.polar2cart(dataset[0], dataset[1])
        x = coord[0]
        y = coord[1]
        print(f"Distance: {dist}m    Angle: {angle}deg  Coordinates: {x,y}")
        L1_log.tmpFile(dist, "dist.txt")
        L1_log.tmpFile(angle, "angle.txt")
        L1_log.tmpFile(x, "x.txt")
        L1_log.tmpFile(y, "y.txt")