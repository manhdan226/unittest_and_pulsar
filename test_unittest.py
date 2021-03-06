import boto3 
import unittest
import logging

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")
table = dynamodb.Table('test_api')
logging.basicConfig(level=logging.DEBUG, filename='runtime.log', filemode='w')

def search_item(table):
    scanResponse = table.scan(TableName='test_api')
    item = scanResponse['Items'][0]
    return item
    
class TestAPI(unittest.TestCase):
    def check_format(self):
        item = search_item(table)
        test_id = item['id']
        self.assertIsInstance(test_id,str)
        test_message = item['message']
        self.assertIsInstance(test_id,str)

if __name__ == '__main__':
    while True:
        _count = table.count_item()
        if _count == 1:
            unittest.main()
            item = search_item(table) 
            id = item['id']
            table.delete_item(Key = {'id': id})
        
