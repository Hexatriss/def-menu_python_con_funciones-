# Definimos nuestro stock inicial y un registro de compradores
stock_entradas = {
    'concierto_a': 50,  # 50 entradas disponibles para el concierto A
    'concierto_b': 30    # 30 entradas disponibles para el concierto B
}
compradores = {}  # Diccionario para guardar {nombre: tipo_entrada}

def comprar_entrada():
    """Función para manejar la compra de entradas"""
    print("\n--- COMPRAR ENTRADA ---")
    
    # Pedimos el nombre del comprador
    nombre = input("Ingrese su nombre: ").strip()
    
    # Verificamos si ya compró una entrada
    if nombre in compradores:
        print("Error: Ya has comprado una entrada anteriormente.")
        return
    
    # Mostramos opciones disponibles
    print("\nEventos disponibles:")
    print("1. Concierto A (50 entradas disponibles)")
    print("2. Concierto B (30 entradas disponibles)")
    
    # Solicitamos la elección
    opcion = input("Seleccione el evento (1 o 2): ").strip()
    
    # Validamos la opción
    if opcion not in ['1', '2']:
        print("Error: Opción no válida.")
        return
    
    # Determinamos el tipo de entrada
    tipo_entrada = 'concierto_a' if opcion == '1' else 'concierto_b'
    
    # Verificamos disponibilidad
    if stock_entradas[tipo_entrada] <= 0:
        print("Error: No hay entradas disponibles para este evento.")
        return
    
    # Actualizamos stock y registramos comprador
    stock_entradas[tipo_entrada] -= 1
    compradores[nombre] = tipo_entrada
    
    # Mostramos confirmación
    print(f"\n¡Entrada para {tipo_entrada} comprada con éxito!")
    print(f"Stock actual: Concierto A: {stock_entradas['concierto_a']}, Concierto B: {stock_entradas['concierto_b']}")

def cambiar_pedido():
    """Función para cambiar el tipo de entrada comprada"""
    print("\n--- CAMBIAR PEDIDO ---")
    
    # Pedimos el nombre del comprador
    nombre = input("Ingrese su nombre: ").strip()
    
    # Verificamos si existe
    if nombre not in compradores:
        print("Error: No encontramos tu registro de compra.")
        return
    
    # Obtenemos el evento actual
    evento_actual = compradores[nombre]
    
    # Determinamos el evento alternativo
    if evento_actual == 'concierto_a':
        nuevo_evento = 'concierto_b'
        print("Cambiando de Concierto A a Concierto B")
    else:
        nuevo_evento = 'concierto_a'
        print("Cambiando de Concierto B a Concierto A")
    
    # Verificamos disponibilidad en el nuevo evento
    if stock_entradas[nuevo_evento] <= 0:
        print("Error: No hay entradas disponibles para el nuevo evento.")
        return
    
    # Confirmamos el cambio
    confirmacion = input("¿Confirmar cambio? (S/N): ").strip().upper()
    if confirmacion != 'S':
        print("Cambio cancelado.")
        return
    
    # Actualizamos los registros
    stock_entradas[evento_actual] += 1  # Liberamos una entrada del evento original
    stock_entradas[nuevo_evento] -= 1   # Reservamos una entrada en el nuevo evento
    compradores[nombre] = nuevo_evento  # Actualizamos el registro
    
    print("\n¡Cambio realizado con éxito!")
    print(f"Ahora tienes entrada para: {nuevo_evento}")
    print(f"Stock actual: Concierto A: {stock_entradas['concierto_a']}, Concierto B: {stock_entradas['concierto_b']}")

def ver_stock():
    """Función para mostrar el stock disponible"""
    print("\n--- STOCK DISPONIBLE ---")
    print(f"Concierto A: {stock_entradas['concierto_a']} entradas disponibles")
    print(f"Concierto B: {stock_entradas['concierto_b']} entradas disponibles")
    print(f"Total de compradores registrados: {len(compradores)}")

def menu_principal():
    """Función que muestra el menú principal"""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Comprar una entrada")
        print("2. Cambiar pedido")
        print("3. Ver stock disponible")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            comprar_entrada()
        elif opcion == '2':
            cambiar_pedido()
        elif opcion == '3':
            ver_stock()
        elif opcion == '4':
            print("\nGracias por usar nuestro sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1-4.")

# Ejecutamos el programa
if __name__ == "__main__":
    menu_principal()