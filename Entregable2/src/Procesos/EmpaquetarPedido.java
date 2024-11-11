package Procesos;

import java.util.Random;
import java.util.concurrent.Callable;

public class EmpaquetarPedido implements Callable<Boolean> {
    private final Paquete paquete;
    private final int Tmin;
    private final int Tmax;

    public EmpaquetarPedido(Paquete paquete, int t_min, int t_max) {
        this.paquete = paquete;
        this.Tmin = t_min;
        this.Tmax = t_max;
    }

    @Override
    public Boolean call() throws Exception {
        if (!paquete.isPagoValidado()){
            System.out.println("El pago no fue validado, no se puede empaquetar el pedido");
            return false;
        }

        Thread.sleep(new Random().nextInt(Tmin, Tmax));
        System.out.println("Pedido empaquetado y listo para envío con ID: " + paquete.getEtiquetaID());
        return true;
    }
}
