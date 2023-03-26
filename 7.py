x = int(input("Ingrese un numero mayor o igual a 2 y menor o igual que 50")) #Se ingresa el valor al que se le quiere sacar los divisores, pero debe ser un valor que este entro 2 y 50, incluyendolos
D = 1 #Se inicializa esta variable en 1,Este valor "D" seran los posibles divisores que tiene "x"

if x<2 or x>50: #Si la variable que se ingresa no pertenece al rango establecido se imprime un mensaje notificando eso
    print("El numero no pertenece al rango entre 2 y 50")

while D <= x: #El bucle se termina hasta que "D" tenga el mismo valor que la variable "x"
    if x < 2 or x > 50: #Si la variable que se ingresa no pertenece al rango se rompe la cadena while
        break
    if x % D == 0: # Si el modulo entre "x" y "D", es cero, el valor D es divisor de "x"
        print(str(D)+ " Es divisor de " +str(x)) #Y se imprime que "D" es divisor de "x"
    D += 1 # Se suma el valor de "D", hasta que llegue al valor de "x"