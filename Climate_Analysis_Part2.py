import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Base.classes.keys()
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
         F"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation<br/>")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").all()
    for item in data:
        data = {}
        data["date"]=Measurement.date
        data["prcp"]=Measurement.prcp
    return jsonify(data)


@app.route("/api/v1.0/station")
def names():
    """Return a list of all station names"""
    # Query all stations
    results = session.query(Station.name).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/<start>")

def tobs():
    results = session.query(Measurement.tobs).\
    filter(Measurement.date >= "2016-08-23").\
    filter(Measurement.station == "USC00519281").all()

    temps = list(np.ravel(results))
    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")

def startend(start, end):
    new_start = start.replace(" ", "")
    new_end = end.replace(" ", "")
    results = session.query(func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(]Measurement.date <= end).all()
    new_data = list(np.ravel(results))
    
    return jsonify(new_data)

if __name__ == '__main__':
    app.run(debug=True)
