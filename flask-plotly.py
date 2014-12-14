#!/usr/bin/env python

from flask import Flask
# pip install plotly
import plotly.plotly as py
from plotly.graph_objs import *

###### Configuration, read by app.config.from_object ######
LISTEN_IP             = '0.0.0.0'  # 0.0.0.0 for running in Docker
LISTEN_IP             = ''         # set to '' for only localhost
LISTEN_PORT           = 5001
###########################################################

app = Flask(__name__)
app.config.from_object(__name__)

def makeIframeString(data):

    trace1 = Scatter (
        x = data['x'],  y = data['y'],
        fill='tozeroy', fillcolor="red",
        opacity=0.52,   name="Amazing Things"
    )

    layout = Layout(
        title='Amazing Things over time',
        xaxis=XAxis(
            title='My Age',
            titlefont=Font(
                size=18, color='#7f7f7f'
            )
        ),
        yaxis=YAxis(
            title='Number of things I find amazing',
            titlefont=Font(
                size=18, color='#7f7f7f'
            )
        )
    )
    data = Data([trace1])
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='amazing-things', auto_open=False)
    iframe_string = '<iframe id="igraph" style="border:none" src="'
    iframe_string = iframe_string+plot_url+'/550/550" width="100%" height="700"></iframe>'

    return (iframe_string)

def makeData():
    data = {}
    data['x'] = data['y'] = []
    data['x'] = range(43)
    data['y'] = [ i * i * i for i in data['x']]
    return (data)

@app.route('/')
def index():
    """
    Make a simple index.html page
    """
    html = "<h1>Amazing Things</h1>"

    flaskData = makeData()

    iFrameString = makeIframeString(flaskData)

    html = html + "<hr>\n";
    html = html + iFrameString + "\n"
    html = html + "<ht>\n";

    return html

if __name__ == "__main__":

    app.run(host=app.config['LISTEN_IP'],port=app.config['LISTEN_PORT'],debug=True)

    # data = makeData()

    '''
    The file 'plotly-creds.sec' is a text file with your Plot.ly
    credentials in it.  The first line is your username and the
    second line is your secret key.
    '''
    # creds=[]
    # with open("plotly-creds.sec") as f:
    #     creds = [x.strip('\n') for x in f.readlines()]

    # py.sign_in(creds[0], creds[1])

    # urlish = makeIframeString(data)

    # print urlish
