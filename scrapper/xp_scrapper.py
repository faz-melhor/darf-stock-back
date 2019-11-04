import pandas as pd
import tabula

filename = 'samples/xp-2.pdf'
multiple_tables = tabula.read_pdf(filename, stream=True, guess=False, multiple_tables=True, area=(30,1,50,100), relative_area=True)

print(multiple_tables) 