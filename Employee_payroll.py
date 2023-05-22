#this program is a gift to you my friend..lol
Tax_rate1=10/100
Tax_rate2=5/100
def Married_emp(tax_type):
    Gross_pay = Employee_rate*Employee_hours
    print("Gross Pay = ",Gross_pay)
    Deduct = Gross_pay*tax_type
    print("Deductions total = ",Deduct)
    Net_pay = Gross_pay-Deduct
    print("Your Net Pay = ")

def Single_emp(tax_type):
    Gross_pay = Employee_rate*Employee_hours
    print("Gross Pay = ",Gross_pay)
    Deduct = Gross_pay*tax_type
    print("Deductions total = ",Deduct)
    Net_pay = Gross_pay-Deduct
    print("Your Net Pay = ",Net_pay)

Employee_name=input("Please Enter Your name: ")
Employee_rate=eval(input("What your rate (Employee rate): "))
Employee_status=input("S(Single) or M(Married)?: ")
Employee_hours=eval(input("What are the number of hours recorded at work: "))
if (Employee_status=="M"):
    Married_emp(Tax_rate2)

if (Employee_status=="S"):
    Single_emp(Tax_rate1)
