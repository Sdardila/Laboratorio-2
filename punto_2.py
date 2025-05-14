class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def crear_lista_doble_enlazada(elementos):
    if not elementos:
        return None
    head = Nodo(elementos[0])
    current = head
    for i in range(1, len(elementos)):
        nuevo_nodo = Nodo(elementos[i])
        current.next = nuevo_nodo
        nuevo_nodo.prev = current
        current = nuevo_nodo
    return head

def crear_lista_circular_doble_enlazada(elementos):
    if not elementos:
        return None
    head = Nodo(elementos[0])
    current = head
    for i in range(1, len(elementos)):
        nuevo_nodo = Nodo(elementos[i])
        current.next = nuevo_nodo
        nuevo_nodo.prev = current
        current = nuevo_nodo
    current.next = head
    head.prev = current
    return head

def imprimir_lista_doble(head):
    elementos = []
    current = head
    while current:
        elementos.append(current.data)
        current = current.next
    print("Lista doblemente enlazada:", elementos)

def imprimir_lista_circular_doble(head):
    if not head:
        print("Lista circular doblemente enlazada: []")
        return
    elementos = []
    current = head
    original_head = head # Guardar la cabeza original para la condición de parada
    if head:
        while True:
            elementos.append(current.data)
            current = current.next
            if current == original_head:
                break
    print("Lista circular doblemente enlazada:", elementos)

def eliminar_nodo_doble(head, nodo_a_eliminar):
    if not head or not nodo_a_eliminar:
        return head
    if nodo_a_eliminar.prev:
        nodo_a_eliminar.prev.next = nodo_a_eliminar.next
    else:
        head = nodo_a_eliminar.next
        if head:
            head.prev = None
    if nodo_a_eliminar.next:
        nodo_a_eliminar.next.prev = nodo_a_eliminar.prev
    return head

def eliminar_nodo_circular_doble(head, nodo_a_eliminar):
    if not head or not nodo_a_eliminar:
        return head
    if head.next == head:  # Solo un nodo en la lista
        return None
    if nodo_a_eliminar == head:
        head = head.next
    nodo_a_eliminar.prev.next = nodo_a_eliminar.next
    nodo_a_eliminar.next.prev = nodo_a_eliminar.prev
    return head

def insertar_ordenado_doble(head, nuevo_nodo):
    if not head:
        return nuevo_nodo
    if nuevo_nodo.data <= head.data:
        nuevo_nodo.next = head
        head.prev = nuevo_nodo
        return nuevo_nodo
    current = head
    while current.next and current.next.data < nuevo_nodo.data:
        current = current.next
    nuevo_nodo.next = current.next
    if current.next:
        current.next.prev = nuevo_nodo
    current.next = nuevo_nodo
    nuevo_nodo.prev = current
    return head

def destruir_lista_circular_doble(head):
    if not head:
        return None
    current = head.next
    original_head = head # Guardar la cabeza original para la condición de parada
    while current != original_head:
        temp = current
        current = current.next
        del temp
    del head
    return None

def obtener_elementos_usuario():
    while True:
        entrada = input("Ingrese los elementos separados por comas (ej: 1,2,3) o deje vacío para terminar: ")
        if not entrada.strip():
            return []
        elementos_str = entrada.split(',')
        elementos = []
        valido = True
        for elem in elementos_str:
            try:
                elementos.append(int(elem.strip()))
            except ValueError:
                print("Por favor, ingrese solo números enteros separados por comas.")
                valido = False
                break
        if valido:
            return elementos

