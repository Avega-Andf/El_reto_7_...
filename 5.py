n = float(input("ingrese un numero ")) #Se ingresa el numero al que se le quiere sacar el factorial
x = n #El valor "x", sera el que multiplicara a la variable "n", y comenzara teniendo el mismo valor que "n"

while x > 1: # El bucle va hasta que "x" llega 1, ya que si llega a 0, todo el bucle daria cero
    print(n) #Se imprimen todos los resultados hasta llegar, al factorial del numero
    x -= 1 #Se resta 1 a la variable "x"
    n *= x # Se multiplica "n" por "x" ejm: Factorial de 4 = (4*4)*(4*3)*(4*2)*(4*1), siendo los numeros 4,3,2,1 la variable x, donde cada vez disminuye una unidad
    
print ("El factorial del numero dado es: " +str(n) ) #Se imprime el ultimo valor de n, que seria el valor factorial