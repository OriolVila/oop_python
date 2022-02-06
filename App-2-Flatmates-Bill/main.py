from flat import Bill, Flatmate
from reports import FileSharer, PdfReport

#Build command line interface
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is your flatmate's name? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))


pdf_report=PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())

#the_bill = Bill(amount = 120, period = "April 2021")
#john = Flatmate(name = "John", days_in_house = 20)
#marry = Flatmate(name = "Marry", days_in_house= 25)

#print("John pays: ", john.pays(bill = the_bill, flatmate2=marry))
#print("Marry pays: ", marry.pays(bill = the_bill, flatmate2=john))

#python -m pip install fpdf

#pdf_report=PdfReport(filename="Report1.pdf")
#pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)

