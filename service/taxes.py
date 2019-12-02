from itertools import groupby


class TaxCalculator:
    @staticmethod
    def calculate_tax(financial_operations):
        financial_operations.sort_values(inplace=True, kind='mergesort')
        grouped = [list(g) for k, g in groupby(financial_operations, lambda fo: fo.asset_name)]
        print(grouped)
        x = [TaxCalculator.calculate_balance(fo) for fo in grouped]
        return grouped

    @staticmethod
    def calculate_balance(asset_financial_operations):

        # buying_summary = TaxCalculator.filter_and_sum(asset_financial_operations)
        # average_buying_price = buying_summary["price"]/buying_summary["total_quantity"]
        # selling_summary = TaxCalculator.filter_and_sum(asset_financial_operations, 'V')
        # total_balance = sells_balance - buys_balance
        for paper in asset_financial_operations:
            average_price = dict()
            profit_loss = []
            print(type(paper))
        #     for operation in paper:
        #         if operation.op_type == "C":
        #             average_price["quantity"] += operation.quantity
        #             average_price["total_price"] += operation.total_price
        #             average_price["average"] = average_price["total_price"]/average_price["quantity"]
        #         elif operation.op_type == "V":
        #             profit_loss.append(operation.total_price - (average_price["average"] * operation.quantity))
        #             average_price["quantity"] -= operation.quantity
        #             average_price["total_price"] = average_price["quantity"] * average_price["average"]
        # print(profit_loss)
        # return profit_loss

    @staticmethod
    def filter_and_sum(asset_financial_operations, search_filter='C'):
        operations = filter(lambda fo: fo.op_type == search_filter, asset_financial_operations)
        summary = {"price": sum(op.total_price() for op in operations),
                   "total_quantity": sum(op.quantity for op in operations)}
        return summary
