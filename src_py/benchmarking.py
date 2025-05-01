import MetodosOrdenamiento as mO

class Benchmarking:
    def __init__(self):
        print("Benchmarking instanciado...")
        self.mO = mO.MetodosOrdenamiento()  # Asegúrate de instanciar correctamente la clase si es necesario
        arreglo = self.build_arreglo(10000)  # Crear un arreglo de 10000 elementos
        print("\nLlamando al método de ordenamiento burbuja...")
        tarea = lambda: self.mO.ordenamiento_burbuja(arreglo)  # Definir la tarea a medir
        tiempoM = self.contar_con_current_time(tarea)  # Contar el tiempo de ejecución
        tiempoN = self.contar_con_current_Nanotime(tarea)  # Contar el tiempo de ejecución
        print(f"Tiempo de ejecución: {tiempoM} Mili segundos")
        print(f"Tiempo de ejecución: {tiempoN} Nano segundos")

        # Llamar al método de ordenamiento burbuja optimizado
        print("\nLlamando al método de ordenamiento burbuja optimizado...")
        tarea1 = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo)  # Definir la tarea a medir
        tiempoN1 = self.contar_con_current_Nanotime(tarea1)  # Contar el tiempo de ejecución
        print(f"\tTiempo de ejecución: {tiempoN1} Nano segundos")

        # Llamar al método de ordenamiento por selección
        print("\nLlamando al método de ordenamiento por selección...")
        tarea2 = lambda: self.mO.ordenamiento_seleccion(arreglo)  # Definir la tarea a medir
        tiempoN2 = self.contar_con_current_Nanotime(tarea2)  # Contar el tiempo de ejecución
        print(f"\tTiempo de ejecución: {tiempoN2} Nano segundos")
        
        # Llamar al método de ordenamiento shell
        print("\nLlamando al método de ordenamiento por shell...")
        tarea3 = lambda: self.mO.ordenamiento_shell(arreglo)  # Definir la tarea a medir
        tiempoN3 = self.contar_con_current_Nanotime(tarea3)  # Contar el tiempo de ejecución
        print(f"\tTiempo de ejecución: {tiempoN3} Nano segundos")




    def build_arreglo(self, n):
        # Crear un arreglo de tamaño n con números aleatorios
        import random
        arreglo = []
        for _ in range(n):  # Cambié 'tamaño' por 'n'
            numero = random.randint(1, 9999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time(self, tarea):
        import time
        # Contar el tiempo de ejecución de una tarea en segundos
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)

    def contar_con_current_Nanotime(self, tarea):
        import time
        # Contar el tiempo de ejecución de una tarea en nanosegundos
        inicio = time.time_ns()  # usa time_ns() para obtener tiempo en nanosegundos
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000  # Convertir nanosegundos a segundos
