import time
from prettyprinter import pprint

class TrafficLights:
    """class representng traffic light at a junction of 4 roads in four different direction"""

    def __init__(self,direction = "east"):

        # Mode in which the traffic lights operate
        self.direction = direction

        #dict representing lights in 4 direction in a junction
        self.direction_dict = {
            "east" : "red",
            "south" : "red",
            "west" : "red",
            "north" : "red"
            }
    
    def automatic_mode(self):
        """
        Function to automatic control of the traffic lights
        Control will trun green one of the light and waits for 10 seconds and turns the next signal green
        the control will be moving in clockwise direction

        """
        
        direction_index = list(self.direction_dict.keys()).index(self.direction)
        direction_list = list(self.direction_dict.keys())

        try:

            while (True):

                self.direction_dict[direction_list[direction_index]] = "green"
                self.direction_dict[direction_list[direction_index-1]] = "red"
                pprint(self.direction_dict)
                print("Press Cntrl-C to take mannual control")

                time.sleep(10)
                direction_index = (direction_index+1)%4
        
        except KeyboardInterrupt:
            self.direction_dict[direction_list[direction_index]] = "red"
            self.mannual_mode()
    

    def mannual_mode(self):

        """
        mannual control of the traffic lights , given lane will be turned green until we specify with lane should turn green next
        
        """

        while(True):
            direction = input("enter the direction to turn green or press A to go automatic mode : ")

            if direction == "a" or direction == "A":
                self.automatic_mode()

            self.direction = direction
            self.direction_dict[self.direction] = "green"

            pprint(self.direction_dict)
            
            self.direction_dict[self.direction] = "red"


if __name__ == "__main__":

    traffic_signal = TrafficLights()
    traffic_signal.automatic_mode()