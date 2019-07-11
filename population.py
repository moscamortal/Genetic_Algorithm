import random
class Population():

    def start_Random_Population(teacher_List, population_List):
        population_Leng = 100 #Defini o tamanho da populacao
        i = 0
        while i <= population_Leng:  #Executa a quantida de vezes igual ao tamanho da populacao
            for teacher in teacher_List: #Executa uma vez para cada professor dessa solucao
                avaliable_days = 0
                for week_Day in teacher.classWeekPeriods: #Executa para cada dia da semana
                    if avaliable_days <= teacher.classDaysAvaliable: 
                        if random.choice([True, False]): #Gera um random para adicionar um periodo ao dia da semana
                            population_List.append(random.choice(teacher.periods)) 
                            avaliable_days += 1
                        else:
                            population_List.append("0")



