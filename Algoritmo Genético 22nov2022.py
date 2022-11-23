import numpy as np
import matplotlib.pyplot as plt

from population import * #Función para crear la población
from gray2real import * #Para convertir en decimal, usando código gray
from fitness import * #Función para obtener el valor y saber qué tan apto es
from selection import *
from crossover import *
from mutation import *
from newindiv import *
from proyecto import *

def main():
    #create initial population
    n = 32    #num. of individuals
    c_len = 26 #length of chromosome
    pop = population(n,c_len)
    
    #######################################
    print("*** Genetic Algorithm ***")
    print("Population size:\t",n)
    print("Chromosome length:\t",c_len)
    #print("initial pop. ", pop)
    
    bestfits_g = []
    tg = int(input("Cantidad de generaciones: "))
    for g in range(tg):
        #maxgen = int(input("Number of generations: \t"))
        fit = []
        for indiv in pop:
            fit.append(fitness(gray2real(indiv)))
        #print("pop.fitness: ", fit)
        #print("min fitness: ", np.min(fit))
        #print("max fitness: ", np.max(fit))
        #print("mean fitness: ", np.mean(fit))
        #print("std_dev fitness: ", np.std(fit))

        fit_index = selection(fit)
        parent0 = pop[fit_index]
        #print(fit_index)
        #print("par0: ", parent0)

        fit_index = selection(fit)
        parent1 = pop[fit_index]

        while parent1 == parent0:
            fit_index = selection(fit)
            parent1 = pop[fit_index]

        #print(fit_index)
        #print("par1: ", parent1)

        offspring0, offspring1 = crossover(parent0, parent1)

        offspring0 = mutation(offspring0)
        offspring1 = mutation(offspring1)

        #print("off0: ", offspring0)
        #print("off1: ", offspring1)

        fit_p0 = fitness(gray2real(parent0))
        fit_p1 = fitness(gray2real(parent1))
        fit_o0 = fitness(gray2real(offspring0))
        fit_o1 = fitness(gray2real(offspring1))

        #print("fit_par0: ", fit_p0)
        #print("fit_par1: ", fit_p1)
        #print("fit_off0: ", fit_o0)
        #print("fit_off1: ", fit_o1)

        newpop = []
        #Selección de padres/hijos
        if fit_o0 <= fit_p0 or fit_o0 <= fit_p1:
            newpop.append(offspring0)
        if fit_o1 <= fit_p0 or fit_o1 <= fit_p1:
            newpop.append(offspring1)
        if fit_p0 <= fit_o0 and fit_p0 <= fit_o1:
            newpop.append(parent0)
        if fit_p1 <= fit_o0 and fit_p1 <= fit_o1:
            newpop.append(parent1)

        #Incluir al mejor individuo (elitismo, mejor aptitud)
        bestfit = min(fit) #Aptitud máxima
        bestfits_g.append(bestfit)
        #print(bestfit)
        bestindex = fit.index(bestfit) #El índice (en la lista fit), número de posición, con la aptitud máxima
        newpop.append(pop[bestindex])

        #Elitismo extendido (no solamente el mejor, grupo de mejores)
        meanfit = np.mean(fit)
        stddevfit = np.std(fit)
        for i in range(len(fit)):
            if fit[i] < meanfit - stddevfit: #Mayor que la media y una desviación estándar (top)
                newpop.append(pop[i])

        #Fillers (rellenos)
        while(len(newpop) < n):
            newpop.append(newindiv(c_len))
            
        pop = newpop
    
    bestfit = min(fit) #Aptitud máxima
    bestindex = fit.index(bestfit) #El índice (en la lista fit), número de posición, con la aptitud máxima
    sol = gray2real(pop[bestindex])
    solfit = fitness(sol)
    print(sol)
    Ri = R(sol[2],sol[3],rsq)
    s = ('W: '+str(round(1e6*sol[0],1))+'μm\t'+'L: '+str(round(1e6*sol[1],1))+'μm'+"\nR:", Ri, 'Ω')
    print("Solución: ", s)
    print("ECM: ", solfit)
    
    VR =[]
    Id = ID(beta,sol[0],sol[1],VGS,VT,VDS)
    for i in Id:
      VR.append(Ri*i)

    Grafica(VR_data,VGS,VR)

    plt.figure(2)
    plt.plot(bestfits_g)
    plt.show()
    

main()