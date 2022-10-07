#GPA Calculator - Grade Point Average

from time import perf_counter
t1 = perf_counter()

#Grades from your diploma
gradesSubjects = [5,4,4,5,4,5,5,4,4,4,4,3,3,3,4,4,3,3,4,4,5,4,3,4,3,4,4,3,4,4,5,4,3,4,3,4,3]
gradesSubjectsHours = [170,170,425,408,799,102,552,102,133,102,266,170,68,102,102,102,85,289,102,216,211,126,184,243,243,102,192,102,170,102,136,136,68,96,121,85,102]
gradesSubjectsTest = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
gradesSubjectsTestHours = [200,68,170,80,119,136,50,102,102,96,102,95,76,76,96,96,96,109]
gradesCoursework = [3,4,4,5,3,4,5,5,5,5,4,5,5]
gradesPractice = [5,5,5,5]
gradesDiploma = [5]

#RU GPA
gradesTotal = gradesSubjects + gradesCoursework + gradesPractice + gradesDiploma + gradesSubjectsTest
j = 0
for i in gradesTotal:
    j += i
gpaRU = f'RU GPA - {j / len(gradesTotal):.2}'
print(gpaRU)

#US GPA
#Transfer of the school grades from RU to USA
#step1
gradesForUSTotal = []
gradesForUS = gradesSubjects + gradesSubjectsTest
for i in gradesForUS:
    if i == 5:
        gradesForUSTotal.append(4)
    elif i == 4:
        gradesForUSTotal.append(3)
    elif i == 3:
        gradesForUSTotal.append(2)
gradesHoursTotal = gradesSubjectsHours + gradesSubjectsTestHours

#step2
j = 0
for i in range(len(gradesForUSTotal)):
    j += gradesForUSTotal[i] * gradesHoursTotal[i]

#step3
k = 0
for i in gradesHoursTotal:
    k += i

#step4
gpaUS = f'US GPA - {(j/k):.1f}'
print(gpaUS)




t2 = perf_counter()
print(f'\nCalc time: {t2-t1:.6f} sec')