def calculate_gpa(grades, course_credits):
    grade_points = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'F': 0.0
    }

    total_credits = 0
    total_grade_points = 0

    for course, grade in grades.items():
        credit_hours = course_credits.get(course, 0)
        total_credits += credit_hours
        total_grade_points += grade_points.get(grade, 0) * credit_hours

    return total_grade_points / total_credits if total_credits != 0 else 0.0

def main():
    course_credits = {
        'MATH 202': 3,
        'CIT 202': 3,
        'CYB 204': 3,
        'CYB 206': 2,
        'CIT 204': 2,
        'CSC 202': 3,
        'IFT 206': 3,
        'CYB 202': 2
    }


    print("")
    print("Students GPA Calcluator") 
    print("==========================================")
    print("")
    num_students = int(input("Enter the number of students(e.g 2): "))
    print("___________________________________________________")
    print("")
    students_data = []

    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        student_grades = {}

        for course in course_credits.keys():
            grade = input(f"Enter grade for {course} (A/B/C/D/F): ")
            student_grades[course] = grade

        gpa = calculate_gpa(student_grades, course_credits)
        students_data.append({
            'name': name,
            'gpa': gpa,
            'grades': student_grades
        })
        print("==========================================") 
        print(" ")

    highest_gpa_student = max(students_data, key=lambda x: x['gpa'])
    lowest_gpa_student = min(students_data, key=lambda x: x['gpa'])

    print("\nStudent's CGPA Summary:")
    for student in students_data:
        print(f"{student['name']} - GPA: {student['gpa']:.2f}")

    print(f"\nHighest GPA: {highest_gpa_student['name']} - (GPA: {highest_gpa_student['gpa']:.2f})")
    print(f"Lowest GPA: {lowest_gpa_student['name']} - (GPA: {lowest_gpa_student['gpa']:.2f})")

if __name__ == "__main__":
    main()
