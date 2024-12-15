from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

file_path = os.path.join(os.path.dirname(__file__), 'cla.csv')

df = pd.read_csv(csv_path)

PER_PAGE = 20

@app.route("/")
def home():
    return "<h1>This is CLA Database</h1>"

@app.route("/cla")
def loans_list():
    try:
        current_page = int(request.args.get('page', 1))
        if current_page < 1:
            raise ValueError
    except ValueError:
        return "Invalid page number. Must be a positive integer.", 400

    start = (current_page - 1) * PER_PAGE
    end = start + PER_PAGE

    loans = df[start:end].to_dict('records')

    if not loans:
        return "No loans found for this page.", 404

    total_pages = (len(df) + PER_PAGE - 1) // PER_PAGE  
    pagination = {
        "current_page": current_page,
        "total_pages": total_pages,
        "has_next": current_page < total_pages,
        "has_prev": current_page > 1,
    }

    return render_template('cla.html', loans=loans, pagination=pagination)

@app.route("/cla/<BU_ID>")
def loans_details(BU_ID):
    matching_rows = df[df['BU_ID'].astype(str) == str(BU_ID)]

    if not matching_rows.empty:
        loan = matching_rows.to_dict('records')[0]
        return render_template('loans.html', loan=loan)
    else:
        return f"BU_ID {BU_ID} not found", 404

if __name__ == '__main__':
    app.run(debug=True)
