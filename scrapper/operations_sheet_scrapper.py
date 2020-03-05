import pandas as pd
from model.financial_operation import FinancialOperation
import datetime

class OperationsSheetFlavor:
    @staticmethod
    def read_xls(filename):
        return pd.read_excel(filename, spreadsheet='operacoes', header=0, engine="xlrd")

    def create_financial_op(self, line):
        if (line[1].strip()[-1] == 'F'):
            asset_name = line[1][0:-1]
        else:
            asset_name = line[1]

        op_type = line[4]
        price = line[3]
        quantity = line[2]
        date = line[0].to_pydatetime()

        return FinancialOperation(op_type, asset_name, quantity, price, date)
