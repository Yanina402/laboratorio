def es_primo(n):
    """Función auxiliar para determinar si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(num):
    primos = []
    for i in range(num + 1):
        if es_primo(i):
            primos.append(i)
            print(i)  
    
    return len(primos)  

cantidad_primos = contar_primos(20)
print(f"Cantidad de números primos encontrados: {cantidad_primos}")