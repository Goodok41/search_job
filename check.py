from collection import read_inbox
from save_read import save_vacancies

vacancies = read_inbox("inbox")
save_vacancies(vacancies, "data/vacancies.json")
print(len(vacancies))