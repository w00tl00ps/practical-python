# report.py
#
# Exercise 2.4
import csv
import stock
import tableformat

from fileparse import parse_csv
from portfolio import Portfolio

def read_portfolio(filename):
  portfolio = []
  portfolioDict = []
  stock_list = []
  #Skip old code
  #            '''
  #            with open(filename, 'rt') as f:
  #              rows = csv.reader(f)
  #              headers = next(rows)
  #              for row in rows:
  #                #record = dict( zip( headers, row) )
  #                #portfolioDict.append( record )
  #                portfolioDict.append({'name':row[0], 'shares':int(row[1]), 'price':float(row[2])})
  #                '''
  with open(filename) as f:
    portfolioDict = parse_csv(f, types=[str,int,float])
  
  portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portfolioDict ]
  return Portfolio(portfolio)

  #stock_list = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portfolioDict ]
  #return stock_list
  
  #return portfolioDict
  
def read_prices(filename):
  priceDict = {}
  #Skip old code
  #            '''
  #            f = open(filename,'r')
  #            rows = csv.reader(f)
  #            for row in rows:
  #              try:
  #                #stockDict = {row[0]:float(row[1])}
  #                priceDict[row[0]] = float(row[1])
  #              except IndexError:
  #                print('IndexError: ', row)
  #            f.close()'''
  with open(filename) as f:
    priceDict = dict(parse_csv(f, has_headers=False))
  #print(priceDict)
  return priceDict

def make_report(portfolio, prices):

  report = []
  for s in portfolio:
    name = s.name #x['name']
    shares = s.shares #int( x['shares'] )
    price = float(prices[name])
    change = price - float( s.price) #['price'] )
    
    line = (name, shares, price, change)
    report.append(line)
    
  return report

def print_report(report, formatter):
  '''
  Prints a formatted report generated by make_report.
  '''
  #pprint(report)
  headers = ('Name', 'Shares', 'Price', 'Change')
  formatter.headings(['Name','Shares','Price','Change'])
  
  #print('%10s %10s %10s %10s' % headers)
  #print( ('-' * 10 + ' ') * len(headers))
  
  for name, shares, price, change in report:
    #price = '$' + str( round(price, 2)) ADD DOLLAR SIGN
    rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
    formatter.row(rowdata)
    #print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    #print('%10s %10d %10.2f %10.2f' % r)
  return

def portfolio_report(portfolio_filename: str, prices_filename: str, fmt='txt'):
  '''
  Package everything together to generate report.
  '''
  prices = read_prices(prices_filename)
  portfolio = read_portfolio(portfolio_filename)
  report = make_report(portfolio, prices)
  
  #create formatter and print report
  #formatter = tableformat.TextTableFormatter()
  #formatter = tableformat.CSVTableFormatter()    
  #formatter = tableformat.HTMLTableFormatter()  
  formatter = tableformat.create_formatter(fmt)
  print_report(report, formatter)
  return


def main(argv):
  if len(sys.argv) != 4:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
  portfolio_filename = argv[1]
  prices_filename = argv[2]
  format = argv[3]
  portfolio_report(portfolio_filename, prices_filename, format) #use txt by default but can specify fmt
  return

if __name__ == '__main__':
    import sys
    main(sys.argv)

#portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

"""
costBasis = 0
currentValue = 0

for x in portfolio:
  costBasis += x['price']*x['shares']
  symbol = x['name']
  currentValue += x['shares'] * prices[symbol]
  
print('Cost Basis: ', costBasis)
print('Current Value: ', currentValue)
print('Gain/Loss', round(currentValue - costBasis, 2))
"""

