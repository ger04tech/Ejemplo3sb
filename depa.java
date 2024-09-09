import java.util.ArrayList;
import java.util.Scanner;

public class depa {
    public static void main(String[] args) {
        ArrayList<String[]> ventasTotales = new ArrayList<>();
        ventasTotales.add(new String[]{"Mes", "Departamento", "Ventas"});
        ventasTotales.add(new String[]{"Agosto", "Ropa", "3000"});
        ventasTotales.add(new String[]{"Agosto", "Deportes", "1000"});
        ventasTotales.add(new String[]{"Agosto", "Jugueteria", "4000"});
        ventasTotales.add(new String[]{"Septiembre", "Ropa", "4000"});
        ventasTotales.add(new String[]{"Septiembre", "Deportes", "3000"});
        ventasTotales.add(new String[]{"Septiembre", "Jugueteria", "8000"});
        ventasTotales.add(new String[]{"Octubre", "Ropa", "2500"});
        ventasTotales.add(new String[]{"Octubre", "Deportes", "1500"});
        ventasTotales.add(new String[]{"Octubre", "Jugueteria", "4500"});
        ventasTotales.add(new String[]{"Noviembre", "Ropa", "3200"});
        ventasTotales.add(new String[]{"Noviembre", "Deportes", "1200"});
        ventasTotales.add(new String[]{"Noviembre", "Jugueteria", "1200"});
        ventasTotales.add(new String[]{"Diciembre", "Ropa", "5000"});
        ventasTotales.add(new String[]{"Diciembre", "Deportes", "2300"});
        ventasTotales.add(new String[]{"Diciembre", "Jugueteria", "2300"});
        ventasTotales.add(new String[]{"Enero", "Ropa", "4700"});
        ventasTotales.add(new String[]{"Enero", "Deportes", "2700"});
        ventasTotales.add(new String[]{"Enero", "Jugueteria", "6700"});
        ventasTotales.add(new String[]{"Febrero", "Ropa", "3400"});
        ventasTotales.add(new String[]{"Febrero", "Deportes", "1200"});
        ventasTotales.add(new String[]{"Febrero", "Jugueteria", "4400"});
        ventasTotales.add(new String[]{"Marzo", "Ropa", "2300"});
        ventasTotales.add(new String[]{"Marzo", "Deportes", "2100"});
        ventasTotales.add(new String[]{"Marzo", "Jugueteria", "2500"});
        ventasTotales.add(new String[]{"Abril", "Ropa", "4500"});
        ventasTotales.add(new String[]{"Abril", "Deportes", "4500"});
        ventasTotales.add(new String[]{"Abril", "Jugueteria", "2300"});
        ventasTotales.add(new String[]{"Mayo", "Ropa", "3670"});
        ventasTotales.add(new String[]{"Mayo", "Deportes", "7670"});
        ventasTotales.add(new String[]{"Mayo", "Jugueteria", "3670"});
        ventasTotales.add(new String[]{"Junio", "Ropa", "5300"});
        ventasTotales.add(new String[]{"Junio", "Deportes", "9300"});
        ventasTotales.add(new String[]{"Junio", "Jugueteria", "5600"});
        ventasTotales.add(new String[]{"Julio", "Ropa", "2000"});
        ventasTotales.add(new String[]{"Julio", "Deportes", "8000"});
        ventasTotales.add(new String[]{"Julio", "Jugueteria", "2300"});

        Scanner scanner = new Scanner(System.in);

        // Vaciar ventas de un departamento
        System.out.print("¿Qué departamento deseas vaciar? (Jugueteria, Ropa, Deportes): ");
        String departamentoAVaciar = scanner.nextLine();
        for (String[] registro : ventasTotales) {
            if (registro[1].equalsIgnoreCase(departamentoAVaciar) && !registro[0].equals("Mes")) {
                registro[2] = "0";
            }
        }

        // Mostrar ventas después de vaciar el departamento
        System.out.println("\nVentas después de vaciar el departamento:");
        for (String[] registro : ventasTotales) {
            System.out.printf("%-12s %-12s %-7s%n", registro[0], registro[1], registro[2]);
        }

        // Agregar datos
        System.out.print("\nIngresa el mes para el nuevo registro: ");
        String mesNuevo = scanner.nextLine();
        System.out.print("Ingresa el departamento para el nuevo registro (Jugueteria, Ropa, Deportes): ");
        String departamentoNuevo = scanner.nextLine();
        System.out.print("Ingresa las ventas para el nuevo registro: ");
        String ventasNuevas = scanner.nextLine();

        ventasTotales.add(new String[]{mesNuevo, departamentoNuevo, ventasNuevas});

        // Mostrar registros actualizados
        System.out.println("\nVentas actualizadas:");
        for (String[] registro : ventasTotales) {
            System.out.printf("%-12s %-12s %-7s%n", registro[0], registro[1], registro[2]);
        }

        scanner.close();
    }
}
