# importing our tools.
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping

# Set-up Flask.
app = Flask(__name__)

# Telling python how to connect to Mongo using PyMongo.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Setting up our Flask route.
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Adding second route.
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# Telling Flask to run
if __name__ == "__main__":
   app.run()