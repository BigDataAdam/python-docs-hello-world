import flask
from flask import request, jsonify
import csv, json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


datasets = {2011: '2011 Stack Overflow Survey Results.csv', 2012: '2012 Stack Overflow Survey Results.csv', 2013: 'demo.csv'}


@app.route('/', methods=['GET'])
def home():
    return '''From this API you can get datasets from the stack overflow survey 
for the years 2011 - 2020. Use /api/v1/datasets and the desired year as parameter.'''





@app.route('/api/v1/datasets', methods=['GET'])
def api_id():
    # Check if an year was provided as part of the URL.

    if 'year' in request.args:
        year = int(request.args['year'])
    else:
        return "Error: No year field provided. Please specify a year."
    
    if year > 2020 or year < 2011:
        return "Error: Data for this year is not available."
    
    file_name = datasets[year] 
    data = {}
    with open(file_name) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for idx, rows in enumerate(csvReader):
            #id = rows['id']
            data[idx] = rows


    return data

#app.run()
