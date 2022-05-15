from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)

class HomePage(MethodView):

    def get(selfself):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = billform.days_in_house1.data

        name2 = billform.name2.data
        days_in_house2 = billform.days_in_house2.data

        the_bill = flat.Bill(float(amount), period)
        flatmate1 = flat.Flatmate(name1, float(days_in_house1))
        flatmate2 = flat.Flatmate(name2, float(days_in_house2))

        return render_template('results.html',
                               name1=flatmate1.name,
                               amount1=round(flatmate1.pays(the_bill, flatmate2),2),
                               name2=flatmate2.name,
                               amount2=round(flatmate2.pays(the_bill, flatmate1),2))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="December 2016")

    name1 = StringField("Name: ", default="Alex")
    days_in_house1 = StringField("Days in house: ", default=10)

    name2 = StringField("Name: ", default="John")
    days_in_house2 = StringField("Days in house: ", default=20)

    button = SubmitField("Calculate")

app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill',
                 view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',
                 view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)