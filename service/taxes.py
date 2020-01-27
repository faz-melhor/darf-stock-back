from itertools import groupby
import collections, functools, operator 

class TaxCalculator:
    @staticmethod
    def calculate_tax(financial_operations):
        financial_operations.sort_values(inplace=True, kind='mergesort')
        grouped = [list(g) for k, g in groupby(financial_operations, lambda paper: paper.asset_name)]
        profit_loss = [TaxCalculator.calculate_p_l(paper) for paper in grouped]
        total_p_l = sum(pl['p_l'] for pl in profit_loss)
        total_sell = sum(sell['sell'] for sell in profit_loss)
        print(total_sell)
        print(f'Total pl {total_p_l}')
        if (total_sell >= 20001):
            return total_p_l * 0.15
        
        # print(str(total_p_l))
        # print(total_sell)
        # print(str(profit_loss))
        else:
            return 0

    # calculate profit and loss on a set of paper, operated in a range of time
    @staticmethod
    def calculate_p_l(paper):
        paper_average = {'asset_name': paper[0].asset_name, 'quantity':0, 'total_price':0,'average':0}
        profit_loss = {'p_l':0,'sell':0}
        for operation in paper:
            if operation.op_type == "C":
                paper_average["quantity"] += operation.quantity
                paper_average["total_price"] += operation.total_price()
                paper_average["average"] = paper_average["total_price"]/paper_average["quantity"]
            elif operation.op_type == "V":
                profit_loss['p_l'] += (operation.total_price() - (paper_average["average"] * operation.quantity))
                profit_loss['sell'] += operation.total_price()
                paper_average["quantity"] -= operation.quantity
                paper_average["total_price"] = paper_average["quantity"] * paper_average["average"]
        print(paper_average)
        return profit_loss

    @staticmethod
    def filter_and_sum(asset_financial_operations, search_filter='C'):
        operations = filter(lambda fo: fo.op_type == search_filter, asset_financial_operations)
        summary = {"price": sum(op.total_price() for op in operations),
                   "total_quantity": sum(op.quantity for op in operations)}
        return summary
