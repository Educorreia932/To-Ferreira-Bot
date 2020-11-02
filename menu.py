import datetime
import re
import requests

from bs4 import BeautifulSoup
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text

URL = "https://sigarra.up.pt/sasup/pt/web_base.gera_pagina?P_pagina=265689"

canteens = {
    "FEUP": "Cantina de Engenharia",
    "FMUP": "Cantina de S. João"
}

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

def retrieve_menu_pdf(university):
    """Retrieve's a canteen's menu PDF file"""
    university = university.upper()

    # Retrieve menu's PDF link
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, features="lxml")

    menu_anchors = soup.select("div.mobile a")

    for anchor in menu_anchors:
        canteen_name = anchor.next

        if canteen_name == canteens[university]:
            pdf_url = "https://sigarra.up.pt/sasup/pt/" + anchor["href"]

    r = requests.get(pdf_url)
    open(university + ".pdf", 'wb').write(r.content)

def calculate_page(pdf_file):
    """Auxiliary function to calculate the week's menu corresponding page from the PDF file"""
    lines = extract_text(pdf_file, page_numbers=[0]).split("\n")

    for line in lines:
        if re.search('^PERÍODO:|^Semana', line): # Search for week's date line
            line = line.lower()

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

            return week + 1

def retrieve_menu_image(university):
    pdf_file = university + ".pdf"

    page = calculate_page(pdf_file)

    menu = convert_from_path(pdf_file, 500, first_page=page, last_page=page + 1)[0]
    menu.save('out.jpg', 'JPEG')
