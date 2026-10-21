from collection import read_inbox
from save_read import load_vacancies, save_vacancies

STATE_FILE = "data/vacancies.json"

vacancies = load_vacancies(STATE_FILE)
print("Было в памяти:", len(vacancies))

vacancies.update(read_inbox("inbox"))
print("Стало:", len(vacancies))

save_vacancies(vacancies, STATE_FILE)