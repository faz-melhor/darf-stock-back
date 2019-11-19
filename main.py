from scrapper.xp_scrapper import XPFlavor
from service.taxes import TaxCalculator

if __name__ == "__main__":
    file = 'samples/xp-2.pdf'
    # print (sys.path)
    xp = XPFlavor()
    # data_matrix = xp.read_pdf(file)
    # xp.read_test()
    data_matrix =xp.read_test()
    lines = data_matrix.apply(xp.create_financial_op, axis=1)
    TaxCalculator.calculate_tax(lines)
    #print(lines)
