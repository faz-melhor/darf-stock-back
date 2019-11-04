class FinancialOperation:
    
    def __init__(self, op_type, asset_name, quantity, price):
        self.__op_type = op_type
        self.__asset_name = asset_name
        self.__quantity = quantity
        self.__price = price

    def total_price(self):
        return self.__price * self.__quantity
    
    def __str__(self):
        pass