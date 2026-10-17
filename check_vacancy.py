from vacancy import Vacancy

a = Vacancy("1", "Аналитик", "1–3 года", "SQL, Python")
b = Vacancy("2", "Аналитик", "нет опыта", "Excel")

print(repr(a))
print(repr(b)) 

a.key_skills.append("SQL")

print(a.key_skills)
print(b.key_skills)  