
class Bus():
    def __init__(self):
      self.max_passengers=30
      self.passengers_in_bus=0


    def add_passengers(self,person):
        self.passengers_in_bus+=person.space
        return self.passengers_in_bus
    

    def get_down_passengers(self,person):
        self.passengers_in_bus-=person.space
        return self.passengers_in_bus

class Person():
  def __init__(self):
    self.space=1


def transport_person():
  bus_on_track=True
  int_action=0
  
  my_new_bus=Bus()
  
  
  while bus_on_track==True:
    new_person=Person()
    print("Aquí vamos el ray empezo!!!")
    int_action=int(input("Ingrese Por favor lo que desea realizar en el autobus. 1. Subir Persona, 2. Bajar Persona, 3.Mostrar cantidad de personas en el Bus, 4.Fin de la Ruta: "))
    try:
      if int_action==1:
        if my_new_bus.passengers_in_bus<my_new_bus.max_passengers:
          print(f'En el bus hay: {my_new_bus.add_passengers(new_person)} pasajeros')
        else:
          print("No se puede subir nadie el Bus va a su máxima capacidad")
      if int_action==2:
        if my_new_bus.passengers_in_bus!=0:
          print(f'En el bus hay: {my_new_bus.get_down_passengers(new_person)} pasajeros')
        else:
          print("No se puede bajar nadie el Bus tiene 0 pasajeros")
      if int_action==3:
        print(f'En el bus hay: {my_new_bus.passengers_in_bus} pasajeros')
      if int_action==4:
        bus_on_track=False
      if int_action<1 or int_action>4:
        raise Exception
    except ValueError:
      print("El Bus no reconoce letras")
    except Exception as ex:
      print("El Bus solo reconoce opciones entre 1 y 4")


transport_person()