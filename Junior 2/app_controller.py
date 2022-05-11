
from flask import Flask, request, render_template, jsonify
from junior_model import store_in_dictionary, load, save_dictionary, clear_dictionary
from junior_model import dictionary, get_dictionary

import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)


@app.route('/')
def home():
    load()
    return render_template('hem.html')


@app.route('/vattenkonsumtion')
def vattenkonsumtion(): # vi kan stoppa in en lista (från databas) som en parameter
   list = [1,2,3,4,5,6,7]
   df = pd.DataFrame({
      'Veckodag': ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag',
      'Lördag', 'Söndag'],
      'Vatten i dl': list,
      'månad': ['Måndag', 'Måndag', 'Måndag', 'Tisdag', 'Tisdag', 'Tisdag', 'Tisdag']
   })
   fig = px.bar(df, x='Veckodag', y='Vatten i dl', color='månad',
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('vattenkonsumtion.html', graphJSON=graphJSON)


@app.route('/temperatur')
def temperatur():
   df = pd.DataFrame({
      'Veckodag': ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag',
      'Lördag'],
      'Temperatur': [4, 1, 2, 2, 4, 5],
      'månad': ['Måndag', 'Måndag', 'Måndag', 'Tisdag', 'Tisdag', 'Tisdag']
   })
   fig = px.bar(df, x='Veckodag', y='Temperatur', barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('temperatur.html', graphJSON=graphJSON)


@app.route('/antalvattningar')
def antalvattningar():
   df = pd.DataFrame({
      'Veckodag': ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag',
      'Lördag'],
      'Antal vattningar': [1, 5, 1, 4, 5, 3],
      'månad': ['Måndag', 'Måndag', 'Måndag', 'Tisdag', 'Tisdag', 'Tisdag']
   })
   fig = px.bar(df, x='Veckodag', y='Antal vattningar', color='månad',
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('antalvattningar.html', graphJSON=graphJSON)


@app.route('/bevattning')
def bevattning():
    load()
    return render_template('bevattning.html')




if __name__ == '__main__':
    app.run(debug=True,  port=8080)
