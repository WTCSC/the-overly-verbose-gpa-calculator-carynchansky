# Overview
**GPA Calculator** - this Python program calculates a student’s current GPA, analyzes semester performance, and checks whether a goal GPA is achievable by improving grades.
It follows all the requirements for the GPA Calculator assignment, including input validation, list slicing, and clear, user-friendly feedback.

## Features
* Ask the user how many grades they want to enter (must be at least 5).
* Validate every grade to ensure it’s a number between 0.0 and 4.0.
* Calculate and display the overall GPA with a personalized message.
* Allow semester GPA comparison using list slicing.
* Check if the user’s goal GPA can be reached by raising a single grade to 4.0.
* Provide friendly, clear, and motivational feedback throughout.

## How It Works

1. Input Grades

    * The program asks how many grades to enter (minimum 5).

    * Each grade must be between 0.0 and 4.0.

    * Invalid input is handled gracefully with error messages.

2. Calculate Current GPA

    * The total sum of grades is divided by the number of grades.

    * The GPA is displayed in a fun, descriptive message (e.g. "Beep boop... Your GPA is 3.24!").

3. Semester GPA Analysis

    * The user chooses to analyze either the first or second half of their classes.

    * The program uses slicing (grades[:mid] or grades[mid:]) to compare semester GPAs with the overall GPA.

4. Goal GPA Analysis

    * The user enters a goal GPA.

    * The program checks if that goal is achievable by changing just one grade to 4.0.

    * If achievable, it tells the user which grade to improve; otherwise, it explains they need to improve multiple grades.

## How to Run

1. Save the program as gpa_calculator.py.

2. Open a terminal or command prompt.

3. Run:

    **python3 gpa_calculator.py**

4. Follow the on-screen prompts to enter your grades and analyze your GPA!