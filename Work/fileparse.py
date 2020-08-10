# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True ):
  '''
  Parse a CSV file into a list of records
  '''
  records = []
  
  with open(filename) as f:
    rows = csv.reader(f)
    
    # Read the file headers, if present
    if has_headers:
      headers = next(rows)
      print(headers)
      
      indices = []
      modified_headers = []
      for counter, col in enumerate(headers):
        if col in select:
          indices.append(counter)
          modified_headers.append(headers[counter]) #print(modified_headers)
      
      
      
      for row in rows:
          if not row:    # Skip rows with no data
              continue
          
          #Handle type casting if specified
          if types:
            modified_row = [ types[i](row[i]) for i in indices ]
          else:
            modified_row = [ (row[i]) for i in indices ]
          
   
          record = dict(zip(modified_headers, modified_row))
          records.append(record)
    elif not has_headers:
      for row in rows:
        record = tuple(row)
        records.append(record)
  return records #list of dicts
  

portfolio = parse_csv('Data/portfolio.csv', select = ['name', 'shares'])
prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
print(portfolio)
print(prices)