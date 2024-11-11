income=45000
tempIncome=income-20000
tax1=tax2=0

if (income>10000 & income<=20000):
    tax1=10000*(10/100)

if(income>20000 & tempIncome>0):
    
    tax2=tempIncome*(20/100)

print("Total Income Tax =",tax1+tax2)
