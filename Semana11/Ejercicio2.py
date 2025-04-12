
class Bus():
    def __init__(self):
      self.max_passengers=30
      self.passengers_in_bus=0


    def add_passengers(self):
      while (self.passengers_in_bus<self.max_passengers):
          self.passengers_in_bus+=1
          print(self.passengers_in_bus)
    

    def get_down_passengers(self):
      while (self.passengers_in_bus!=0):
        self.passengers_in_bus-=1
        print(self.passengers_in_bus)


my_new_bus=Bus()
my_new_bus.add_passengers()
my_new_bus.get_down_passengers()