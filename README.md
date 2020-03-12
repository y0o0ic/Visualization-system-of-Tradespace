# Visualization-system-of-Tradespace
Visualization system of trade space analysis for MITsdm maritime project

## install
make an enviroment by pyenv

'''pyenv versions
pyenv virtualenv 3.6.6 dash
pyenv local 3.6.6/envs/dash
pip install -r requirements.txt'''

## deploy

firstly,

in app.py, change host and port.
    app.run_server(debug=True, host='0.0.0.0', port='80')

secondly,


$ docker build -t dash-azure .
$ docker run -it --rm -p 7625:80 dash-azure

