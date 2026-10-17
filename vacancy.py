#Создание класса вакансии

class Vacancy:

    def __init__(self, vacancy_id, title, experience, description, salary="", key_skills=None, source_file=""):
        
        self.vacancy_id = vacancy_id
        self.title = title
        self.experience = experience
        self.description = description
        self.salary = salary
        if key_skills is None:
            key_skills = []
        self.key_skills = key_skills
        self.source_file = source_file

    def __repr__(self):
        return f"Vacancy(id={self.vacancy_id!r}, title={self.title!r})"

    def __str__(self):
        return f"{self.title} (id {self.vacancy_id}, опыт: {self.experience})"

