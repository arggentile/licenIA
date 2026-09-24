compra = input("¿ingrese el  monto de su compra: ")
compra = float(compra)

if compra < 5000:
    print("Usted no dispone de descuentos por el momento")
elif compra >= 500 and compra <= 10000:
    descuento = 0.10 #
    descuento_aplicado = compra * 0.10 #aplicamos el 10% de descuento        
    total = compra  - descuento_aplicado
    print("Usted tiene un descuento del 10%. Descuento aplicado: ", descuento_aplicado )
    print("El total a pagar es: ", total)
elif compra > 10000: #podriamos haber puesto solo el else
    descuento = 0.15 #
    descuento_aplicado = compra * 0.15 #aplicamos el 10% de descuento        
    total = compra  - descuento_aplicado
    print("Usted tiene un descuento del 15%. Descuento aplicado: ", descuento_aplicado )
    print("El total a pagar es: ", total) 
