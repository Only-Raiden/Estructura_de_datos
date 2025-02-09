# Estructura_de_datos
Repositorio de la Materia de Estructura de Datos 
Explicacion codigo python 
Este código permite gestionar un registro de ventas mensuales en tres categorías: ropa, deportes y juguetería. Funciona a través de un menú interactivo donde el usuario puede ingresar, buscar y eliminar datos.

El programa inicia con listas vacías para almacenar los datos. La función ingresar_datos() permite al usuario registrar ventas por mes, asegurándose de que los valores ingresados sean numéricos. La función buscar_elemento() permite consultar las ventas de un mes específico. La función eliminar_venta() permite eliminar las ventas de un mes ingresado.

El menú principal, gestionado por mostrar_menu(), ofrece cuatro opciones: ingresar datos, buscar ventas, eliminar ventas o salir del programa. El menú se repite hasta que el usuario elige la opción de salida. Un detalle a mejorar es que, actualmente, al ingresar nuevos datos se sobrescriben las listas en lugar de actualizarse.

Explacacion codigo java 
El programa en Java VentasMensuales permite gestionar registros de ventas mensuales en tres categorías: ropa, deportes y juguetería. Utiliza ArrayList para almacenar los meses y las ventas de cada categoría, y Scanner para la entrada de datos del usuario.

El programa inicia llamando a mostrarMenu(), que presenta un menú interactivo con las opciones:

Ingresar datos de ventas
Buscar ventas por mes
Eliminar ventas de un mes
Salir
Si el usuario elige ingresar datos, ingresarDatos() solicita el nombre del mes y las ventas de cada categoría, validando que sean números mediante validarEntrada(), y luego almacena los valores en las listas correspondientes.

Para buscar información, buscarElemento() permite ingresar un mes y muestra las ventas si existe en la lista. Si el mes no se encuentra, muestra un mensaje de error.

Si el usuario desea eliminar registros, eliminarVenta() busca el mes ingresado y elimina los datos asociados de todas las listas.

El programa continúa ejecutando el menú hasta que el usuario elige la opción "Salir".
