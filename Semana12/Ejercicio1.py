class BankAccount():
    balance=int(input("Indique Por Favor el monto de su balance: "))


    def depositing_money(self,deposit):
        self.deposit=deposit
        self.balance=self.balance+self.deposit
        print(self.balance)


    def withdraw_money(self,withdraw):
        self.withdraw=withdraw
    

class SavingsAccount(BankAccount):
    def __init__(self):
        try:
            self.minbalance=int(input("Por favor indique cual es el balance Mínimo: "))
        except ValueError:
            print("El balance minimo no pueden ser letras o tener valores negativos")
    def min_balance(self):
        if (self.balance-self.withdraw)<=self.minbalance:
            print("Operación No se puede realizar, Balance Insuficiente")
        else:
            self.balance=self.balance-self.withdraw
            print(self.balance)


def bank_operation():
    my_boolean=True
    my_saving_account=SavingsAccount()

    while (my_boolean==True):        
        try:
            my_bank_operation=int(input("Por favor indique cual es la operación que desea realizar. 1. Depósito, 2. Retiro, 3. Ver mi Balance, 4. Salir del Sistema"))
            if my_bank_operation==1:
                my_saving_account.depositing_money(int(input("Por favor indique el Monto del Depósito: ")))
            elif my_bank_operation==2:
                my_saving_account.withdraw_money(int(input("Por favor indique el Monto del Retiro: ")))
                my_saving_account.min_balance()
            elif my_bank_operation==3:
                print(my_saving_account.balance)
            if my_bank_operation==4:
                my_boolean=False
            if my_bank_operation<1 or my_bank_operation>4:
                raise Exception
        except ValueError:
            print("No se pueden ingresar letras solo números")
        except Exception as ex:
            print(f'El número de instrucción tiene que estar entre 1 y 4, intente de nuevo por favor {ex}')
        

bank_operation()