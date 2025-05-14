class Nodo:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = None

def insertar_nodo(inicio, fila, columna, valor):
    if valor == 0:
        return inicio
    nuevo = Nodo(fila, columna, valor)
    if inicio is None:
        return nuevo
    actual = inicio
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nuevo
    return inicio

def lista_a_diccionario(cabeza):
    matriz = {}
    actual = cabeza
    while actual:
        matriz[(actual.fila, actual.columna)] = actual.valor
        actual = actual.siguiente
    return matriz

def diccionario_a_lista(diccionario):
    cabeza = None
    for (i, j), v in sorted(diccionario.items()):
        cabeza = insertar_nodo(cabeza, i, j, v)
    return cabeza

def imprimir_lista(cabeza):
    actual = cabeza
    while actual:
        print(f"({actual.fila}, {actual.columna}, {actual.valor}) -> ", end="")
        actual = actual.siguiente
    print("NULL")

def potencia_matriz_dispersa(lista, n, m):
    A = lista_a_diccionario(lista)
    resultado = {}
    for (i, j), valor in A.items():
        resultado[(i, j)] = valor ** n
    return diccionario_a_lista(resultado)

print("🧮 Bienvenido. Vamos a construir una matriz dispersa cuadrada.")

while True:  # Validate input for m
    try:
        m = int(input("🔢 Ingrese el tamaño m de la matriz cuadrada (m x m): "))
        if m < 1:
            print("Por favor, ingrese un valor válido (m ≥ 1): ")
        else:
            break  # Exit the loop if m is valid
    except ValueError:
        print("⚠️ Entrada inválida. Ingrese un entero para el tamaño de la matriz.")


print("\n🧾 Ingrese los elementos de la matriz.")
print("Para cada elemento, ingrese: fila columna valor")

cabeza = None
for i in range(m):
    for j in range(m):
        while True:  # Loop until valid input is given for each element
            entrada = input(f"Elemento [{i}][{j}]: ").strip()
            try:
                valor = int(entrada)
                break  # Exit the inner loop if input is valid
            except ValueError:
                print("⚠️ Entrada inválida. Ingrese solo el valor (entero).")
        if valor != 0:  # Insert only if the value is not zero
            cabeza = insertar_nodo(cabeza, i, j, valor)

# Mostrar lista enlazada original
print("\n📥 Lista enlazada ORIGINAL:")
imprimir_lista(cabeza)

# Solicitar n
n = int(input("\n🔁 Ingrese la potencia n (n ≥ 1): "))
while n < 1:
    n = int(input("Por favor, ingrese un valor válido (n ≥ 1): "))

# Calcular potencia
resultado = potencia_matriz_dispersa(cabeza, n, m)

# Mostrar resultado
print(f"\n📤 Lista enlazada RESULTADO para A^{n}:")
imprimir_lista(resultado)