class Sleevy:
    def __init__(self,n_serie):
        self.n_serie=n_serie

class Sensor(Sleevy) :
     def __init__(self, type, position, data_type) :
         self.type = type
         self.position = position
         self.data_type = data_type

class PPG(Sensor) :
    def get_info(self) :
        print(f"I'm the {self.type} sensor set up in {self.position} in the {self.n_serie} Sleevy")
   
    def task(self) :
        print(f"I'm sending {self.data_type} data")
 
 
class EMG(Sensor) :
    def get_info(self) :
        print(f"I'm the {self.type} sensor set up in {self.position}")
 
    def task(self) :
        print(f"I'm sending {self.data_type} data")
 
class Accel(Sensor) :
    def get_info(self) :
        print(f"I'm the {self.type} sensor set up in {self.position}")
   
    def task(self) :
        print(f"I'm sending {self.data_type} data")
 
 
class Heat(Sensor) :
    def get_info(self) :
        print(f"I'm the {self.type} sensor set up in {self.position}")
 
    def task(self) :
        print(f"I'm sending {self.data_type} data")
class Interface(Sleevy) :
    def __init__(self, username, password) :
        self.username = username
        self.password = password
 
    def log_in(self) :
        print(f"To connect, please enter your {self.username} and your {self.password}")