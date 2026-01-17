from fasthtml.common import *

app = FastHTML()

count = 0

@app.route("/")
def index():
    return Div(
        P(f"Count: {count}", id="counter"),
        Button("Increment", hx_get="/increment", hx_target="#counter")
    )

@app.route("/increment")
def increment():
    global count
    count += 1
    return P(f"Count: {count}")

serve()