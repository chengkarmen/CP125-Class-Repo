#Name: CHENG KARMEN
#Problem description: Write a Python program that checks the grade for one student.

def determine_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
    
marks = float(input("Enter the student's mark: "))
print(f"Mark: {marks}, Grade: {determine_grade(marks)}")