def student():
    while True:
        print("--"*20,"Welcome to JanaPriya High Schools","--"*20)
        name = input("Enter your name: ")
        marks = int(input("Enter your marks: "))

        if marks > 90:
            print(f"Hello {name}!, you have secured Grade: 'A' in the final exams")
        elif 90 > marks > 80:
            print(f"Hi {name}!, you have secured Grade: 'B' in the final exams")
        elif 80 > marks > 70:
            print(f"Hi {name}!, you have secured Grade: 'C' in the final exams")
        elif 70 > marks > 60:
            print(f"Hi {name}!, you have secured Grade: 'D' in the final exams")
        else:
            print(f"Hi {name}!, you haven't secured any Grades, Better Luck next time...")

        # To checking for another students grade....
        checking_another_student = input("Do you have another student? (y/n): ")
        if checking_another_student.lower()[0]  != "y":
            print("Thanks you for your time!")
            break
