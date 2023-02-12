student_heights = input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])

print(student_heights)

sum_height = 0
for n in range(0,len(student_heights)):
    sum_height += student_heights[n]

print(round(sum_height/len(student_heights)))