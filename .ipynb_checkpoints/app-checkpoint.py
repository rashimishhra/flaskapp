from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_excel("cladatabase.xlsx")

@app.route("/")
def home():
    return "<h1>Welcome to the CLA Database</h1>"

@app.route("/cladatabase")
def loans_list():
    loans = df[:20].to_dict('records')
    return render_template('cladatabase.html', loans=loans)

@app.route("/cladatabase/<int:BU_ID>")
def loan_details(BU_ID):
    matching_loans = df[df['BU_ID'] == BU_ID].to_dict('records')
    if matching_loans:
        return render_template('loan.html', loan=matching_loans[0])
    else:
        return "<h1>Loan not found!</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)