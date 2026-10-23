import csv
from collections import Counter
from pathlib import Path

from skills import find_skills


def count_skills(vacancies, synonyms):
    counter = Counter()
    for vacancy in vacancies.values():
        counter.update(find_skills(vacancy, synonyms))
    return counter

def print_report(counter, total):
    if total == 0:
        print("Вакансий нет: сохраните страницы в папку inbox")
        return

    print(f"Вакансий: {total}")
    for skill, count in counter.most_common():
        share = count / total * 100
        print(f"{skill:<28} {count:>3}  {share:.0f}%")

def save_report(counter, total, path):
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["навык", "вакансий", "доля, %"])
        for skill, count in counter.most_common():
            writer.writerow([skill, count, round(count / total * 100)])