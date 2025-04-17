class Contact():
    def __init__(self,name,lastname,phonenumber):
        self.name=name
        self.lastname=lastname
        self.phonenumber=phonenumber


class Agenda(Contact):
    def __init__(self):
        self.my_agenda=[]
        self.person=[]
        self.my_contact={}
        self.my_contact_header=['Nombre:','Apellido:','Numero de Telefono:']
    
    
    def adding_contacts(self,name,lastname,phonenumber):
        self.name=name
        self.lastname=lastname
        self.phonenumber=phonenumber
        self.person.append(self.name,self.lastname,self.phonenumber)
        for item in self.my_contact_header:
            self.my_contact[item]=self.person[index]
            index+=1
        self.my_agenda.append(self.my_contact)


    def deleting_contacts(self):
        self.my_agenda.pop()


class Message(Agenda):
    def sending_message(self,body_message,phone_number):
        self.body_message=body_message
        self.phone_number=phone_number
        print(f'Estoy enviando el mensaje: {self.body_message} al numero: {self.phone_number}')


class Phone(Agenda):
    def calling(self,contact_number):
        self.contact_number=contact_number
        print(f'Estoy llamando al numero: {self.contact_number}')
        
    
    def reciving_call(self,contact_number):
        pass


class File():
    def __init__(self,name,extension,file_number,size):
        self.name=name
        self.extension=extension
        self.size=size
        self.file_number=file_number
    


class AudioPlayer(File):
    def reproduce_audio(self,audiofile):
        print(f'I am reproducing the{audiofile.name}')


class VideoPlayer(File):
    def reproduce_video(self,videofile):
        print(f'I am reproducing the{videofile.name}')


class Camera(File):
    def activate_camera(self):
        print("Hola Soy una camara")


class Storage(File):
    

    def __init__(self):
        self.my_storage=[]
        self.my_dict_files={}
        self.my_files_headers=[]
        self.my_files_values=[]


    def storaging_files(self,my_file):
        self.my_file=my_file
        self.my_files_values.append(my_file.name,my_file.extension,my_file.size)


class Device(Phone,AudioPlayer,VideoPlayer,Camera,Message):
    def __init__(self,is_on,signal_on,batery_on):
        self.is_on=is_on
        self.is_signal=signal_on
        self.batery_on=batery_on
    

    def execute_instruction(self,my_device):
        self.my_device=my_device


def main():
    phone_is_on=True
    signal_is_on=True
    batery_is_on=True
    my_device=Device(phone_is_on,signal_is_on,batery_is_on)
    while phone_is_on==True:
        try:
            my_instruction=int(input("Por favor ingrese un comando. 1.Encender Movil, 2.Realizar Llamada, 3. Enviar SMS, 4.Apagar Movil"))
            if my_instruction==1:
                print("Hola!!!.Bienvenido a su Dispositivo Movil")
            if my_instruction==2:
                try:
                    my_call_input=int(input("Ingrese la accion que desea realizar 1.Llamar a un numero, 2. Regresar"))
                    if my_call_input<1 or my_call_input>2:
                        raise Exception
                except ValueError:
                    print("El menu del dispositivo no recibe letras")
                except Exception as err:
                    print("El dispositivo solo recibe numeros entre 1 y 2 como respuesta de este menu")
                if my_call_input==1:
                    try:
                        telephone_number=int(input("Ingrese el numero de telefono por favor: "))
                        my_device.calling(telephone_number)
                    except ValueError:
                        print("El numero de telefono debe ser un numero no debe contener letras")
            if my_instruction==3:
                try:
                    my_message_input=int(input("Ingrese la accion que desea realizar 1.Textear a un numero, 2. Regresar"))
                    if my_message_input==1:
                        try:
                            telephone_number=int(input("Ingrese el numero de telefono por favor: "))
                            my_texting=input("Digite por favor el mensaje que desea enviar: ")
                            my_device.sending_message(my_texting,telephone_number)
                        except ValueError:
                            print("El numero de telefono debe ser un numero no se permiten letras")
                    if my_message_input<1 or my_message_input>2:
                        raise Exception
                except ValueError:
                    print("El menu del dispositivo no recibe letras")
                except Exception as err:
                    print("El menu del dispositivo solo recibe numeros entre 1 y 2")
            if my_instruction==4:
                phone_is_on=False
            if my_instruction<1 or my_instruction>4:
                raise Exception
        except ValueError:
            print("Por favor ingrese un numero de instruccion valido, no se reciben letras")
        except Exception as err:
            print("El menu solo recibe numeros entre  y 4")

main()