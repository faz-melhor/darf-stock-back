from scrapper.cei_scrapper import CEIFlavor
from scrapper.operations_sheet_scrapper import OperationsSheetFlavor
from service.taxes import TaxCalculator

if __name__ == "__main__":
    
    file = 'samples2/operacoes.xls'
    
    # cei = CEIFlavor()
    operations_sheet = OperationsSheetFlavor()
    df = operations_sheet.read_xls(file)
    financial_operations = df.apply(operations_sheet.create_financial_op, axis=1)
    total_tax = TaxCalculator.calculate_tax(financial_operations)
    print(total_tax)
