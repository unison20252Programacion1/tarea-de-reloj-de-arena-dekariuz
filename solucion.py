# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    # Parte superior
    for i in range(m//2 + 1):
        if i==m//2 and 2==m/(m//2):
            break 
        print(" " * i + s * (m - 2*i))
     # Parte inferior
    for i in range(m//2 - 1, -1, -1):
        print(" " * i + s * (m - 2*i))
        
