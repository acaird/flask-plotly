
# Using Plot.ly from Dockerized WSGI Flask Applications

[Plot.ly](http://plot.ly) is a very handy website for presenting
plotted data; the API is really nice and the results are interactive
and look nice.

[Flask](http://flask.pocoo.org/) is a nice lightweight Python web
framework that make simple data presentation on the web almost trivial
and complicated presentation not too difficult.

Obviously, two useful and easy things should be used together; the
files here are an example of using them together.

The one file not included in this repository is the file with my
Plot.ly credentials. To use this, you'll need to make a file called
`plotly-creds.sec` in the same directory as the file
`flask-plotly.ps`; the format of `plotly-creds.sec` is:
```
plotly_username
plotly_APIkey
```
If you don't have a username and API key, you can get them for free at
[plot.ly](http://plot.ly).

If you want to run the local version by typing `python
flask-plotly.py` You will also need to install the Flask and Plot.ly
Python libraries by typing, for example:
```
pip install flask
pip install OrderedDict
pip install --upgrade simplejson
pip install plotly
```

If you only want to run the Dockerized version, those will get
installed during the [Docker](http://docker.io) build process. You'll
need a Docker environment, of course, and there is more on that the
[Docker website](http://docker.io) and once you have that, you can
type:
```
docker build -t "$USER/flaskly:test" .
docker run -t -d -i -p 5000:80 $USER/flaskly:test
```
then browse to http://localhost:5000 to see the web page.

## The "Trick"

The trick to all of this is using the `plotly.plotly.sign_in()`
function in the right place in the code and with the right
credentials. Everything else is sort of standard, unless you've never
used Flask and Plot.ly and Docker before, then those parts are neat,
too.
