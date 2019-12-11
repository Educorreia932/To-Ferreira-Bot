from PyPDF2 import *

def extract(filename):  
    with open(filename, 'rb') as f:
          pdf = PdfFileReader(f)
          # get the first page
          page = pdf.getPage(1)

          text = page.extractText()
          
          text = str.join(" ", text.splitlines())
          
          text = text.split("SOPA")[1]
          sopa = "🥣 **Sopa:**" + text.split("CARNE")[0] + "\n"
              
          text = text.split("CARNE")[1]
          carne = "🍖 **Carne:**" + text.split("PESCADO")[0] + "\n"
          
          text = text.split("PESCADO")[1]
          pescado = "🐟 **Peixe:**" + text.split("VEGETARIANO")[0] + "\n"
          
          text = text.split("VEGETARIANO")[1]
          vegetariano = "🥦 **Vegetariano:**" + text.split("NOTAS")[0]
          
          teste = vegetariano.split("    ")
          
          for word in teste:
              print(word)

    return sopa + carne + pescado + vegetariano

from openpyxl import load_workbook
from texttable import Texttable

def excel():
    wb2 = load_workbook("output.xlsx")
    
    ws = wb2["Table 3"]
    
    result = []
    
    for row in ws.values:
        for value in row:
            result.append(value.replace("\xa0", ""))
    
    dias = result[0:6]
    carne = result[12:18]
    peixe = result[18:24]
    vegetariano= result[24:31]
    
    t = Texttable()
    t.add_rows([dias, carne, peixe, vegetariano])

    return t.draw()[0:1980]
    
    
    