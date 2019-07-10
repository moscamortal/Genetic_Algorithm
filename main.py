from teacher import Teacher
<<<<<<< HEAD

def main():
    teacher_List = []

    teacher_List = Teacher.teacher_initialize(teacher_List)
    Teacher.periods_initialize(teacher_List)
=======
from population import Population

def main():
    teacher_List = [] #Lista dos professores carregados
    population_List = [] #População do algoritmo

    teacher_List = Teacher.teacher_initialize(teacher_List) #Instancia os professores 
    Teacher.periods_initialize(teacher_List) #Carrega os periodos de cada professor
    Population.start_Random_Population(teacher_List,population_List) #Gera a primeira população
>>>>>>> 636eef40fdb63904bcc6b1c910f5a69afa5de227

if __name__ == "__main__":
    main()
