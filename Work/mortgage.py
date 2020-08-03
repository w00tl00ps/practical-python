# mortgage.py
#
# Exercise 1.7
mortgage = 500000
interest = 0.05
monthly_pay = 2684.11
amort = 30
total_paid = 0
month = 0

extra_amount = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while mortgage > 0:
  mortgage = mortgage + mortgage*0.05/12 - monthly_pay
  if extra_payment_start_month <= month < extra_payment_end_month:
    mortgage -= extra_amount
    total_paid += extra_amount
    
  total_paid += monthly_pay
  month += 1
  if mortgage < 0:
    total_paid += mortgage
    mortgage = 0
  print(month, round(total_paid, 2), round(mortgage, 2))
  
print('Total paid', total_paid)
print('Months', month)  