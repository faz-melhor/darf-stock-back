# darf-stock-back

It's the backend of the application the darf generator web application. This app is meant to help stock traders that are bound to pay tributes oblige by Brazilian law nº 11.033/2004.

# Rules of tribute

Individual net profit in stock market operations are tributed if the total value of sells overflows the amount of 20.001,00 R$ in a month. If instead of profit the set of operations in the month turns out to be a loss, said loss can be deducted on the following months of the year.

## How is it done?

Basically, when someone buys something on the stock market a brokerage invoice is generated, the price of the asset being bought and the fees related to the acquisition will be written in it. For the calculation the sum of all fees plus the value paid for the asset is called cost of purchase.

After some time someone decides to sell a portion or all of its shares, the p/l (profit/loss) is calculated by this equation:

*amount-bought \*price-bought-((amount-sold\*price-sold)+((amount-sold/amount-bought)\*buying-fee)+selling-fee)*

If the result is a negative number than the operation ended in loss otherwise it ended in profit, and if all sells in the month should surpass the total value of 20.001,00 this profit should be tributed.

# How the system works?

The user should upload all the brokerage invoice he has, the system will read the invoices and calculate how much tax the user needs to pay.

More information: 
* https://apet.jusbrasil.com.br/noticias/2164112/venda-de-acoes-acima-de-r-20-mil-por-mes-pode-pagar-ir/amp
* http://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2004/Lei/L11033.htm

 Linked repositories: [darf-stock-front](https://github.com/lucasnathan/darf-stock-front)
