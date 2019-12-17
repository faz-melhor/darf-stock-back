import pandas as pd
import tabula
import locale
from model.financial_operation import FinancialOperation


class XPFlavor:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    @staticmethod
    def read_pdf(file):
        filename = file
        multiple_tables = tabula.read_pdf(filename, 
                                          stream=True, 
                                          guess=False, 
                                          multiple_tables=True, 
                                          area=(30,1,50,100), 
                                          relative_area=True,pages='all')
        print(multiple_tables)
        return multiple_tables[0]
        # 1 - Op_type
        # 3 - Name
        # 6 - Quantidade
        # 7 - preco
        # print(multiple_tables[0][7])
    # def read_test(self):
    #     dados = [['C','AES TIETE E',2000,10.0],
    #              ['V','AES TIETE E',2000,20.0]] 
    #     # dados = [['C','AES TIETE E',2000,10.0],
    #     #          ['C','ACAO DO DARIO',10,20.0],
    #     #          ['V','AES TIETE E',1800,13.0],
    #     #          ['C','AES TIETE E',150,12.0],
    #     #          ['C','AES TIETE E',100,13.0],
    #     #          ['V','AES TIETE E',200,10.0],
    #     #          ['C','AES TIETE E',130,10.0],
    #     #          ['V','AES TIETE E',200,10.0],
    #     #          ['V','ACAO DO DARIO',10,22.0]]
    #     return pd.DataFrame(dados, columns = ['0', '1', '2', '3'])
    
    def read_float_with_comma(self, num):
        _locale_radix = locale.localeconv()['decimal_point']
        if _locale_radix != '.':
            num = num.replace(_locale_radix, ".")
        return float(num)

    def create_financial_op(self, line):
        # print(self.read_float_with_comma(line[7]))
        # print(len(line))
        # print(line)
        if (len(line)==9):
            return FinancialOperation(line[1], line[3], self.read_float_with_comma(line[5]), self.read_float_with_comma(line[6]))
        else:
            return FinancialOperation(line[1], line[3], self.read_float_with_comma(line[6]), self.read_float_with_comma(line[7]))
        