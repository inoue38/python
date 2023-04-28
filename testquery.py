import re
import json
import requests
import datetime
import boto3
import time
import sys
import socket
from flask import Flask, abort, request
from flask_restful import Resource, Api
from datetime import datetime
from boto3.dynamodb.conditions import Key

spaceid = "1234567890abcdefghijklmnopqrstuvwxyz"

dynamodb = boto3.resource('dynamodb',region_name='ap-northeast-1')
table    = dynamodb.Table('db_put_test')
dbresponse = table.query(
    KeyConditionExpression=Key('spaceid').eq(spaceid)
)

print(dbresponse)
