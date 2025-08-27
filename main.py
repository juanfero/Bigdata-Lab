def es_par(numero: int) -> bool:
    """Devuelve True si el número es par, False si es impar"""
    return numero % 2 == 0


if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if es_par(numero):
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
