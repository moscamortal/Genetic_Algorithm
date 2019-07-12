from teacher import Teacher
from population import Population
from csv_Manager import Csv_Manager

def main():
    teacher_List = []
    population_List = [] #Populacao do algoritmo

    teacher_List = Teacher.teacher_initialize(teacher_List)
    Teacher.periods_initialize(teacher_List)
    population_List = Population.start_Random_Population(teacher_List,population_List) #Gera a primeira populacao

    Csv_Manager.write_list_to_file(population_List,"result.csv")

if __name__ == "__main__":
    main()
