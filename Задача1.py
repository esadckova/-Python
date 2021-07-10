from time import sleep


class TrafficLight:
    __color = 0

    def running(self):
        while True:
            print("red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(10)


trafficlight = TrafficLight()
trafficlight.running()
