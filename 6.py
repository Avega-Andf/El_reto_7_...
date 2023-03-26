x = input("Piensa un número del 1 al 100, y cuando estés listo presiona enter para comenzar: ") #Al precionar la tecla enter comienza el codigo
y = 50 #Se inicializa la variable en el numero 50, porque es el numero que se encuentra en la mitad en el rango de 1 a 100

print("Acaso el número es:" + str(y) + "?") #El codigo comienza preguntando si el numero que piensas es el 50, a partir de eso:

Pregunta = input("El número que estás pensando es igual, poco menor , menor, poco mayor o mayor al que dije?: ")

while Pregunta != str("igual"): #Si se elige que es igual, el codigo se acaba e imprime que se adivino el numero
    if Pregunta == "poco menor": #Si no es igual, y se digita que es menor se resta 1 al valor actual, y se vuelve a preguntar
        y -= 1
    elif Pregunta == "poco mayor": #Si no es igual, y se digita que es mayor se suma 1 al valor actual, y se vuelve a preguntar
        y += 1
    elif Pregunta == "menor": #Se añaden opciones diferentes como poco menor,poco mayor, mayor y menor para avanzar al numero que se piensa algo mas rapido o algo mas lento segun se acerca al numero
        y -= 5
    elif Pregunta == "mayor": #Al digitar mayor o menor se le suma 5 unidades a diferencia de digitar poco menor o poco mayor
        y += 5
    
    print("Acaso el número es:" + str(y) + "?") #Por medio de este print se digita el nuevo numero
    
    Pregunta = input("El número que estás pensando es igual, poco menor , menor, poco mayor o mayor al que dije?: ") #Por medio de este print se vuelve a preguntar

print("¡He adivinado el número!") #Fin del bucle cuando se digita que el numero es igual al pensado