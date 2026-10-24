from pathlib import Path

from bs4 import BeautifulSoup

from errors import ParseError
from vacancy import Vacancy


def find_text(soup, data_qa):
    element = soup.find(attrs={"data-qa": data_qa})
    if element is None:
        return ""
    return element.get_text(" ", strip=True).replace("\xa0", " ")


def parse_vacancy_file(path):
    path = Path(path)
    soup = BeautifulSoup(path.read_bytes(), "html.parser")

    link = soup.find("link", rel="canonical")
    if link is None:
        raise ParseError(path.name, "нет ссылки canonical — это не страница вакансии hh")
    vacancy_id = link["href"].split("/")[-1]

    title = find_text(soup, "vacancy-title")
    if not title:
        raise ParseError(path.name, "у вакансии нет названия")

    key_skills = []
    for element in soup.find_all(attrs={"data-qa": "skills-element"}):
        key_skills.append(element.get_text(strip=True))

    return Vacancy(
        vacancy_id,
        title,
        find_text(soup, "vacancy-experience"),
        find_text(soup, "vacancy-description"),
        key_skills=key_skills,
        source_file=path.name,
    )