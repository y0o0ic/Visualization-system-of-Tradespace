# Visualization-system-of-Tradespace
Visualization system of trade space analysis for MITsdm maritime project

## install
make an enviroment by pyenv

```pyenv versions
pyenv virtualenv 3.6.6 dash
pyenv local 3.6.6/envs/dash
pip install -r requirements.txt
```

## deploy

firstly,

in app.py, change host and port.
    app.run_server(debug=True, host='0.0.0.0', port='80')

secondly, build docker

```
docker build -t dash-trade-space .
docker run -it --rm -p 7625:80 dash-trade-space
```

check http://localhost:7625/

next, push docker image to azure hub. 

```
az login
docker login <azure repository container url>
docker build -t dash-trade-space .
docker tag dash-trade-space <azure repository container url>/dash-trade-space:latest
docker push <azure repository container url>/dash-trade-space:latest
```

if you can't use az comamnd,```brew update && brew install azure-cli```

Finally, On portal.azure, deploy WebApp using registerd container.
