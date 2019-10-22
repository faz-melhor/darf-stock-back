import tabula

filename = '../samples/xp-1.pdf'
multiple_tables = tabula.read_pdf(filename, lattice=True, multiple_tables=True)
print(multiple_tables[2][5])