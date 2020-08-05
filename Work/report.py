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
      portfolio.append( (row[0], int(row[1]), float(row[2]) ) )
      portfolioDict.append({'name':row[0], 'shares':int(row[1]), 'price':float(row[2])})
  
  portfolioDict
  
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

#
# 
#
prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)
pprint(prices)

costBasis = 0
currentValue = 0


for x in portfolio:
  costBasis += x['price']*x['shares']
  symbol = x['name']
  currentValue += x['shares'] * prices[symbol]
  
print('Cost Basis: ', costBasis)
print('Current Value: ', currentValue)
print('Gain/Loss', round(currentValue - costBasis, 2))