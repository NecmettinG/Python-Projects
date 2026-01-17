from fasthtml.common import *

items = ["Apple", "Banana", "Cherry"]

app = FastHTML()

@app.route("/")
def index():
    return Ul(*[Li(item) for item in items])

serve()