print("Attendance Calculator")
total = int(input("Total Classes Conducted: "))
attended = int(input("Classes Attended: "))
percentage = (attended / total) * 100
print("Attendance =", round(percentage, 2), "%")
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
