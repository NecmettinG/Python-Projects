

from fasthtml.common import *
import json

app = FastHTML()

@app.route("/data")
def data():
    response_data = {"message": "Hello, JSON!"}
    return json.dumps(response_data)

serve()