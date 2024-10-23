def contiene_ceros_consecutivos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False
resultado1 = contiene_ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5)
print(resultado1)  

resultado2 = contiene_ceros_consecutivos(6, 0, 5, 1, 0, 3, 0, 1)
print(resultado2)  