def procesar_listas_con_seguimiento(ptr1_head, ptr2_head):
    print("\n--- Proceso ---")

    print("\n1. Estado inicial:")
    print("   PTR1:", end=" ")
    imprimir_lista_doble(ptr1_head)
    print("   PTR2:", end=" ")
    imprimir_lista_circular_doble(ptr2_head)

    elementos_ptr2 = []
    current_ptr2 = ptr2_head
    nodos_ptr2_procesados = set()

    if current_ptr2:
        original_head_ptr2 = ptr2_head # Guardar la cabeza original para la condición de parada
        while current_ptr2 and current_ptr2 not in nodos_ptr2_procesados:
            elementos_ptr2.append(current_ptr2.data)
            nodos_ptr2_procesados.add(current_ptr2)
            current_ptr2 = current_ptr2.next
            if current_ptr2 == original_head_ptr2:
                break

    # Añadir a PTR1 los elementos de PTR2 que no están en PTR1
    elementos_añadidos = []
    for elemento in elementos_ptr2:
        encontrado_en_ptr1 = False
        current_ptr1 = ptr1_head
        while current_ptr1:
            if elemento == current_ptr1.data:
                encontrado_en_ptr1 = True
                break
            current_ptr1 = current_ptr1.next
        if not encontrado_en_ptr1:
            nuevo_nodo = Nodo(elemento)
            ptr1_head = insertar_ordenado_doble(ptr1_head, nuevo_nodo)
            elementos_añadidos.append(elemento)

    print("\n2. Después de añadir a PTR1 los elementos de PTR2 no presentes:")
    print("   Elementos añadidos a PTR1:", elementos_añadidos)
    print("   PTR1:", end=" ")
    imprimir_lista_doble(ptr1_head)
    print("   PTR2:", end=" ")
    imprimir_lista_circular_doble(ptr2_head)

    # Eliminar elementos comunes de PTR1 y PTR2
    elementos_eliminados = []
    current_ptr2 = ptr2_head
    if current_ptr2:
        original_head_ptr2 = ptr2_head # Guardar la cabeza original para la condición de parada
        nodos_ptr2_procesados = set()
        while current_ptr2 and current_ptr2 not in nodos_ptr2_procesados:
            nodos_ptr2_procesados.add(current_ptr2)
            current_ptr1 = ptr1_head
            elemento_actual_ptr2 = current_ptr2.data
            next_ptr2 = current_ptr2.next # Guardar el siguiente nodo antes de potencialmente eliminar current_ptr2

            while current_ptr1:
                if elemento_actual_ptr2 == current_ptr1.data:
                    ptr1_head = eliminar_nodo_doble(ptr1_head, current_ptr1)
                    ptr2_head = eliminar_nodo_circular_doble(ptr2_head, current_ptr2)
                    elementos_eliminados.append(elemento_actual_ptr2)
                    break
                current_ptr1 = current_ptr1.next

            if not ptr2_head:
                break
            elif current_ptr2 == next_ptr2: # Si solo queda un nodo o dos y se eliminó uno
                if elemento_actual_ptr2 not in elementos_eliminados: # Agregar esta condición
                    elementos_eliminados.append(elemento_actual_ptr2)
                break
            current_ptr2 = next_ptr2 # Usar el nodo guardado para continuar la iteración
            if current_ptr2 == original_head_ptr2:
                break


    print("\n3. Después de eliminar los elementos comunes:")
    print("   Elementos comunes eliminados:", elementos_eliminados)
    print("   PTR1:", end=" ")
    imprimir_lista_doble(ptr1_head)
    print("   PTR2:", end=" ")
    if ptr2_head:
        imprimir_lista_circular_doble(ptr2_head)
    else:
        print("[]")

    # Eliminar la lista PTR2
    destruir_lista_circular_doble(ptr2_head)
    ptr2_destruido = None

    print("\n4. Después de destruir PTR2:")
    print("   PTR1:", end=" ")
    imprimir_lista_doble(ptr1_head)
    print("   PTR2 (destruido):", ptr2_destruido)

    return ptr1_head, ptr2_destruido

if __name__ == "__main__":
    print("Ingrese los elementos para la lista doblemente enlazada (PTR1), separados por comas y en orden ascendente:")
    elementos_ptr1 = obtener_elementos_usuario()
    lista1 = crear_lista_doble_enlazada(elementos_ptr1)

    print("\nIngrese los elementos para la lista circular doblemente enlazada (PTR2), separados por comas:")
    elementos_ptr2 = obtener_elementos_usuario()
    lista2 = crear_lista_circular_doble_enlazada(elementos_ptr2)

    procesar_listas_con_seguimiento(lista1, lista2)