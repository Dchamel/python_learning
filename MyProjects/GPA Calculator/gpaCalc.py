#GPA Calculator Grade Point Average

from time import  perf_counter
t1 = perf_counter()
gradesSubjects = [5,4,4,5,4,5,5,4,4,4,4,3,3,3,4,4,3,3,4,4,5,4,3,4,3,4,4,3,4,4,5,4,3,4,3,4,3]
# gradesSubjectsTest = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
gradesSubjectsTest = []
gradesCoursework = [3,4,4,5,3,4,5,5,5,5,4,5,5]
gradesPractice = [5,5,5,5]
gradesDiploma = [5]

#RU GPA
gradesTotal = gradesSubjects + gradesCoursework + gradesPractice + gradesDiploma + gradesSubjectsTest
print(len(gradesTotal))
j = 0
for i in gradesTotal:
    j += i
print(f'Simple RU GPA - {j / len(gradesTotal):.2}')

#EN GPA


t2 = perf_counter()
print(f'{t2-t1:.6f} sec')