from abc import ABC, abstractmethod
import random

class Robot(ABC):
    def __init__(self,name):
        self.name = name
        self.battery = random.randint(0,100)

    @abstractmethod
    def perform_task(self):
        pass

    def battery_status(self):
        return(f"{self.name} baterijas līmenis: {self.battery} %")

class CleaningRobot(Robot):
    def perform_task(self):
        return(f"{self.name} tīra telpu ar putekļusūcēju!")

class SecurityRobot(Robot):
    def perform_task(self):
        return(f"{self.name} patrulē teritorijā un skenē apkārtni!")

class CookingRobot(Robot):
    def perform_task(self):
        return(f"{self.name} gatavo gardu ēdienu!")

robots = [
    CleaningRobot("RoboCleaner"),
    SecurityRobot("RoboGuard"),
    CookingRobot("ChefBot")]

for robot in robots:
    print(robot.battery_status())
    print(robot.perform_task())
    print("-"*30)

