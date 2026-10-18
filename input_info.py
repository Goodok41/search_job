from pathlib import Path
from bs4 import BeautifulSoup
from vacancy import Vacancy

def parse_vacancy_file(path):
    path = Path(path)
    soup = BeautifulSoup(path.read_bytes(), "html.parser")

    link = soup.find("link", rel="canonical")
    vacancy_id = link["href"].split("/")[-1]

    title = soup.find(attrs={"data-qa": "vacancy-title"}).get_text(strip=True)
    experience = soup.find(attrs={"data-qa": "vacancy-experience"}).get_text(strip=True)

    description_element = soup.find(attrs={"data-qa": "vacancy-description"})
    if description_element is None:
        description = ""
    else:
        description = description_element.get_text(strip=True)

    key_skills = []
    for element in soup.find_all(attrs={"data-qa": "skills-element"}):
        key_skills.append(element.get_text(strip=True))

    return Vacancy(vacancy_id, title, experience, description=description, key_skills=key_skills, source_file=path.name)