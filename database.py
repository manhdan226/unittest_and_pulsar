import boto3 

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")

def show_all_table(table):
    scanResponse = table.scan(TableName='tracking_id')
    items = scanResponse['Items']
    print('Scan all items in datatable: ')
    for item in items:
        print(item)

def create_table():
    table = dynamodb.create_table(
    TableName='tracking_data',
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

    table.meta.client.get_waiter('table_exists').wait(TableName='tracking_data')
    print("Done!")

def delete_table(table):
    table.delete()

if __name__ == "__main__":
    table = dynamodb.Table('tracking_data')
    #create_table()
    #show_all_table(table)
    #delete_table(table)
        