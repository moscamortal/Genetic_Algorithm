import csv

class Teacher():

    def __init__(self):
        self.name = ""
        self.classPeriods = []
        self.periods = []
        self.classDays = 0

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
                    CSV_teacher.classPeriods.append(i) #Inseri o periodo informado no arquivo no objeto
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
        for period in self.classPeriods:
            if period != "0":
                self.classDays += 1
