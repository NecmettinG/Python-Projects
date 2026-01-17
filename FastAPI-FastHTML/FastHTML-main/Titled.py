from fasthtml.common import *

app, rt = fast_app(live=True)

@rt('/')
def get():
    return Titled("FastHTML", Div(
        H1('Hello Dr.Mohammed'),
        P('This is a paragraph')
    ))
serve()

