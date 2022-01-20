# Prometheus AWS Cost Exporter

Tiny application extracting AWS costs per day in USD grouped by tag.




## Run

There are many ways how to use this script, the most clean is to run it as a script

```
export AWS_ACCESS_KEY_ID='---YOUR-ID---'
export AWS_SECRET_ACCESS_KEY='---YOUR-SECRET---' 

cd src

./main.py 1> /tmp/metrics/aws_cost_explorer.prom 
```



But I recomend to run it as a [nomad job](https://nomadproject.io). The [example definition](./deploy.nomad) is part of the repository



## Develop

```
python -m venv exporter
source exporter/bin/activate
pip3 install -r requirements.txt

```

