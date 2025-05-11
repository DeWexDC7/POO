'''
Sistema Básico de Inventario con POO
Autor: Daniel Chavez
Escuela de Posgrado de Newman
'''

class Producto:
    """
    Clase para representar un producto en el inventario.
    """
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto.
        
        Parámetros:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad disponible del producto.
            
        Raises:
            ValueError: Si el nombre está vacío, el precio es negativo o la cantidad es negativa.
            TypeError: Si el tipo de datos no es el correcto.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
            
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = cantidad
        
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.
        
        Parámetros:
            nuevo_precio (float): Nuevo precio del producto.
            
        Raises:
            ValueError: Si el precio es negativo.
            TypeError: Si el tipo de dato no es el correcto.
        """
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número")
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
            
        self.precio = float(nuevo_precio)
        return True
        
    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto.
        
        Parámetros:
            nueva_cantidad (int): Nueva cantidad del producto.
            
        Raises:
            ValueError: Si la cantidad es negativa.
            TypeError: Si el tipo de dato no es el correcto.
        """
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un número entero")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        self.cantidad = nueva_cantidad
        return True
        
    def calcular_valor_total(self):
        """
        Calcula el valor total del producto (precio × cantidad).
        
        Returns:
            float: Valor total del producto.
        """
        return self.precio * self.cantidad
        
    def __str__(self):
        """
        Devuelve una representación en cadena del producto.
        
        Returns:
            str: Representación del producto.
        """
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}, Valor Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    """
    Clase para gestionar una colección de productos.
    """
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar productos.
        """
        self.productos = []
        
    def agregar_producto(self, producto):
        """
        Añade un producto al inventario.
        
        Parámetros:
            producto (Producto): Producto a añadir.
            
        Raises:
            TypeError: Si el objeto no es una instancia de la clase Producto.
        """
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto")
            
        # Verificar si el producto ya existe (por nombre)
        producto_existente = self.buscar_producto(producto.nombre)
        if producto_existente:
            # Si ya existe, solo actualizamos la cantidad
            producto_existente.actualizar_cantidad(producto_existente.cantidad + producto.cantidad)
            return False
        else:
            # Si no existe, lo añadimos a la lista
            self.productos.append(producto)
            return True
        
    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre.
        
        Parámetros:
            nombre (str): Nombre del producto a buscar.
            
        Returns:
            Producto o None: El producto encontrado o None si no existe.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")
            
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
        
    def calcular_valor_inventario(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Valor total del inventario.
        """
        valor_total = 0
        for producto in self.productos:
            valor_total += producto.calcular_valor_total()
        return valor_total
        
    def listar_productos(self):
        """
        Muestra todos los productos del inventario.
        
        Returns:
            list: Lista de productos.
        """
        return self.productos


def mostrar_menu():
    """
    Muestra el menú de opciones disponibles.
    """
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar precio de un producto")
    print("4. Actualizar cantidad de un producto")
    print("5. Mostrar todos los productos")
    print("6. Calcular valor total del inventario")
    print("0. Salir")
    print("================================")


def menu_principal():
    """
    Función principal que gestiona el menú interactivo.
    """
    inventario = Inventario()
    
    # Agregar algunos productos de ejemplo
    try:
        inventario.agregar_producto(Producto("Laptop", 1200.50, 5))
        inventario.agregar_producto(Producto("Mouse", 25.99, 10))
        inventario.agregar_producto(Producto("Teclado", 45.75, 8))
        print("Se han agregado productos de ejemplo al inventario.")
    except (ValueError, TypeError) as e:
        print(f"Error al agregar productos de ejemplo: {e}")
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 0:
                print("¡Gracias por usar el Sistema de Inventario!")
                break
                
            elif opcion == 1:
                # Agregar producto
                try:
                    nombre = input("Nombre del producto: ")
                    precio = float(input("Precio del producto: "))
                    cantidad = int(input("Cantidad del producto: "))
                    
                    nuevo_producto = Producto(nombre, precio, cantidad)
                    if inventario.agregar_producto(nuevo_producto):
                        print(f"Producto '{nombre}' agregado correctamente.")
                    else:
                        print(f"El producto '{nombre}' ya existía. Se ha actualizado la cantidad.")
                except (ValueError, TypeError) as e:
                    print(f"Error al agregar el producto: {e}")
                    
            elif opcion == 2:
                # Buscar producto
                try:
                    nombre_buscar = input("Nombre del producto a buscar: ")
                    producto = inventario.buscar_producto(nombre_buscar)
                    if producto:
                        print("\nProducto encontrado:")
                        print(producto)
                    else:
                        print(f"No se encontró ningún producto con el nombre '{nombre_buscar}'")
                except TypeError as e:
                    print(f"Error: {e}")
                    
            elif opcion == 3:
                # Actualizar precio
                try:
                    nombre_producto = input("Nombre del producto a actualizar: ")
                    producto = inventario.buscar_producto(nombre_producto)
                    if producto:
                        nuevo_precio = float(input("Nuevo precio: "))
                        producto.actualizar_precio(nuevo_precio)
                        print(f"Precio del producto '{nombre_producto}' actualizado correctamente.")
                    else:
                        print(f"No se encontró ningún producto con el nombre '{nombre_producto}'")
                except (ValueError, TypeError) as e:
                    print(f"Error al actualizar el precio: {e}")
                    
            elif opcion == 4:
                # Actualizar cantidad
                try:
                    nombre_producto = input("Nombre del producto a actualizar: ")
                    producto = inventario.buscar_producto(nombre_producto)
                    if producto:
                        nueva_cantidad = int(input("Nueva cantidad: "))
                        producto.actualizar_cantidad(nueva_cantidad)
                        print(f"Cantidad del producto '{nombre_producto}' actualizada correctamente.")
                    else:
                        print(f"No se encontró ningún producto con el nombre '{nombre_producto}'")
                except (ValueError, TypeError) as e:
                    print(f"Error al actualizar la cantidad: {e}")
                    
            elif opcion == 5:
                # Mostrar todos los productos
                productos = inventario.listar_productos()
                if productos:
                    print("\n===== LISTA DE PRODUCTOS =====")
                    for producto in productos:
                        print(producto)
                    print("=============================")
                else:
                    print("El inventario está vacío.")
                    
            elif opcion == 6:
                # Calcular valor total del inventario
                valor_total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${valor_total:.2f}")
                
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                
        except ValueError:
            print("Error: Debe ingresar un número.")
        
        # Pausa para que el usuario pueda leer el resultado
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    try:
        menu_principal()
    except Exception as e:
        print(f"Error inesperado: {e}")
        print("El programa ha finalizado debido a un error.")
