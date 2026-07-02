# Q3 — letter grade (elif ladder) 

grade = int(input("Input your grade (int) >> "))

if grade >= 90 and grade < 100:
    print("Grade: A")
elif grade >= 80 and grade < 90:
    print("Grade: B")
elif grade >= 70 and grade < 80:
    print("Grade: C")
elif grade >= 60 and grade < 70:
    print("Grade: D")
elif grade >= 0 and grade < 60:
    print("Grade: F")
else:
    print("ERROR: OUT OF RANGE!")