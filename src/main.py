#!/usr/bin/env python3


from AWS_CostExporter import AWS_CostExporter
from pprint import pprint
from os import getenv
from datetime import datetime, timedelta

if __name__ == '__main__':

    group_by_tag = getenv('AWS_GROUP_BY_TAG', 'project')

    aws = AWS_CostExporter(
            region=getenv('AWS_REGION', 'eu-central-1'),
            access_key_id=getenv('AWS_ACCESS_KEY_ID'),
            secret_access_key=getenv('AWS_SECRET_ACCESS_KEY')
    )

    date_start = datetime.today() - timedelta(days=2)
    date_end = datetime.today() - timedelta(days=1)

    for m in aws.getMetricsGroupByTags(
                    tag_name=group_by_tag, \
                    date_start=date_start.strftime('%Y-%m-%d'), 
                    date_end=date_end.strftime('%Y-%m-%d')
                    ):
	
        _tag = m['Keys'][0].split('$')[1]
        tag = "not-tagged" if _tag == "" else _tag
        # should not be negative
        value = m['Metrics']['BlendedCost']['Amount'].replace("-","")
        
        print(f'aws_daily_cost_per_tag_in_usd{{group_by="{group_by_tag}", tag="{tag}"}} {value}')
