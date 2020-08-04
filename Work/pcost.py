# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):

  total_cost = 0
  s = ''

  f = open(filename,'rt')
  header = f.readline()
  for line in f:
    s = line.strip('\n').split(',')
    print(s)
    try:
      total_cost +=  float(s[1]) * float(s[2])
    except ValueError:
      print("Couldn't parse", line)
      
    
  print(total_cost)
    
  f.close()

