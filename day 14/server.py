from flask import Flask

from logger import trigger_log_save
from scrape import run as scrape_runner

app=Flask(__name__)
# http://localhost:8000/
@app.route("/",methods=['GET'])
def hello_world():
    # run other code here
    return "hello,world.this is Flask"


# http://localhost:8000/abc
@app.route("/abc",methods=['GET'])
def abc_view():
    # run other code here
    return "hello,world.this is abc"

@app.route("/box_scraper",methods=['POST'])
def box_scraper_view():
    # run other code here
    trigger_log_save()
    scrape_runner()
    return {"data":[1,2,3]}
