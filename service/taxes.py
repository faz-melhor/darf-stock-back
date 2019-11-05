from itertools import groupby

class TaxCalculator:
    @staticmethod
    def calculate_tax(financial_operations):
        grouped = [list(g) for k, g in groupby(financial_operations, lambda fo: fo.asset_name)]
        print(grouped)
        return financial_operations

