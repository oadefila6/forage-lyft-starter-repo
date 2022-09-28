import zope.interface
from abc import ABC, abstractmethod

from Lyft.Serviceable import Serviceable


@zope.interface.implementer(Serviceable)
class Car(ABC):
    def __init__(self, Engine, Battery):
        self.Engine = Engine
        self.Battery = Battery

    @property
    def engine(self):
        return f"{self.engine}"

    @property
    def battery(self):
        return f"{self.battery}"

    @abstractmethod
    def needs_service(self):
        pass
