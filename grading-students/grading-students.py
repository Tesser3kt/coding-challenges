MULTIPLES_OF_FIVE = [x for x in range(101) if x % 5 == 0]

def round_grade(grade: int) -> int:
    for multiple in MULTIPLES_OF_FIVE:
        if grade >= 38 and grade <= multiple:
            if abs(grade - multiple) < 3:
                return multiple
    return grade

def app():
    number_of_grades = int(input())
    rounded_grades = []
    for i in range(number_of_grades):
        rounded_grades.append(round_grade(int(input())))
    for grade in rounded_grades:
        print(grade)

app()
