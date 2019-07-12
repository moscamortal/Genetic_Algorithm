import random
class Population():
    
    def start_Random_Population(teacher_List, population_List):
        population_Leng = 1000 #Defini o tamanho da populacao
        i = 0

        while i <= population_Leng:  #Executa a quantida de vezes igual ao tamanho da populacao
            individual = []

            for teacher in teacher_List: #Executa uma vez para cada professor dessa solucao
                to_Shuffle = ""
                to_Shuffle = (Population.complet_List_With_Zero(teacher.periods,len(teacher.classWeekPeriods)))
                random.shuffle(to_Shuffle)
                individual.extend()

            population_List.append(individual)
            i += 1

        print("População gerada")
        return(population_List)

    def complet_List_With_Zero(list_To_Complet, leng):

        while len(list_To_Complet) < leng:
            list_To_Complet.append("0")
        return (list_To_Complet)