from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Пути к файлам
html_file_path = "C:/Users/Acer/PycharmProjects/meiranagay/Cpi.html"
csv_file_path = "C:/Users/Acer/PycharmProjects/meiranagay/economic_data.csv"

# Открываем и читаем HTML файл
with open(html_file_path, "r", encoding="utf-8") as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "html.parser")

# Находим таблицу в HTML файле
table = soup.find("table")

# Проверяем, что таблица найдена
if table:
    rows = table.find_all("tr")

    # Открываем CSV файл для записи
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Заголовок CSV файла
        writer.writerow(["Related", "Last", "Previous", "Unit", "Reference"])

        # Обрабатываем строки таблицы
        for row in rows[1:]:  # Пропускаем первую строку (заголовок)
            cells = row.find_all("td")
            related = cells[0].get_text(strip=True)
            last = cells[1].get_text(strip=True)
            previous = cells[2].get_text(strip=True)
            unit = cells[3].get_text(strip=True)
            reference = cells[4].get_text(strip=True)

            # Форматируем дату Reference
            reference_date = datetime.strptime(reference, "%b %Y")
            formatted_date = reference_date.strftime("%d-%m-%Y")


            # Записываем строку в CSV файл
            writer.writerow([related, last, previous, unit, formatted_date])

    print(f"Данные успешно записаны в {csv_file_path}")
