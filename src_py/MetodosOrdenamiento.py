#Cree una clase MetodosOrdenamiento con metodos de ordenamiento
#Crear un metodo de ordenamiento por burbuja reciba una arreglo y la ordene de menor a mayor

class MetodosOrdenamiento:
    def ordenamiento_burbuja(self, arreglo):
        arreglo=arreglo.copy()  # Hacer una copia del arreglo original
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo

    def sort_burbuja_mejorado_optimizado(self,array):
       arreglo=array.copy()  
       # Ordenamiento burbuja optimizado
       n = len(arreglo)
       for i in range(n):
           intercambiado = False 
           for j in range(0, n-i-1):
               if arreglo[j] > arreglo[j+1]:
                   arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                   intercambiado = True 
           if not intercambiado:
               break  
       return arreglo


    def ordenamiento_seleccion(self, arreglo):
        # Ordenamiento por selección
        arreglo=arreglo.copy()  
        n = len(arreglo)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo