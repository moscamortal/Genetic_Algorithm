#Arquivos com funções que testam funcionalidades

def teacher_List_Test(teacher_List): # Teste para verificar se todos os itens da lista de professores estão instanciadas
    for teacher in teacher_List:
        print("Nome :" + teacher.name)
        print("Segunda :" + teacher.monday)
        print("Terça :" + teacher.tuesday)
        print("Quarta :" + teacher.wednesday)
        print("Quinta :" + teacher.thursday)
        print("Sexta :" + teacher.friday)

        print("Segunda2 :" + teacher.monday2)
        print("Terça2 :" + teacher.tuesday2)
        print("Quarta2 :" + teacher.wednesday2)
        print("Quinta2 :" + teacher.thursday2)
        print("Sexta2 :" + teacher.friday2+"\n")