import random
import itertools

def tournamentSelection(population, k):  #selection
    randomSelection = []
    for i in range(k):
        randomSelection.append(population[random.randint(0, len(population)-1)])

    fitness1 = fitnessValue(randomSelection)
    indexOfBest = fitness1.index(max(fitness1))

    parent1 = randomSelection[indexOfBest]
    
    randomSelection = []
    for i in range(k):
        randomSelection.append(population[random.randint(0, len(population)-1)])
    
    fitness2 = fitnessValue(randomSelection)
    indexOfBest = fitness2.index(max(fitness2))

    parent2 = randomSelection[indexOfBest]

    return parent1, parent2

def fitnessValue(population):  #objective function
    return list(2*pow(int((population[i]),2),2)+1 for i in range(0, len(population)))

def initialPopulation(p):    #formulation and encoding
    return list("{:03b}".format(random.randint(0,6)) for i in range(1, p+1))

def crossover(parent1, parent2, crossProb):
    offList1 = list(parent1)
    offList2 = list(parent2)
    if(random.random() < crossProb):
        crossoverPoint = random.randint(0,2)
        for i in range(crossoverPoint, 3):
            offList1[i], offList2[i] = offList2[i], offList1[i]   #swap
    
    return ''.join(offList1), ''.join(offList2)

def mutation(offspring1, offspring2, mutationProb):
    
    mutatedList1 = list(offspring1)
    mutatedList2 = list(offspring2)
    if(random.random() < mutationProb):
        
        for i in range(0,3):
            if random.randint(0,1)==1:
               if mutatedList1[i]=='0':
                    mutatedList1[i]='1'

               else:
                    mutatedList1[i]='0'

               if mutatedList2[i] =='0':
                   mutatedList2[i] = '1'

               else:
                   mutatedList2[i] ='0'
    
    return ''.join(mutatedList1), ''.join(mutatedList2)

p = int(input("Enter the number of individuals in the population: "))
k = int(input("Enter k for Tournament Selection: "))

crossoverProbability = float(input("Enter the crossover probability: "))
mutationProbability = float(input("Enter the mutation probability: "))

generated = 0
expanded = 0

initialPop = initialPopulation(p)
print('\nInitial Population: ', initialPop)
generated += p

currentPop = initialPop.copy()
indexOfBest = 0
solution = 0
nextPop = []

while generated < 10000:
    maxFit = 0
    nextPop = currentPop.copy()
    fitness = fitnessValue(nextPop)
    
    for i in range(0, len(fitness)):
        if maxFit < fitness[i] and int((nextPop[i]),2) > 0 and int((nextPop[i]),2) <= 6:
            maxFit = fitness[i]
            indexOfBest = i

    solution = int((nextPop[indexOfBest]),2)
    nextPop = []

    for i in range(0, int(p/2)):
        parent1, parent2 = tournamentSelection(currentPop, k)
        expanded += 2
        offspring1, offspring2 = crossover(parent1, parent2, crossoverProbability)
        mutated1, mutated2 = mutation(offspring1, offspring2, mutationProbability)

        nextPop.append(mutated1)
        nextPop.append(mutated2)

    currentPop = nextPop.copy()
    generated += p
    print("Next Population: ", currentPop)

print('\nInitial Population: ', initialPop)
print('Maximum value of x is: ', solution)
print('No of nodes generated: ', generated)
print('No of nodes expanded: ', expanded)