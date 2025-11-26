# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    # Parte superior
    for i in range(n):
        print(" " * i + s * (2*(n-i)-1))
    
    # Parte inferior
    for i in range(1, n):
        print(" " * (n-i-1) + s * (2*i+1))
    pass
