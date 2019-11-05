class FinancialOperation:
    
    def __init__(self, op_type, asset_name, quantity, price):
        self.__op_type = op_type
        self.__asset_name = asset_name
        self.__quantity = quantity
        self.__price = price

    @property
    def op_type(self):  
        return self.__op_type

    @property
    def asset_name(self):  
        return self.__asset_name

    @property
    def quantity(self):  
        return self.__quantity

    @property
    def price(self):  
        return self.__price

    def total_price(self):
        return self.__price * self.__quantity
    
    def __str__(self):
        return "OpType: {} - AssetName: {} Quantity: {} - Price: {}".format(self.__op_type, self.__asset_name, 
                                                                            self.__quantity, self.__price)