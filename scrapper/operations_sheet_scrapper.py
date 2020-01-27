import pandas as pd
from model.financial_operation import FinancialOperation


class OperationsSheetFlavor:
    @staticmethod
    def read_xls(filename):
        return pd.read_excel(filename, spreadsheet='operacoes-comuns', header=0, engine="xlrd")

    def create_financial_op(self, line):
        if (line[1].strip()[-1] == 'F'):
            asset_name = line[1][0:-1]
        else:
            asset_name = line[1]

        if (not line[3]):
            op_type = 'C'
            price = line[4]
            quantity = line[2]
        else:
            op_type = 'V'
            price = line[5]
            quantity = line[3]
        return FinancialOperation(op_type, asset_name, quantity, price)
