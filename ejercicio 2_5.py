def letras_unicas(palabra):
    letras = set(palabra)
    letras_ordenadas = sorted(letras)
    return letras_ordenadas
resultado = letras_unicas("entretenido")
print(resultado) 