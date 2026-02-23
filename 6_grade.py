#Grade Calculator
sub1 = float(input("Enter marks for Subject 1:"))
sub2 = float(input("Enter marks for Subject 2:"))
sub3 = float(input("Enter marks for Subject 3:"))
sub4 = float(input("Enter marks for Subject 4:"))
sub5 = float(input("Enter marks for Subject 5:"))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100
print("\n--- Student Result ---")
print("Total Marks (out of 500):",total_marks)
print("Percentage:",percentage,"%")
if percentage >= 90:
    grade = "A+(Outstanding)"
elif percentage >= 80:
    grade = "A(Excellent)"
elif percentage >= 70:
    grade = "B(Good)"
elif percentage >= 60:
    grade = "C(Average)"
elif percentage >= 50:
    grade = "D(Pass)"
else:
    grade = "F(Fail)"
print("Grade:",grade)
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")