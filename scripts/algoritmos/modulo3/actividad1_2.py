class Cuenta:
    def __init__(self, apellido, nombre, nrocuenta, saldo = 0):
        self.apellido = apellido
        self.nombre = nombre
        self.nrocuenta = nrocuenta
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            print("Monto negativo")

    def retirar(self, monto):
        if(monto<0):
            print("monto negativo, debe ser positivo")
            return
        if(self.saldo < monto):
            print("Monto menor a lo que se quiere retirar")
            return

        self.saldo -= monto
        
    def info(self):
        print(f"Cuenta nro {self.nrocuenta} cliente es: {self.apellido}{self.nombre} saldo es: {self.saldo}")

        
cuenta1 = Cuenta("El señor de los anillos 1", "juanito peres", 2000)
cuenta2 = Cuenta("El señor de los anillos 2", "H cabral", 2002)
cuenta3 = Cuenta("El señor de los anillos 3", "lucho Olivera", 2000)

cuenta1.info()
cuenta2.info()
cuenta3.info()

cuenta1.depositar(1000)
cuenta1.info()
cuenta1.retirar(500)
cuenta1.info()
cuenta1.retirar(300)
cuenta1.info()
cuenta1.retirar(400)

cuenta1.info()
    
        
        