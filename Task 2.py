#Write a program to calculate the electricity bill based on the following conditions:


units=int(input("Enter the number of units consumed: "))
if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+((units-100)*7)
else:
    bill=(100*5)+(100*7)+((units-200)*10)
print("Electricity Bill = ₹",bill)



#discount calculation:


amount=float(input("Enter purchase amount: "))
if amount>=5000:
    discount=amount*20/100
elif amount>=2000:
    discount=amount*10/100
else:
    discount=0
finalamount=amount-discount
print("Original Amount = ₹",amount)
print("Discount Amount = ₹",discount)
print("Final Payable Amount = ₹",finalamount)

#bank loan:

age=int(input("Enter age: "))
salary=float(input("Enter monthly salary: "))
creditscore = int(input("Enter credit score: "))
if age>=21 and age<=60 and salary>=30000:
    if creditscore>=750:
        print("Loan Approved")
    elif creditscore>=650:
        print("Loan Approved with Guarantor")
    else:
        print("Loan Rejected (Low Credit Score)")
else:
    print("Loan Rejected (Age or Salary Criteria Not Met)")