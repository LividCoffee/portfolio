def sort_grades(grades):
    en_grades = ["A", "B", "C", "D", "F"]
    grades_upper = [grade.upper() for grade in grades]
    grades_count = range(len(grades))
    for char in grades_count:
        if grades_upper[char] not in en_grades:
            print("Одно из значений является недопустимым")
            break
        else:
            grades_upper.sort(reverse=True)
            print(grades_upper)
            break


sort_grades(['Ad', 'B', 'C', 'C', 'F', 'A'])
sort_grades(['b', 'c', 'C', 'f', 'A'])
sort_grades(['1', 'B+', 'C-', 'C', '@', 'A'])
