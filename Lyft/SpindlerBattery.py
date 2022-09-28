from abc import abstractmethod

from Lyft.batt import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_service_date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date

    @abstractmethod
    def needs_service(self):
        pass