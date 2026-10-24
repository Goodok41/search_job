import json
from pathlib import Path
from vacancy import Vacancy

def save_vacancies(vacancies, path):
    data = {}
    for vacancy_id, vacancy in vacancies.items():
        data[vacancy_id] = {
            "title": vacancy.title,
            "experience": vacancy.experience,
            "description": vacancy.description,
            "key_skills": vacancy.key_skills,
            "source_file": vacancy.source_file,
        }

    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def load_vacancies(path):
    path = Path(path)
    if not path.exists():
        return {}

    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    vacancies = {}
    for vacancy_id, fields in data.items():
        vacancies[vacancy_id] = Vacancy(
            vacancy_id,
            fields["title"],
            fields["experience"],
            fields["description"],
            key_skills=fields["key_skills"],
            source_file=fields["source_file"],
        )
    return vacancies      