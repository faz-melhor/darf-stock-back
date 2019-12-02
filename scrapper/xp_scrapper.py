import pandas as pd
import tabula
from model.financial_operation import FinancialOperation


class XPFlavor:

    @staticmethod
    def read_pdf(self, file):
        filename = file
        multiple_tables = tabula.read_pdf(filename, 
                                          stream=True, 
                                          guess=False, 
                                          multiple_tables=True, 
                                          area=(30,1,50,100), 
                                          relative_area=True)
        print(multiple_tables)
        return multiple_tables[0]
        # 1 - Op_type
        # 3 - Name
        # 6 - Quantidade
        # 7 - preco
        # print(multiple_tables[0][7])
    def read_test(self): 
        dados = [['C','AES TIETE E',200,10.0],
                 ['C','ACAO DO DARIO',10,20.0],
                 ['V','AES TIETE E',180,13.0],
                 ['C','AES TIETE E',150,12.0],
                 ['C','AES TIETE E',100,13.0],
                 ['V','AES TIETE E',200,10.0],
                 ['C','AES TIETE E',130,10.0],
                 ['V','AES TIETE E',200,10.0]]
        return pd.DataFrame(dados, columns = ['0', '1', '2', '3'])
        

    def create_financial_op(self, line):
        # return FinancialOperation(line[1], line[3], line[6], line[7])
        return FinancialOperation(line[0],line[1],line[2],line[3])
