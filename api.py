import numpy as np
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import wrapper
from shapely.geometry import Point
from shapely_geojson import dumps, Feature, FeatureCollection

app = Flask(__name__)
cors = CORS(app)


@app.route('/geojson-features', methods=['GET'])
def get_all_points():
    eff, lats, lons, m = wrapper.get_monthly()
    data = []
    i = 0
    for lo in lons:
        j = 0
        for la in lats:
            data.append({'lat': float(la), 'lng': float(lo), 'efficiency': float(eff[j][i])})
            j += 1
        i += 1
    
    # feature_collection = FeatureCollection(features)
    
    # return(dumps(feature_collection, indent=2))
    resp = {'max': float(m), 'data': data}
    return(jsonify(resp))

    
    # return({'empty':'empty'})

@app.route('/')
def main():
    return render_template('index.html')

app.run()