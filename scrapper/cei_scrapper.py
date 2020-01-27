import pandas as pd
from model.financial_operation import FinancialOperation

class CEIFlavor:
    @staticmethod
    def read_xls(filename):
        sheet = pd.read_excel(filename, spreadsheet = 'Ana', skiprows=10, header=0, usecols="B,D,E,G,I,J", engine="xlrd")
        first_row_with_all_NaN = sheet[sheet.isnull().all(axis=1) == True].index.tolist()[0]
        filtered_sheet = sheet.loc[0:first_row_with_all_NaN-1]
        return filtered_sheet
       
    def create_financial_op(self, line):
        if(line[2].strip() == 'Merc. Fracionário'):
            line[3] = line[3][0:-1]
        return FinancialOperation(line[1].strip().upper(), line[3], line[4], line[5])