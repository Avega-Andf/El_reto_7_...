x = int(input("Ingrese un numero"))
if x % 2 != 0: #Si el numero no es par se le resta 1, para que se vuelva par
    x -= 1 
while x >= 2: #El condicional hace que el codigo se imprime hasta que llegue a 2
    print(x)
    x -= 2 #Al restarle 2 a un numero par, el resultado va a seguir siendo par 