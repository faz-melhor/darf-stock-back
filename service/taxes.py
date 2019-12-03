from itertools import groupby


class TaxCalculator:
    @staticmethod
    def calculate_tax(financial_operations):
        financial_operations.sort_values(inplace=True, kind='mergesort')
        grouped = [list(g) for k, g in groupby(financial_operations, lambda fo: fo.asset_name)]
        # print(grouped)
        x = [TaxCalculator.calculate_p_l(fo) for fo in grouped]
        print (x)
        return grouped

    # calculate profit and loss on a set of paper, operated in a range of time
    @staticmethod
    def calculate_p_l(paper):
        paper_average = {'quantity':0, 'total_price':0,'average':0}
        profit_loss = []
        for operation in paper:
            if operation.op_type == "C":
                paper_average["quantity"] += operation.quantity
                paper_average["total_price"] += operation.total_price()
                paper_average["average"] = paper_average["total_price"]/paper_average["quantity"]
            elif operation.op_type == "V":
                profit_loss.append(operation.total_price() - (paper_average["average"] * operation.quantity))
                paper_average["quantity"] -= operation.quantity
                paper_average["total_price"] = paper_average["quantity"] * paper_average["average"]
        return profit_loss

    @staticmethod
    def filter_and_sum(asset_financial_operations, search_filter='C'):
        operations = filter(lambda fo: fo.op_type == search_filter, asset_financial_operations)
        summary = {"price": sum(op.total_price() for op in operations),
                   "total_quantity": sum(op.quantity for op in operations)}
        return summary
