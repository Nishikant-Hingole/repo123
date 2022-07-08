stud_name = input("Enter your name \n")
print("How many subject")
subject = int(input())
student_mark = []
total = 0
for i in range(subject):
    z = int(input("Enter Subject Mark One by One \n"))
    student_mark.append(z)
    total += student_mark[i]

print("Your All Subject Mark is:", *student_mark)
percentage = total / subject
for x in student_mark:
    if (x >= 35):
        print("Congradulation", stud_name)
        print("Total Mark Obtained", total)
        print("Percentage:", percentage)
        break
    else:
        print("Sorry you are Fail")