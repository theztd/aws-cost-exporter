try:
    import boto3


except ImportError as err:
    print(err)
    print("...")
    print("Missing requiremens please run pip3 install -r requirements.txt and try it again")
    exit(1)


class AWS_CostExporter():
    def __init__(self, access_key_id, secret_access_key, region) -> None:
        try:
            self._cost_explorer = boto3.client('ce',
                region_name=region,
                aws_access_key_id=access_key_id, 
                aws_secret_access_key=secret_access_key
            )
        
        except IOError as err:
            print(err)
            print("...")
            print("Please chack accaee policy in AWS IAM. Working example of IAM policy is in README.md")
            exit(1)


    def getMetricsGroupByTags(self, date_start, date_end, tag_name):
        result = self._cost_explorer.get_cost_and_usage(
            TimePeriod={
                'Start': date_start,
                'End': date_end
            },
            Granularity='DAILY',
            Metrics=['BlendedCost'],
            GroupBy=[
                {
                    'Type': 'TAG',
                    'Key': tag_name
                },
            ]
        )['ResultsByTime'][0]['Groups']

        return result