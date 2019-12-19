from openpyxl import load_workbook
from PIL import Image, ImageDraw
from texttable import Texttable

def excel(school):
    result = []
    wb2 = load_workbook(school + ".xlsx")
    
    if (school == "FEUP"):
        ws = wb2["Table 1"]
        
        ws.delete_cols(3, 8) 
        ws.delete_cols(1, 1) # Deletes collumns C to J
        ws.delete_rows(32, 11) 
        ws.move_range("A2:B43", rows = -1) 
             
        counter = 0
        
        dias = ["", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        carne = ["Carne"]
        peixe = ["Peixe"]
        vegetariano= ["Vegetariano"]
    
        for row in ws.values:
            for value in row:
                i = counter % 6       
                
                if value == None:
                    continue
                
                if i == 2 :
                    carne.append(value)
                    
                elif i == 3:
                    peixe.append(value)
                    
                elif i == 5:
                    vegetariano.append(value)
                    
            counter += 1
            
    else:
        ws = wb2["Table 3"]
    
        for row in ws.values:
            for value in row:
                result.append(value.replace("\xa0", ""))
    
        dias = result[0:6]
        carne = result[12:18]
        peixe = result[18:24]
        vegetariano= result[24:31]
    
    t = Texttable()
    t.add_rows([dias, carne, peixe, vegetariano])

    return t.draw()

def image(school, table):
    # let's draw the text we got on an image
    img = Image.new('RGB', (1000, 600), color=(0x3F, 0x3F, 0x3F))
    d = ImageDraw.Draw(img)
    
    # write the text to the created image
    # string_result should contain a string with
    # all the text on the table, line by line (lines
    # separated by '\n')
    d.text((10, 10), table, fill=(0xE3, 0xE3, 0xE3))
    img.save(school + ".png")
    
    # after this you only need to post the image
    # it's a light weight image (easier to search for)
    # seems a lot better than plain text because it doesn't
    # break on different resolutions
