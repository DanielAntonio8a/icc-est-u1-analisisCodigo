import benchmarking as bm
import MetodosOrdenamiento as mo
import benchmarking as bm
import matplotlib.pyplot as plt

# Obtener hora actual con segundos y tu nombre
nombre = "Daniel Duran"
hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Archivo principal o main
if __name__=="__main__":
    print("Hola Mundo")
    brench=bm.Benchmarking()
    metodos=mo.MetodosOrdenamiento()

    #tam=10000
    tamanios=[50, 100, 1000]
    resultados=[]

    for tam in tamanios:
        arreglo_base=brench.build_arreglo(tam)

        metodos_dic={
            "Burbuja": metodos.ordenamiento_burbuja,
            "Burbuja Mejorado": metodos.sort_burbuja_mejorado_optimizado,
            "Seleccion": metodos.ordenamiento_seleccion,
            "Insercion": metodos.sort_Insercion,
            "Shell": metodos.ordenamiento_shell,
        }
        for nombre, metodo in metodos_dic.items():
            #print(f"Ejecutando {nombre}...")
            tiempo_resultado = brench.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (tam,nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    for tam,nombre,tiempo in resultados:
        print(f"Tamano: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    #Prepara datos para ser graficos
    #1 Crear un diccionario o map para almacenar los resultados por metodos
    tiempos_by_metodo = {
        "Burbuja": [],
        "Burbuja Mejorado": [],
        "Seleccion": [],
        "Insercion": [],
        "Shell": [],
    }
    for tam,nombre,tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(10, 6))

    #Graficar los tiempos de ejecucion para cada metodo
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')
        
    # Título con nombre y hora
    titulo = f"Tiempos de Ejecución - {nombre} - {hora_actual}"
    plt.title(titulo)

    #Agregar parametros
    plt.title('Tiempos de Ejecucion de Metodos de Ordenamiento')
    plt.xlabel('Tamanio del Arreglo')
    plt.ylabel('Tiempo (segundos)')

    #Agregar leyenda
    plt.legend()
    
    # Cambiar el título de la ventana (si el entorno lo permite)
    plt.gcf().canvas.manager.set_window_title(titulo)

    #Mostrar el grafico
    plt.show()
    
    
    
    
    
    
    from datetime import datetime

# Obtener hora actual con segundos
hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mostrar en consola
print("Hora actual:", hora_actual)
