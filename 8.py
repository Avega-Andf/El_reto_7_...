def calcularprimo(n : int):
    i = 2 # se inicia con i=2, porque todos los numeros son divisibles entre uno, y no tendria sentido comenzar con uno
    if n == 2 : #Se inicia con n = 2
        print(n) #se imprime el valor de n=2, debido a que es el primer primo
    
    while i < n : #El condicional se realiza para todos los i menor que n
        if n % i == 0: #Si el module de n con i es igual a cero, n no es primo y se rompe el ciclo
            break #se rompe el ciclo
        elif i == n-1: #si no se rompe el ciclo, se seguira calculando el modulo de i, hasta que i sea igual a n-1
            print(n)  #Si llega hasta aca significa que n es primo, ya que no es divisible por ningun numero hasta un numero anterior a "n"  y se imprime el valor de n
        i += 1 #Se le suma una unidad a i para seguir probando el modulo entre n, se repite hasta que i sea menor que n

if __name__ == "__main__" :
    
    n = 2 #El valor del primer n
    Limite = 100 #La cantidad de numeros primos que se buscaran va desde 2 hasta 100
    
    while n < Limite: #mientras n sea menor que el limite de 100, se seguira probando por cada numero de la funcion calcularprimo 
        primo = calcularprimo(n) #se llama la funcion primo para hacer lo que pasa dentro de la funcion desde el numero 2 hasta el numero 100
        n += 1 #se le suma 1 a n, despues de cada ciclo hasta llegar a 100.