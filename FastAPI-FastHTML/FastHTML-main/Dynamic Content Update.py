
from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Div(
        P("Current time:", id="time"),
        Button("Refresh Time", hx_get="/time", hx_target="#time")
    )

@app.route("/time")
def time():
    from datetime import datetime
    return P(datetime.now().strftime("%H:%M:%S"))

serve()
