import random

def PSO(marks, k, numOfParticles, iterations):
    generated = 0    #initialization
    expanded = 0

    positions = []
    for i in range(0, numOfParticles):
        pos = []
        for j in range(0, k):
            pos.append(marks[random.randint(0, len(marks)-1)])
        positions.append(pos)

    velocity = []
    for i in range(0, numOfParticles):
        vel = []
        for j in range(0, k):
            vel.append(0)
        velocity.append(vel)
        
    fitness = []
    for i in range(0, len(positions)):
        fitness.append(fitnessValue(positions[i], marks))

    pbestPosition = positions.copy()
    gbestPosition = positions[fitness.index(min(fitness))]
    print('\nInitialization done!')
    print('\nIteration 1')
    print('Positions: ', positions)
    print('Velocities: ', velocity)
    print('Pbest: ', fitness)
    print('Pbest positions: ', pbestPosition)
    print('Gbest positions: ', gbestPosition)
    print('Gbest value: ', fitness[fitness.index(min(fitness))])
    print()

    c1 = 2      #updation
    c2 = 2
    generated += numOfParticles
    expanded += numOfParticles
    it = 2
   
    while it <= iterations:
      vUpdated = []
      pUpdated = []
      for i in range(0,numOfParticles):
            v = velocity[i].copy()
            pb = pbestPosition[i].copy()
            s = positions[i].copy()
            gb = gbestPosition.copy()

            for j in range(0,len(velocity[i])):
                v[j] = v[j]+ c1*random.randint(0,1)*(pb[j]-s[j])+ c2*random.randint(0,1)*(gb[j]-s[j])
            
            vUpdated.append(v)

            for j in range(0, len(positions[i])):
                s[j] = s[j] + v[j]
            pUpdated.append(s)

      velocity = vUpdated.copy()
      position = pUpdated.copy()

      for i in range(0, numOfParticles):
            if fitnessValue(pbestPosition[i],marks) > fitnessValue(positions[i],marks):
                pbestPosition[i] = positions[i].copy()
                fitness[i] = fitnessValue(pbestPosition[i],marks)

      print('Updatation! \n')
      print('Iteration ', it, ': ')
      print('Positions: ', positions)
      print('Velocities: ', velocity)
      print('Pbest: ', fitness)
      print('Pbest positions: ', pbestPosition)
      print('Gbest positions: ', gbestPosition)
      print('Gbest value: ', fitness[fitness.index(min(fitness))])
      print()

      it += 1
      generated += numOfParticles
      expanded += numOfParticles

    groupRepresentative = gbestPosition
    print('Group representatives: ', groupRepresentative)
    print("Groups:")
    for i in range(0, k):
        groups = []
        for j in range(0,len(marks)):
            index = difference(groupRepresentative, marks[j])
            if index == i:
                groups.append(marks[j])
        print(groups)

    print('No of nodes generated: ', generated)
    print('No of nodes expanded: ', expanded)

def difference(state, n):
    diff = []
    for j in range(0, len(state)):
            d = abs(state[j] - n)
            diff.append(d)
    return diff.index(min(diff))

def fitnessValue(state, marks):
    objValue = 0
    for i in range(0, len(marks)):
        diff = []
        for j in range(0, len(state)):
            d = abs(state[j] - marks[i])
            diff.append(d)
        objValue += diff[diff.index(min(diff))]**2
    return objValue

numOfParticles = 3
iterations = 5
print('Number of particles: ', numOfParticles)
print('Number of interations: ', iterations)
n = int(input('Enter the number of students: '))
k = int(input('Enter the number of groups: '))
maxMarks = int(input('Enter max marks: '))
print('Enter marks: ')
i = 0
marks = []
while i < n:
    mark = int(input())
    if(mark < 0 or mark > maxMarks):
        print('Marks not in range! Enter again.')
        continue
    marks.append(mark)
    i += 1

PSO(marks, k, numOfParticles, iterations)


