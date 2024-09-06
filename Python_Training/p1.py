
meal = str(input("Whats your favourite food? "))

billamount = 0
tax = 0.0
if meal == "chicken":
    billamount += 40
elif meal == "fries":
    billamount += 12
else:
    billamount = 0
    
if billamount > 15:
    tax = 12.5
else:
    tax = 6
print(billamount)
tax = tax/100
print(tax)
finalamount = billamount *(tax+1)
print(finalamount)
