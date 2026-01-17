from fasthtml.common import *

app, rt = fast_app(live=True) #rt is for routing between addresses.

@rt('/') #Address is http://localhost:5001/
def get():
    return Div(
        H1('Hello Dr. Mohammed this is H1'), #These are headers.
        H2('Hello Dr. Mohammed this is H2 '),
        H3('Hello Dr. Mohammed this is H3'),
        H4('Hello Dr. Mohammed this is H4'),
        H5('Hello Dr. Mohammed this is H5'),
        H6('Hello Dr. Mohammed this is H6'),
     
    )
serve()

