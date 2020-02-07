import requests
from bs4 import BeautifulSoup

schools_names = {"FEUP": "Cantina de Engenharia",
                 "FMUP": "Cantina de S. João"}

def get_menu_pdf(school):
    url = "https://sigarra.up.pt/sasup/pt/web_base.gera_pagina?P_pagina=265689"
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="lxml")
    
    divs = soup.find_all("ul", {"class": "lista"})
    
    schools = {}
    
    for div in divs:        
        links = div.find_all("a")
        
        for link in links:
            schools[link.text] = "https://sigarra.up.pt/sasup/pt/" + link.get("href")
       
    file = requests.get(schools[schools_names[school]])
    open("menu.pdf", "wb").write(file.content)
    