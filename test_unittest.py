import boto3 
import unittest
import logging

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")
table = dynamodb.Table('test_api')

logging.basicConfig(level=logging.DEBUG, filename='runtime.log', filemode='w')

class TestAPI(unittest.TestCase,item):
    def runTest(self):
        test_id = item['id']
        self.assertIsInstance(test_id,str)

if __name__ == '__main__':
    while True:
        _count = table.count_item()
        if _count == 1:
            scanResponse = table.scan(TableName='test_api')
            item = scanResponse['Items'][0]
            unittest.main(item)
        
