from fasthtml.common import *

app = FastHTML()

@app.route("/")
def index():
    return Html(
        Body(
            Header(navigation_bar(["Home", "About"])),
            Div("Welcome to the homepage!", id="content")
        )
    )

def navigation_bar(items):
    return Nav(Ul(*[Li(Button(item, hx_get=f"/{item.lower()}")) for item in items]))

@app.route("/about")
def about():
    return Div("This is the About page.")

serve()