# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
  portfolio = []
  portfolioDict = []
  
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      #record = dict( zip( headers, row) )
      #portfolioDict.append( record )
      portfolioDict.append({'name':row[0], 'shares':int(row[1]), 'price':float(row[2])})
  
  return portfolioDict
  
def read_prices(filename):
  priceDict = {}
  
  f = open(filename,'r')
  rows = csv.reader(f)
  for row in rows:
    try:
      #stockDict = {row[0]:float(row[1])}
      priceDict[row[0]] = float(row[1])
    except IndexError:
      print('IndexError: ', row)
  f.close()
  
  return priceDict

def make_report(portfolio, prices):
  report = []
  for x in portfolio:
    name = x['name']
    shares = int( x['shares'] )
    price = prices[name]
    change = price - float( x['price'] )
    line = (name, shares, price, change)
    report.append(line)
    
  return report

def print_report(report):
  '''
  Prints a formatted report generated by make_report.
  '''
  #pprint(report)
  headers = ('Name', 'Shares', 'Price', 'Change')
  print('%10s %10s %10s %10s' % headers)
  print( ('-' * 10 + ' ') * len(headers))
  for name, shares, price, change in report:
    price = '$' + str( round(price, 2))
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    #print('%10s %10d %10.2f %10.2f' % r)
  return

def portfolio_report(portfolio_filename: str, prices_filename: str):
  '''
  Package everything together to generate report.
  '''
  prices = read_prices(prices_filename)
  portfolio = read_portfolio(portfolio_filename)
  report = make_report(portfolio, prices)
  print_report(report)
  return




portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

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

