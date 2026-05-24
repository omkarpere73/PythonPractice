students = [("A", 70), ("B", 85), ("C", 60), ("D", 85)]

sorted_students1 = sorted(students , key = lambda x: x[0])
print(sorted_students1)

sorted_students2 = sorted(students , key = lambda x: x[1])
print(sorted_students2)