from flask import Flask

app = Flask(__name__)

# load env vars
from dotenv import load_dotenv

load_dotenv(verbose=True)


@app.route("/")
@app.route("/index")
def index():
    return "Everything is working !"
