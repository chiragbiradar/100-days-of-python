student_scores = input("Input list of student scores ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

maxm=student_scores[0]
for n in range(0,len(student_scores)):
    if maxm<student_scores[n]:
        maxm=student_scores[n]

print(maxm)