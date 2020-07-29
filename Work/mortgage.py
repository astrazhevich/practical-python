# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
mon_num = 1
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= mon_num <= extra_payment_end_month:
        p = payment + extra_payment
    else:
        p = payment
    principal = principal * (1+rate/12) - p
    total_paid = total_paid + p
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    print(mon_num, round(total_paid, 2), round(principal, 2))
    mon_num = mon_num + 1    

print(f'Total paid {total_paid:0.2f}')
print(f'Months {mon_num-1}')