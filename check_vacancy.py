from pathlib import Path

from input_info import parse_vacancy_file

for file in Path("inbox").glob("*.html"):
    vacancy = parse_vacancy_file(file)
    print(vacancy.title, vacancy.key_skills)