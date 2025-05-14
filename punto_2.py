class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.sig = None

# Insertar manteniendo el orden
def insertar_ordenado(cabeza, valor):
    nuevo = NodoDoble(valor)
    if not cabeza or valor < cabeza.valor:
        nuevo.sig = cabeza
        if cabeza:
            cabeza.ant = nuevo
        return nuevo
    actual = cabeza
    while actual.sig and actual.sig.valor < valor:
        actual = actual.sig
    if actual.valor == valor:
        return cabeza  # No insertar repetido
    nuevo.sig = actual.sig
    if actual.sig:
        actual.sig.ant = nuevo
    actual.sig = nuevo
    nuevo.ant = actual
    return cabeza

# Fusiona PTR2 en PTR1 y elimina PTR2
def fusionar_listas(PTR1, PTR2):
    actual = PTR2
    while actual:
        if not existe(PTR1, actual.valor):
            PTR1 = insertar_ordenado(PTR1, actual.valor)
        actual = actual.sig
    PTR2 = None
    return PTR1

# Verifica si un valor ya está en PTR1
def existe(cabeza, valor):
    actual = cabeza
    while actual:
        if actual.valor == valor:
            return True
        actual = actual.sig
    return False

# Imprimir lista doble
def imprimir_lista_doble(cabeza):
    while cabeza:
        print(cabeza.valor, end=" <-> ")
        cabeza = cabeza.sig
    print("NULL")

# Ejemplo
PTR1 = NodoDoble(1)
PTR1.sig = NodoDoble(3)
PTR1.sig.ant = PTR1
PTR1.sig.sig = NodoDoble(5)
PTR1.sig.sig.ant = PTR1.sig

PTR2 = NodoDoble(2)
PTR2.sig = NodoDoble(3)
PTR2.sig.ant = PTR2
PTR2.sig.sig = NodoDoble(6)
PTR2.sig.sig.ant = PTR2.sig

print("Antes:")
imprimir_lista_doble(PTR1)

PTR1 = fusionar_listas(PTR1, PTR2)

print("Después:")
imprimir_lista_doble(PTR1)
