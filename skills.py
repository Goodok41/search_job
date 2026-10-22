import json
from pathlib import Path


def load_synonyms(path):
    with Path(path).open(encoding="utf-8") as file:
        return json.load(file)


def find_skills(vacancy, synonyms):
    text = vacancy.description + " " + " ".join(vacancy.key_skills)
    text = text.lower()

    found = set()
    for skill, variants in synonyms.items():
        for variant in variants:
            if variant in text:
                found.add(skill)
                break
    return found