# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter2=',', silence_errors=False ):
  '''
  Parse a CSV file into a list of records
  '''
  records = []

  #Raise error if no headers exist and header selection was specified
  if select and has_headers==False:
    raise RuntimeError('select argument requires column headers')
    
  
  #with open(filename) as f:
  rows = csv.reader(filename, delimiter=delimiter2)
  
  ##########################################
  # Read the file headers, if present
  if has_headers:
    headers = next(rows)
    #print(headers)
    
    indices = []
    modified_headers = []
    for counter, col in enumerate(headers):
      try:
        if col in select:
          indices.append(counter)
          modified_headers.append(headers[counter]) #print(modified_headers)
      except TypeError:
        indices.append(counter)
        modified_headers.append(headers[counter])
    
    rowCount = 1
    
    #
    # Create a list of dicts from each row
    #
    for row in rows:
        if not row:    # Skip rows with no data
            continue
        
        try:
          #Handle type casting if specified
          if types:
            modified_row = [ types[i](row[i]) for i in indices ]
          else:
            modified_row = [ (row[i]) for i in indices ]
        except ValueError as e:
          if not silence_errors:
            #print('Error processing row ', rowCount, row)
            log.warning("Row %d: Couldn't convert %s", rowCount, row)
            log.debug("Row %d: Reason %s", rowCount, e)
          continue  
 
        record = dict(zip(modified_headers, modified_row))
        records.append(record)
        rowCount += 1
        
  elif not has_headers:
    for row in rows:
      if not row:    # Skip rows with no data
        continue     
      record = tuple(row)
      records.append(record)
  return records #list of dicts





#
# Test function
#  
'''
with open('Data/portfolio.csv') as f:
  portfolio = parse_csv(f)

#portfolio = parse_csv('Data/portfolio.csv', select = ['name', 'shares'])
print(portfolio)

import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
  port = parse_csv(file, types=[str,int,float])
  
print(port)

port = parse_csv('Data/portfolio.csv', types=[str,int,float])
print(port)

'''

'''

prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
print('Portfolio 1')
print(portfolio)
print('Prices')
print(prices)

portfolio2 = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter2=' ')
print('Portfolio2')
print(portfolio2)

prices2 = parse_csv('Data/missing.csv', types=[str, int, float], silence_errors=True)
'''