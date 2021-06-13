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



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    print(mars_data)
    
    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)