import os
import time


#Exercise 6.6
# Modify the code in Exercise 6.5 so that the file-reading 
# is performed by a generator function follow(filename)


""" def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            yield print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')    
 """
# Modify the stock ticker code so that it looks like this:

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

""" 
if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}') 
"""

"""
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

"""