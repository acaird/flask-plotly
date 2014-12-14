# To build it:
#       docker build -t "acaird/flaskly:test" .
# To start it:
#       docker run -t -d -i -p 5000:80 acaird/flaskly:test
# Base this on RedHat(ish), because that's what CAEN uses
FROM centos:centos6
MAINTAINER Andrew Caird "acaird@umich.edu"
# Apply all the updates
RUN yum update -y
# Install Apache and mod_wsgi for our Flask app
RUN yum install httpd mod_wsgi -y
# Get the new packages and python27
RUN yum install centos-release-SCL -y
RUN yum install python27 -y
# Install pip then use it to install Flask and its dependancies
RUN (. /opt/rh/python27/enable && easy_install-2.7 pip && pip install flask && pip install plotly)
RUN (. /opt/rh/python27/enable && pip install OrderedDict && pip install --upgrade simplejson)
# Copy in our flask-virthost config file
COPY webserver/flask-virthost.conf /etc/httpd/conf.d/
# Copy in our WSGI file
COPY webserver/flaskly.wsgi /var/www/flaskly/
# Copy in sysconfig/httpd that specifies foreground mode for httpd
COPY webserver/sysconfig-httpd /etc/sysconfig/httpd
# Copy in our flask app and templates
ADD flask-plotly.py /var/www/flaskly/flaskPlotly.py
# Copy our plotly credentials file
COPY plotly-creds.sec /var/lib/
# Export our favorite port 5000
# EXPOSE 5000
#
CMD /etc/init.d/httpd start
# CMD /bin/bash -l
