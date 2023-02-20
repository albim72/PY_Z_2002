from homework import Homework
from exam import Exam

print("_____________ HOMEWORK _____________")
uc1 = Homework()
uc1.grade = 89
assert uc1.grade == 89
print(uc1.grade)

print("_____________ EXAM _____________")
uc2 = Exam()
uc2.writing_grade = 80
uc2.math_grade = 62

print(f'writing: {uc2.writing_grade}')
print(f'math: {uc2.math_grade}')
