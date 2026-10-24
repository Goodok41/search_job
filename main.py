from collection import read_inbox
from report import count_skills, print_report, save_report
from save_read import load_vacancies, save_vacancies
from skills import load_synonyms

vacancies = load_vacancies("data/vacancies.json")
new_vacancies, skipped = read_inbox("inbox")
vacancies.update(new_vacancies)
save_vacancies(vacancies, "data/vacancies.json")

if skipped:
    print(f"Пропущено файлов: {len(skipped)}")
    for error in skipped:
        print(f"  {error}")

synonyms = load_synonyms("synonyms.json")
counter = count_skills(vacancies, synonyms)
print_report(counter, len(vacancies))
save_report(counter, len(vacancies), "data/skills.csv")