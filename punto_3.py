class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, valor):
        self.items.append(valor)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0


def esta_balanceada(expresion):
    pila = Pila()
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in '([{':
            pila.apilar(caracter)
        elif caracter in ')]}':
            if pila.esta_vacia() or pila.desapilar() != pares[caracter]:
                return "No balanceada"
    return "Balanceada" if pila.esta_vacia() else "No balanceada"

while True:
    expresion = input("Ingrese una expresión (o 'salir' para terminar): ")
    if expresion.lower() == 'salir':
        break
    resultado = esta_balanceada(expresion)
    print(f"{expresion} => {resultado}")