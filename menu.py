import datetime
import re

from pdf2image import convert_from_path
from pdfminer.high_level import extract_text

months = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12
}

pdf_file = "engenharia.pdf"

lines = extract_text(pdf_file, page_numbers=[0]).split("\n")

for line in lines:
    if re.search('^Semana de', line):
        numbers_pattern = r'\d+'
        months_pattern = '|'.join(re.escape(s) for s in months)
        regex = re.compile(months_pattern + "|" + numbers_pattern)

        date = regex.findall(line)[-3:]

        day = int(date[0])
        month = months[date[1]]
        year = int(date[2])

        d1 = datetime.date(year, month, day)

        d2 = datetime.date.today()
        d2 = d2 + datetime.timedelta(days= 6 - d2.weekday()) # Last day of current week

        week = (d2 - d1).days // 7

pages = convert_from_path(pdf_file, 500, first_page=1, last_page=2)

for page in pages:
    page.save('out.jpg', 'JPEG')
