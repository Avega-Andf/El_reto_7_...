A = 25.0 # inicializa el valor de la poblacion A en 25 millones
B = 18.9 # inicializa el valor de la poblacion B en  18,9 millones
Año = 1 # Año inicial 

while B < A: # El condicional sera mientras B sea menor que A
  print("Año: " +str(Año) + ", Poblacion A: " + str(round(A,2)) + ", Población B "+ str(round(B,2))) # Se imprimen los valores A y B, y la cantidad de años que han transcurrido
  A *= 1.02 # A se multıplica por 1.02, que seria aumentarle un 2% 
  B *= 1.03 # B se multıplica por 1.03, que seria aumentarle un 3% 
  Año += 1 # El año aumenta
  
print("Fin.") # Se imprime al terminar el ciclo while

print("Despues de " +str(Año)+ " años, la segunda poblacion es mayor que la primera, poblacion de A: " +str(round(A,2)) + " Poblacion de B: " + str(round(B,2))) # Se imprimen los ultimos valores y el año en donde ahora  la poblacion B es mayor que la de A