from teacher import Teacher
from population import Population

def main():
    teacher_List = []
    population_List = [] #Populacao do algoritmo

    teacher_List = Teacher.teacher_initialize(teacher_List)
    Teacher.periods_initialize(teacher_List)
    Population.start_Random_Population(teacher_List,population_List) #Gera a primeira populacao

if __name__ == "__main__":
    main()
