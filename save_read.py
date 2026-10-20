import json
from pathlib import Path

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
    with path.open("w") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)