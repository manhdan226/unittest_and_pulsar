import boto3 

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")


table = dynamodb.create_table(
TableName='test_api',
KeySchema=[
    {
        'AttributeName': 'id',
        'KeyType': 'HASH'
    }
        
],
AttributeDefinitions=[
            {
        'AttributeName': 'id',
        'AttributeType': 'S'
    } 
],
ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}
)

table.meta.client.get_waiter('table_exists').wait(TableName='test_api')
print("Done!")
        