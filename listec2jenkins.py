import boto3

region='ap-south-1'
access_key='AKIAJHGSTG7AQQ2XDMMQ'
secret_key='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'

listec2 = boto3.client('ec2',region_name=region,
	aws_access_key_id=access_key,
	aws_secret_access_key=secret_key)

output = listec2.describe_instances()
for printid in output['Reservations']:
    for printid2 in printid['Instances']:
        for printid3 in printid2['Tags']:
            print((printid2['InstanceId']),
                  (printid2['InstanceType']),
                  (printid2['LaunchTime']),
                  (printid2['State']['Name']),
                  (printid3['Value']))
