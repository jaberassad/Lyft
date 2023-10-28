class Car:
    def __init__(self,engine,battery,time_since_last_service):
        self.engine = engine
        self.battery=battery
        self.time_since_last_service=time_since_last_service
    
class Calliope(Car):
    def __init__(self,engine,battery,time_since_last_service,milleage,):
        super().__init__(engine,battery,time_since_last_service)
        self.milleage=milleage
    def needs_services(self):
        if self.milleage>30000 and self.time_since_last_service>730:
            return True

class Glissade(Car):
    def __init__(self,engine,battery,time_since_last_service,milleage,):
        super().__init__(engine,battery,time_since_last_service)
        self.milleage=milleage
    def needs_services(self):
        if self.milleage>60000 and self.time_since_last_service>730:
            return True

class Palindrome(Car):
    def __init__(self,engine,battery,time_since_last_service,warning_detector,):
        super().__init__(engine,battery,time_since_last_service)
        self.warning_detector=warning_detector
    def needs_services(self):
        if self.warning_detector==True and self.time_since_last_service >730:
            return True

class Thovex(Car):
    def __init__(self,engine,battery,time_since_last_service,milleage,):
        super().__init__(engine,battery,time_since_last_service)
        self.milleage=milleage
    def needs_services(self):
        if self.milleage>30000 and self.time_since_last_service>1460:
            return True

class Roschach(Car):
    def __init__(self,engine,battery,time_since_last_service,milleage,):
        super().__init__(engine,battery,time_since_last_service)
        self.milleage=milleage
    def needs_services(self):
        if self.milleage>60000 and self.time_since_last_service>1460:
            return True     