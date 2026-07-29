total=0
for i in range (1,6):
    mark=float(input("Enter the mark of Subjects" + str(i) + ":"))
    total += mark

average=total/5
if average >= 90:
    grade= "S"
elif average >= 80:
    grade= "A"
elif average >= 70:
    grade= "B"
elif average >= 60:
    grade= "C"
elif average >= 50:
    grade= "D"
else :
    grade = "F"
print("Total Marks =", total)
print("Average =", average)
print("Grade =", grade)
