
from fasthtml.common import *
import time

app = FastHTML()

countdown_time = 10

@app.route("/")
def index():
    return Div(P(f"Countdown starts now!"), Button("Start Countdown", hx_get="/start"))

@app.route("/start")
def start_countdown():
    global countdown_time
    while countdown_time > 0:
        time.sleep(1)
        countdown_time -= 1
        yield f"<script>document.getElementById('countdown').innerText='{countdown_time}'</script>"
    
serve()