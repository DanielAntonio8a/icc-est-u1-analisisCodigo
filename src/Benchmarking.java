import java.util.Random;
public class Benchmarking {
    private MetodosOrdenamiento mOrdenamiento;
    public Benchmarking(){
        long currentMillis = System.currentTimeMillis();
        long currentNano=System.nanoTime();
        System.out.println(currentMillis);
        System.out.println(currentNano);
        mOrdenamiento=new MetodosOrdenamiento();

        int [] arreglo=generarArregloAleatorio(1000000);
        
        Runnable tarea=()-> mOrdenamiento.burbujaTradicional(arreglo);
        double TiempoDuracionMilis=medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNano=medirConNanoTime(tarea);
        System.out.println("tiempo en milisegundo: " + TiempoDuracionMilis);
        System.out.println("Tiempo Duracion " + tiempoDuracionNano);
    }
    public int[] generarArregloAleatorio(int tamano){
        int[] array=new int[tamano];
        Random random=new Random();

        for (int i = 0; i < tamano; i++) {
            array[i]=random.nextInt(1000000);
        }
        return array;
    }
    public double medirConCurrentTimeMiles(Runnable tarea){
        long inicio= System.currentTimeMillis();
        tarea.run();
        long fin =System.currentTimeMillis();
        double timpoSegundos = (fin-inicio)/1000.0;
        return timpoSegundos;
    }
    public double medirConNanoTime(Runnable tarea){
        long inicio=System.nanoTime();
        tarea.run();
        long fin=System.nanoTime();
        return (fin-inicio)/1_000_000_000.0;
    }
}
