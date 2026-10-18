from collection import read_inbox

vacancies = read_inbox("inbox")
print("Вакансий:", len(vacancies))
for vacancy in vacancies.values():
    print(vacancy)