"""
Project: Smart Grade Analyzer
Level: Python Basics
Topics: Conditions, Comparison Operators, Logical Operators
"""

print("=" * 45)
print("          SMART GRADE ANALYZER")
print("=" * 45)

name = input("Enter student name: ").strip()
score = float(input("Enter score (0-100): "))

print("\n" + "-" * 45)

if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")

else:
    if score >= 90:
        grade = "A"
        message = "Excellent performance!"
    elif score >= 80:
        grade = "B"
        message = "Very good work!"
    elif score >= 70:
        grade = "C"
        message = "Good job!"
    elif score >= 60:
        grade = "D"
        message = "You passed, but keep improving."
    else:
        grade = "F"
        message = "You need more practice."

    status = "PASS" if score >= 60 else "FAIL"

    print(f"Student : {name}")
    print(f"Score   : {score:.2f}/100")
    print(f"Grade   : {grade}")
    print(f"Status  : {status}")
    print(f"Feedback: {message}")

    if score >= 95:
        print("Achievement: Outstanding!")

    elif score < 40:
        print("Advice: Review the basics and practice daily.")

print("-" * 45)
print("Analysis completed.")
