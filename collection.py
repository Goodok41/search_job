from pathlib import Path
from input_info import parse_vacancy_file

def read_inbox(folder):
    vacancies = {}
    for file in sorted(Path(folder).glob("*.html")):
        vacancy = parse_vacancy_file(file)
        vacancies[vacancy.vacancy_id] = vacancy
    return vacancies