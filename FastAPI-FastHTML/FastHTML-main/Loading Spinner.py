from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Div(
        P("Loading..."),
        Div(id="content"),
        Button("Load Data", hx_get="/data", hx_target="#content")
    )

@app.route("/data")
def data():
    return P("Data loaded successfully!")

serve()