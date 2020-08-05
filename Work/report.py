# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
  portfolio = []
  
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      portfolio.append( (row[0], int(row[1]), float(row[2]) ) )
  
  print(portfolio)
  
  return portfolio
  

read_portfolio('Data/portfolio.csv')