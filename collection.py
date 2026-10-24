from pathlib import Path

from errors import ParseError
from input_info import parse_vacancy_file


def read_inbox(folder):
    vacancies = {}
    skipped = []
    for file in sorted(Path(folder).glob("*.html")):
        try:
            vacancy = parse_vacancy_file(file)
        except ParseError as error:
            skipped.append(error)
        else:
            vacancies[vacancy.vacancy_id] = vacancy
    return vacancies, skipped