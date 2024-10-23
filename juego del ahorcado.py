import random
palabras = ["python", "programacion","ahorcado", "desafio", "juego"]
def elegir_palabra():
        return random.choice(palabras)  
def pedir_letra():
    letra = input("elige una letra:").lower()
    while not letra.isalpha() or len(letra) != 1:
      letra = input("entrada no valida. Elige una letra: ").lower()
    return letra
def verificar_letra(palabra, letra):
    return letra in palabra
def mostrar_estado(palabra, letras_adivinadas):
    estado = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)
    print("palabra: ", estado)
def ha_ganado(palabra, letras_adivinadas):
    return all(letra in letras_adivinadas for letra in palabra)
def jugar():       
    palabra_secreta =  elegir_palabra()
    letras_adivinadas = set()
    vidas = 6
    print ("bienvenido al juego del ahorcado")
    while vidas > 0:
        mostrar_estado(palabra_secreta, letras_adivinadas)
        print(f"tienes {vidas} vidas restantes.")
        letra = pedir_letra()
        if letra in letras_adivinadas:
             print("ya has elegido esa letra.intenta con otra.")
             continue
        letras_adivinadas.add(letra)
        if verificar_letra(palabra_secreta, letra):
            print("muy bien hecho.la letra esta en la palabra.")
        else:
            vidas -= 1
            print("letra incorrecta.Has perdido una vida")
        if  ha_ganado(palabra_secreta, letras_adivinadas):  
            print(f"felicidades.Has adivinado la palabra:{palabra_secreta}")
            break
    else:
        print(f"Has perdido.La palabra era:{palabra_secreta}")
if __name__ == "__main__":
     jugar()       
              
        

            
