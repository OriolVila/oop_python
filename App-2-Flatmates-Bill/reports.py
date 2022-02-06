import webbrowser
import fpdf
import os
from filestack import Client


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    such as their names, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2)) + " euros"
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2)) + " euros"

        pdf = fpdf.FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        #Ad icon 
        pdf.image("files/house.png", w=30, h=30)

        #Add title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Bill Report", border=0, align="C", ln=1)

        #Insert Period label
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert name and amount flatmate1
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        #Insert name and amount flatmate1
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        #Save bill.pdf
        pdf.output(f"files/{self.filename}")

        #Alternative way to change directory
        os.chdir("files")
        webbrowser.open(self.filename)

class FileSharer(PdfReport):

    def __init__(self, filepath, api_key='AT3uSA5GQRkuYauEdi84rz'):
        self.filepath = filepath
        self.api_key = api_key
    
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url