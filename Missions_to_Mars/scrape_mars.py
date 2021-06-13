# Set environment

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask instance
app = Flask(__name__)

# Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    mars_data = mongo.db.mars.find_one()
    # Return template and data
    return render_template("index.html", mars_dict=mars_data)
