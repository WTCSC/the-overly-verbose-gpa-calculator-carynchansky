def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0.0 <= grade <= 4.0:
                return grade
            else:
                print("Invalid grade. Please enter a number between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 3.5).")


def get_grades():
    grades = []
    print("\nGPA Entry")

    while True:
        try:
            num_grades = int(input("How many grades would you like to enter?: "))
            if num_grades <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(num_grades):
        grade = get_valid_grade(f"Grade #{i+1}: ")
        grades.append(grade)

    return grades




def calculate_gpa(grades):
    return sum(grades) / len(grades)


def display_gpa(grades):
    gpa = calculate_gpa(grades)
    print(f"\nCalculating... beep boop... Your GPA is: {gpa:.2f}")
    print(f"Based on {len(grades)} classes, your GPA is currently sitting at: {gpa:.2f}")
    return gpa


def semester_analysis(grades, overall_gpa):
    print("\nSemester GPA Analysis")
    if len(grades) < 2:
        print("Not enough grades for semester analysis.")
        return

    
    choice = input("Analyze (1) first half or (2) second half? ").strip()
    mid = len(grades) // 2

    if choice == "1":
        semester_grades = grades[:mid]
        sem_label = "first"
    else:
        semester_grades = grades[mid:]
        sem_label = "second"

    sem_gpa = calculate_gpa(semester_grades)
    print(f"\nThe {sem_label} semester GPA is: {sem_gpa:.2f}")

    if sem_gpa > overall_gpa:
        print("Nice! You improved this semester!")
    elif sem_gpa < overall_gpa:
        print("GPA declined this semester. You got this — keep improving!")
    else:
        print("GPA stayed consistent across semesters.")


def goal_gpa_analysis(grades, current_gpa):
    print("\nGoal GPA Analysis")
    goal = get_valid_grade("Enter your goal GPA (0.0–4.0): ")

    if goal <= current_gpa:
        print(f"Congratulations! You already meet or exceed your goal GPA of {goal:.2f}.")
        return

    achievable = False
    for i in range(len(grades)):
        temp_grades = grades.copy()
        temp_grades[i] = 4.0
        new_gpa = calculate_gpa(temp_grades)
        if new_gpa >= goal:
            print(f"You can reach your goal by improving grade #{i+1} to 4.0.")
            print(f"Your new GPA would be {new_gpa:.2f}.")
            achievable = True
            break

    if not achievable:
        print("Raising only one grade to 4.0 won’t reach your goal.")
        print("You’ll need to improve multiple grades to hit your target.")


def main():
    print("Welcome to the GPA Calculator!\n")

    grades = get_grades()

    overall_gpa = display_gpa(grades)

    semester_analysis(grades, overall_gpa)

    goal_gpa_analysis(grades, overall_gpa)

    print("\n Program complete. Thanks for using the GPA Calculator!")


if __name__ == "__main__":
    main()
