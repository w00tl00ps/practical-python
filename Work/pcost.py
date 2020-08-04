# pcost.py
#
# Exercise 1.27
total_cost = 0
s = ''

f = open('Data/portfolio.csv','rt')
header = f.readline()
for line in f:
  s = line.strip('\n').split(',')
  print(s)
  total_cost +=  float(s[1]) * float(s[2])
  
print(total_cost)
  
f.close()
