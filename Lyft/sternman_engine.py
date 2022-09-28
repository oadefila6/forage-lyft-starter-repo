from abc import ABC, abstractmethod

from Lyft.Engine import Engine


class SternmanEngine(Engine):

    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    @abstractmethod
    def needs_service(self):
        pass

    # def engine_should_be_serviced(self):
    #     return self.current_mileage - self.last_service_mileage > 30000
    # def __init__(self, last_service_date, warning_light_is_on):
    #     super().__init__(last_service_date)
    #     self.warning_light_is_on = warning_light_is_on

    # def engine_should_be_serviced(self):
    #     if self.warning_light_is_on:
    #         return True
    #     else:
    #         return False
