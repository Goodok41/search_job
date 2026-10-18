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

    return Vacancy(vacancy_id, title, experience, description="", source_file=path.name)