# import pandas as pd
import tabula

class xp_flavor:
    def read_pdf(self,file):
        filename = file
        multiple_tables = tabula.read_pdf(filename, stream=True, guess=False, multiple_tables=True, area=(30,1,50,100), relative_area=True)
        # 3 - Name
        # 6 - Quantidade
        # 7 - preco
        # print(multiple_tables[0])
if __name__ == "__main__":
    file = 'samples/xp-2.pdf'
    
