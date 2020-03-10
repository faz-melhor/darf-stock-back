from scrapper.cei_scrapper import CEIFlavor
from scrapper.operations_sheet_scrapper import OperationsSheetFlavor
from service.taxes import TaxCalculator

if __name__ == "__main__":
    
    file = 'samples2/operacoes.xls'
    
    # cei = CEIFlavor()
    operations_sheet = OperationsSheetFlavor()
    df = operations_sheet.read_xls(file)
    financial_operations = df.apply(operations_sheet.create_financial_op, axis=1)
    total_tax = TaxCalculator.process_financial_operations(financial_operations)

    for month in total_tax:
        print(f'No mês: {month["date"].strftime("%B")} houveram {month["sell"]}r$ em vendas. E é necessário pagar {month["tax"]}R$ em impostos')
    #print(total_tax)
