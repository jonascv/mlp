from route_strategy import *

class Pedestrian:

    def __init__(self, name: str):
        self.name = name
        self.route = None

    def setRoute(self, route: Route):
        self.route = route.instance()
        
    def move(self):
        if self.route is not None:
            self.route.operation()
        else:
            print("No route selected.")

if __name__ == '__main__':

   pedestrian_1 = Pedestrian("Pedestrian 1")
   pedestrian_1.setRoute(SuperSafe) # Client: Route is set to Super Safe.
   pedestrian_1.move()