population_a = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_b = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

#Suma la población de las dos listas, del elemento 7 en adelante
oldA = sum(population_a[7:])
oldB = sum(population_b[7:])

#Almacena en variables la suma de los datos de las 2 listas
sumA, sumB = sum(population_a), sum(population_b)
oldRateA, oldRateB = oldA/sumA, oldB/sumB

print('The degrees of aging in town A and B are {:5.3f} and {:5.3f} respectively.'.format(oldRateA, oldRateB))