from collections import Counter

# Inventario actual en la tienda
stock_actual = Counter({'camisas': 20, 'pantalones': 15, 'zapatos': 8})

# Llega un nuevo pedido de mercadería (un diccionario común)
nuevo_pedido = {'camisas': 10, 'zapatos': 5, 'gorras': 12}

# Sumamos el nuevo pedido al stock actual directamente usando .update()
stock_actual.update(nuevo_pedido)

print(stock_actual)
# Resultado automático (suma las claves repetidas y agrega las nuevas):
# Counter({'camisas': 30, 'pantalones': 15, 'zapatos': 13, 'gorras': 12})

# Consultar un elemento que NO existe no da error, devuelve 0
print(stock_actual['medias']) 
# Resultado: 0