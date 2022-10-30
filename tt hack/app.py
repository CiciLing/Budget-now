from flask import Flask, render_template, request, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import requests
import json
import random
from main import accountId, todays_purchases, last_months_purchases
import numpy as np
from pychartjs import BaseChart, ChartType, Color



apiKey = '30e9aa4cdc83efa6616783ed0a2e1b8e'

app = Flask(__name__, template_folder="../templates")
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

class MyBarGraph(BaseChart):

    type = ChartType.Bar

    class data:
        label = "Numbers"
        data = [12, 19, 3, 17, 10]
        backgroundColor = Color.Green

@app.route('/')
def greeting():
    return render_template('tt_hack/greetings.html', username='username')

@app.route('/plot')
def line():
    line_labels=labels
    line_values=values
    return render_template('tt_hack/line.html', title='Your spending tracker', max=17000, labels=line_labels, values=line_values)

@app.route('/line')
def homepage(request):

    NewChart = MyBarGraph()
    NewChart.data.label = "My Favourite Numbers"      # can change data after creation

    ChartJSON = NewChart.get()

    return render_template(request=request,
                  template_name='main/line_try.html',
                  context={"chartJSON": ChartJSON})

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
