
from fasthtml.common import *
import requests

app = FastHTML()

@app.route("/")
def index():
    return Button("Fetch Data", hx_get="/fetch")

@app.route("/fetch")
def fetch_data():
    response = requests.get('https://api.example.com/data')
    return Div(response.text)

serve()
