def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    intermedio = num1 + num2 + num3 - mayor - menor  

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:  
        return intermedio
resultado = devolver_distintos(5, 3, 7)
print(resultado)  