import Flask
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Database set-up
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
measurement = Base.classes.measurement
station = Base.classes.station


app = Flask(__name__)

@app.route("/")
def home():
    print ("server build")
    return (
        f"Available route list:"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def names():
    session=Session(engine)

    precipitation = session.query( measurement.date, measurement.prcp).\
    filter(measurement.date > '2016-08-23').\
    order_by(measurement.date).all()
    session.close()

    precipitation_js = list(np.ravel(precipitation))
    return jsonify(precipitation_js)

@app.route("/api/v1.0/stations")
def names():
    session = Session(engine)
    stations_list = session.query(measurement.station, func.sum(measurement.id)).\
    group_by(measurement.station).\
    order_by(func.sum(measurement.id).desc()).all()
    session.close()

    stations_list_js = list(np.ravel(stations_list))
    return jsonify(stations_list_js)

@app.route("/api/v1.0/tobs")
def names():
    session = Session(engine)
    temperature = session.query(measurement.tobs).\
    filter(measurement.station == 'USC00516128', measurement.date > '2016-08-23').\
    order_by(measurement.date.desc()).all()
    session.close()

    temperature_js = list(np.ravel(temperature))
    return jsonify(temperature_js)

@app.route("/api/v1.0/<start>")
def names():
    session = Session(engine)
    temp_max_min_avg = session.query(func.min (measurement.tobs), func.max (measurement.tobs),func.avg (measurement.tobs)).\
    filter(measurement.station == 'USC00516128',measurement.date > '2016-08-23').\
    order_by(func.max(measurement.tobs).desc()).first()
    session.close()

    temp_max_min_avg_js = list(np.ravel(temp_max_min_avg))
    return jsonify(temp_max_min_avg_js)

@app.route("/api/v1.0/<start>/<end>")
def names():
    session = Session(engine)
    temp_max_min_avg = session.query(func.min (measurement.tobs), func.max (measurement.tobs),func.avg (measurement.tobs)).\
    filter(measurement.station == 'USC00516128',measurement.date > '2016-08-23', measurement.date < '2017-08-23').\
    order_by(func.max(measurement.tobs).desc()).first()
    session.close()

    temp_max_min_avg_js = list(np.ravel(temp_max_min_avg))
    return jsonify(temp_max_min_avg_js)
if __name__ == '__main__':
    app.run(debug=True)