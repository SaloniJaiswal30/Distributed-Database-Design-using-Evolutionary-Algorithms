import csv
from random import randint
from random import random
from random import shuffle

#Functions

#Mutate function
def mutate(parent):
    child = list(parent)
    index1 = randint(0,chromosome_size-1)
    index2 = randint(0,chromosome_size-1)
    while (index2 == index1) :
        index2 = randint(0,chromosome_size-1)
    temp = child[index1]
    child[index1] = child[index2]
    child[index2] = temp
    return child
#end mutate

#crossover(PMX) function
def crossover(parent1 , parent2):
    child=[]
    for i in range(0,len(parent1)):
        child.append(0)
    index1 = randint(0,len(parent1)-1)
    index2 = randint(0,len(parent2)-1)
    if(index1==index2):
        index2 = randint(0,len(parent2))
    if (index2<index1):
        temp=index1
        index1=index2
        index2=temp
    t=index2-index1
    for i in range(index1,index2):
        child[i]=parent1[i]
    for i in range(index1,index2):
        p=0
        for j in range(0,t+1):
            if(parent2[i]==child[j]):
                p=p+1
                break
        if(p==0): 
            #print (parent2[i])
            r=parent2[i]
            check(i,parent1,parent2,r,child)

    for i in range (0,len(parent1)):
        p=0
        for j in range(0,len(parent1)):
            if (parent2[i]==child[j]):
                p=p+1
                break
        if(p==0):
            for j in range(0,len(parent1)):
                if(child[j]==0):
                    child[j]=parent2[i]
                    break
    
    return child
def check(n,parent1,parent2,r,child):
    for i in range(0,len(parent1)):
        if (parent2[i]==parent1[n]):
            if(child[i]==0):
                child[i]=r
                return
#end crossover

#fitness function 
def cost(q):
    count = 0
    for i in range(0,len(q)):
        #t=count
        for j in range (0,len(q)):
            count=count+(flow[i][j]*distance[q[i]][q[j]])
        #t=count+F_l[i][q[i]]
    return count   
#end fitness

#print "Default chromosome size : 9"
max_generations = int(input("Enter maximum number of Generations : "))
population_size = int(input("Enter Population Size : "))
flow = [[0, 10, 5, 2, 4, 1, 9, 12, 3],
        [15, 0, 3, 14, 4, 6, 11, 7, 6],
        [7, 6, 0, 10, 12, 5 , 9, 18, 9],
        [3, 5, 7, 0, 12, 17, 5, 2, 7],
        [11, 2, 4, 6, 0, 13, 6, 4, 22],
        [1, 12, 3, 14, 15, 0, 7, 8, 9],
        [2, 29, 4, 16, 2, 17, 0, 11, 4],
        [8, 2, 24, 13, 7, 10, 20, 0, 2],
        [22, 5, 1, 3, 2, 11, 19, 5, 0]]
distance=[[0, 12, 4, 12, 1, 3, 2, 0, 3],
          [1, 0, 13, 4, 14, 6, 11, 17, 1],
          [17, 26, 0, 1, 2, 15 , 8, 4, 7],
          [6, 25, 1, 0, 2, 7, 15, 5, 3],
          [12, 12, 4, 6, 0, 3, 16, 4, 12],
          [1, 2, 13, 4, 5, 0, 7, 18, 9],
          [9, 2, 24, 6, 5, 7, 0, 21, 14],
          [8, 12, 2, 3, 17, 20, 10, 0, 2],
          [2, 5, 10, 3, 25, 1, 9, 15, 0]]
chromosome_size = 9
mutation_rate = 1
crossover_rate = 1

chromosome = []
population = []

print ("\n\nGenerating random initial population... ")
print ("***********************************************")
#Random Population Generation
for i in range(0,chromosome_size):
    chromosome.append(i)
for i in range(0,population_size):
    shuffle(chromosome)
    population.append(list(chromosome))
print (population)
new_population = []

#Iterate for needed number of generations
for i in range(0,max_generations):
    print ("\nComputing Generation : ", i+1 , "... ")
    j=0
    while (j < population_size) :
        parent1 = population[j]
        print ("\t Parent",j+1,": ",parent1, "Cost :" , cost(parent1))
        if (j+1 == population_size):
            child = mutate(parent1)
            if(cost(child)<cost(parent1)):
                population[j]=child
            print ("\t\t After Mutation, Child",j+1,": ",population[j], "Cost :",cost(population[j]))
            break
        parent2 = population[j+1]
        print ("\t Parent",j+2,": ",parent2, "Cost :", cost(parent2))

        if(random() <= crossover_rate) :
            pcost1 = cost(parent1)
            pcost2 = cost(parent2)
            child1 = crossover(parent1,parent2)
            child2 = crossover(parent2,parent1)
            ccost1 = cost(child1)
            ccost2 = cost(child2)
            if(ccost1<pcost1):
                parent1 = child1
            if(ccost2<pcost2):
                parent2 = child2
            print ("\t\t After Crossover, Child",j+1,parent1,"Cost :",cost(parent1))
            print ("\t\t After Crossover, Child",j+2,parent2,"Cost :",cost(parent2))


        if(random()<=mutation_rate):
            pcost1 = cost(parent1)
            pcost2 = cost(parent2)
            child1 = mutate(parent1)
            child2 = mutate(parent2)
            ccost1 = cost(child1)
            ccost2 = cost(child2)
            if(ccost1<pcost1):
                parent1 = child1
            if(ccost2<pcost2):
                parent2 = child2
            print ("\t\t\t After Mutation, Child",j+1,parent1,"Cost :",cost(parent1))
            print ("\t\t\t After Mutation, Child",j+2,parent2,"Cost :",cost(parent2))

        population[j]=parent1
        population[j+1]=parent2
        j=j+2
    #end of while
#end of for
    
print ("Final Population : ")
print (population)
print ("***********************************************")
min_cost = cost(population[0])
min_index = 0
for i in range(1,population_size):
    temp = cost(population[i])
    if (temp<min_cost):
        min_cost = temp
        min_index = i

print ("Optimised allocation :",population[min_index])
print ("Optimised Cost :",min_cost)
