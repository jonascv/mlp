from abc import ABC, abstractmethod

class Route(ABC):
    __instance = None
        
    @abstractmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
    
    def operation(self):
        pass

class SuperSafe(Route):
    def operation(self, distance):
        print("Client: Route is set to Super Safe.")


class Safe(Route):
    def operation(self, distance):
        print("Client: Route is set to Safe.")


class NotSafe(Route):
    def operation(self, distance):
        print("Client: Route is set to Not Safe.")