class BankAccount():
    def __init__(self,balance):
        self.balance=balance


    def depositing_money(self,deposit):
        self.deposit=deposit
        self.balance=self.balance+self.deposit
        return (self.balance)


    def withdraw_money(self,withdraw):
        self.withdraw=withdraw
    
class SavingsAccount(BankAccount):
    def __init__(self,balance,minbalance):
        BankAccount.__init__(self,balance)
        self.minbalance=minbalance

        
    def min_balance(self):
        if (self.balance-self.withdraw)<=self.minbalance:
            print("Operación No se puede realizar, Balance Insuficiente")
        else:
            self.balance=self.balance-self.withdraw
            return self.balance


def bank_operation():
    my_boolean=True
    try:
        my_balance=int(input("Indique Por Favor el monto de su balance: "))
        my_minbalance=int(input("Por favor indique cual es el balance Mínimo: "))
        if my_balance<0 or my_minbalance<0:
            raise NegativeValues
        else:
            my_saving_account=SavingsAccount(my_balance,my_minbalance)

    
        while (my_boolean==True):        
            try:
                my_bank_operation=int(input("Por favor indique cual es la operación que desea realizar. 1. Depósito, 2. Retiro, 3. Ver mi Balance, 4. Salir del Sistema"))
                if my_bank_operation==1:
                    try:
                        deposit_value=int(input("Por favor indique el Monto del Depósito: "))
                        if deposit_value<0:
                            raise negativevalue
                        else:
                            print(my_saving_account.depositing_money(deposit_value))
                    except ValueError:
                        print("El monto del deposito no pueden ser letras")
                    except Exception as negativevalue:
                        print("El monto del deposito no puede ser negativo")
                elif my_bank_operation==2:
                    try:
                        withdraw_value=int(input("Por favor indique el Monto del Retiro: "))
                        if withdraw_value<0:
                            raise negativewithdrawvalue
                        else:
                            my_saving_account.withdraw_money(withdraw_value)
                            print(my_saving_account.min_balance())
                    except ValueError:
                        print("El monto del retiro no puede tener letras")
                    except Exception as negativewithdrawvalue:
                        print("El monto del retiro no puede ser negativo")
                elif my_bank_operation==3:
                    print(my_saving_account.balance)
                if my_bank_operation==4:
                    my_boolean=False
                if my_bank_operation<1 or my_bank_operation>4:
                    raise InvalidNumberException
            except ValueError:
                print ("No se permiten letras en el Menu")
            except Exception as InvalidNumberException:
                print("Solo se permiten numeros entre 1 y 4 en el Menu")
    except ValueError:
        print("No se pueden ingresar letras solo números")
    except Exception as NegativeValues:
        print("El balance o el balance minimo no pueden tener valores negativos")


bank_operation()