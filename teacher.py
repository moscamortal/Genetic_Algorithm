import csv

class Teacher():

    def __init__(self):
        self.name = ""
        self.classWeekPeriods = [] #Quais periodos da semana o professor está disponível
        self.periods = [] #Quais períodos o professor deve dar aula
        self.classDaysAvaliable = 0 #Dias disponíveis na semana para dar aula

    def teacher_initialize(teacher_List):
        with open("teacher.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                CSV_teacher = Teacher()
                CSV_teacher.name = row[0]
                iterrows = iter(row) #Ignora o primeiro item da list
                next(iterrows)
                for i in iterrows:
                    CSV_teacher.classWeekPeriods.append(i) #Inseri o periodo informado no arquivo no objeto
                CSV_teacher.classDays_count()
                teacher_List.append(CSV_teacher)
        return teacher_List

    def periods_initialize(teacher_List):
        with open("periods.csv") as f:
            reader = csv.reader(f)
            next(reader)
            count = 0
            for row in reader:
                iterrows = iter(row) #Ignora o primeiro item da list
                next(iterrows)
                for i in iterrows:
                    if i != "0":
                        teacher_List[count].periods.append(i) #Adiciona os periodos a lista de professores
                count += 1
        return teacher_List

    def classDays_count(self):
        for period in self.classWeekPeriods:
            if period != "0":
                self.classDaysAvaliable += 1
