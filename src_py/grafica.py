import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [2,4,6,8,10]

# crear un grafico de lineas
plt.plot(x,y,label="Linea ", color= "blue")

# Agegar parametros 
plt.title("Grafico de Linea")
plt.xlabel("Eje de la X")
plt.xlabel("Eje de la Y")

#Agregar leyenda
plt.legend()

#Mostrar el grafico
plt.show()



