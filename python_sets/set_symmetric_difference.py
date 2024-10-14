morning_courses = {"Java", "C", "Ruby", "C#", "Lisp"}
afternoon_courses = {"Python", "C#", "Java", "C", "Ruby"}

possible_courses = morning_courses ^ afternoon_courses
print(f"possible_courses = {possible_courses}")

morning_courses_list = ["Java", "C", "Ruby", "C#", "Lisp"]
afternoon_courses_list = ["Python", "C#", "Java", "C", "Ruby"]

possible_courses_list = set(morning_courses_list).symmetric_difference(afternoon_courses_list)
print(f"possible_courses_list = {possible_courses_list}")

print(set(afternoon_courses_list).symmetric_difference(morning_courses_list))