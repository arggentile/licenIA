class Cuenta:
    def __init__(self, nro_cuenta, cliente):
        self.nro_cuenta = nro_cuenta
        self.cliente = cliente
        self.saldo = 0

    def deposito(self, dinero_deposito):
        self.saldo += dinero_deposito

    def retirar(self, cantidad_retirar):
        if(cantidad_retirar<=self.saldo):
            self.saldo -= cantidad_retirar
        else:
            print("Dindeo no dispone de la cantidad necesaria")
            return

    def transferir(self, cantidad_transferir, cuenta_destino):
            if(cantidad_transferir<=self.saldo):
                self.saldo -= cantidad_transferir
            else: # aca deberiamos obtener la uinstancia de la cuenta destino, no se implementa
                print("Dindeo no dispone de la cantidad necesaria")
                return
    
    def mostrar_info(self):
        print(f"Datos de la cuenta son: numero: {self.nro_cuenta}, saldo: {self.saldo} cliente: {self.cliente}")


cuentaJuan = Cuenta(1001, "juan Esteban")
cuentaMariana   = Cuenta(1001, "Mariana")
cuentaJuan.mostrar_info();
cuentaJuan.deposito(1000)
cuentaJuan.deposito(500)
cuentaJuan.mostrar_info()
cuentaJuan.retirar(1000)
cuentaJuan.mostrar_info()
cuentaJuan.retirar(1000)
cuentaJuan.mostrar_info()


