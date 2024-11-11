package Procesos;

import java.util.Random;
import java.util.concurrent.Callable;

public class ProcesarPago implements Callable<Boolean> {
    private final Paquete paquete;
    private final int Tmin;
    private final int Tmax;

    public ProcesarPago(Paquete paquete, int t_min, int t_max) {
        this.paquete = paquete;
        this.Tmin = t_min;
        this.Tmax = t_max;
    }

    @Override
    public Boolean call() throws Exception {

        Thread.sleep(new Random().nextInt(Tmin, Tmax));
        boolean verificador = validarPago();

        if (verificador) {
            System.out.println("Pago aprobado para el paquete con etiqueta ID: " + paquete.getEtiquetaID());
            paquete.setPagoValidado(true);
        } else {
            System.out.println("Pago rechazado para el paquete con etiqueta ID: " + paquete.getEtiquetaID());
        }

        return verificador;
    }

    private boolean validarPago(){
        Random random = new Random();
        return random.nextInt(100) < 80;
    }
}
