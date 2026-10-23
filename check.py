from report import count_skills, print_report, save_report
from save_read import load_vacancies
from skills import load_synonyms

vacancies = load_vacancies("data/vacancies.json")
synonyms = load_synonyms("synonyms.json")

counter = count_skills(vacancies, synonyms)
print_report(counter, len(vacancies))
save_report(counter, len(vacancies), "data/skills.csv")