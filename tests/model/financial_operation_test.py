import pytest
from datetime import date

from model.financial_operation import FinancialOperation
from service.taxes import TaxCalculator

def test_must_run():
    finantial = FinancialOperation("C", "DDMO3", 100, 1.00, date.today())
    assert finantial != None

