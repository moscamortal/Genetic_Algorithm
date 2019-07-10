from teacher import Teacher

def main():
    teacher_List = []

    teacher_List = Teacher.teacher_initialize(teacher_List)
    Teacher.periods_initialize(teacher_List)

if __name__ == "__main__":
    main()
