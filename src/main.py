#!/usr/bin/env python3


from AWS_CostExporter import AWS_CostExporter
from pprint import pprint
from os import getenv


if __name__ == '__main__':

    group_by_tag = getenv('AWS_GROUP_BY_TAG', 'project')

    aws = AWS_CostExporter(
            region=getenv('AWS_REGION', 'eu-central-1'),
            access_key_id=getenv('AWS_ACCESS_KEY_ID'),
            secret_access_key=getenv('AWS_SECRET_ACCESS_KEY')
    )

    for m in aws.getMetricsGroupByTags(tag_name=group_by_tag, date_start='2022-01-19', date_end='2022-01-20'):
        tag = m['Keys'][0].split('$')[1]
        if tag != "":
            value = m['Metrics']['BlendedCost']['Amount']
            print(f'aws_daily_cost_per_tag_in_usd{{group_by="{group_by_tag}", tag="{tag}"}} {value}')
