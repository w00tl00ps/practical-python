# pcost.py
#
# Exercise 1.27
import csv
import sys
import report
import stock


def portfolio_cost(filename):

  #total_cost = 0
  #s = ''

  #f = open(filename)
  #rows = csv.reader(f)
  
  #header = next(rows)
  
  #for i, row in enumerate(rows, start=1):
  #  record = dict( zip(header, row) )
  #  try:
  #    total_cost += float(record['shares']) * float(record['price'])
  #  except ValueError:
  #    print(f'Bad row: {i} Couldn\'t parse: {row}')
  #  
  #f.close()
  
  #Use report.py functions
  portfolio = report.read_portfolio(filename)
  #print(portfolio)
  #total_cost = 0
  #for row in portfolio:
  #  total_cost += row['shares']*row['price']
    
  return sum( [ s.cost() for s in portfolio ] )
  
def main(argv):
  if len(sys.argv) != 2:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
  print( portfolio_cost(argv[1]) )
  
  return
 

if __name__ == '__main__':
    import sys
    main(sys.argv)

'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('System Arguments', sys.argv)

cost = portfolio_cost(filename)
print('Total cost:', cost)  
'''  
"""
def portfolio_cost(filename):

  total_cost = 0
  s = ''

  f = open(filename,'rt')
  header = f.readline()
  for line in f:
    s = line.strip('\n').split(',')
    print(s)
    try:
      shares = float(s[1])
      total_cost +=  shares * float(s[2])
    except ValueError:
      print("Couldn't parse", line)
      
    
  print(total_cost)
    
  f.close()

"""