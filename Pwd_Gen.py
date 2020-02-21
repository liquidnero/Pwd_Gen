#!/usr/bin/env python

import json
import random

class lists:
    def__init__(self,list)
        self.list = []
        
    def app_to_list(self,range,start):
        for t in self.range
und_ls = []
for t in range (26):
    und_ls.append(chr(97+t))
    
upp_ls = []
for t in range (26):
    upp_ls.append(chr(65+t))
    
num_ls = []
for t in range(10):
    num_ls.append(chr(48+t))

char_ls = []
for t in range(15):
    char_ls.append(chr(33+t))
for t in range(7):
    char_ls.append(chr(58+t))
for t in range(6):
    char_ls.append(chr(91+t))
for t in range(4):
    char_ls.append(chr(123+t))

def lower():
    return random.choice(und_ls)

def upper():
    return random.choice(upp_ls)
    
def nums():
    return random.choice(num_ls)

def chars():
    return random.choice(char_ls)
    
def gen_pwd(event):
    y = ""
    new_pwd = []
    for i in range(event["len"]):
        new_pwd.append(rand_pick(event))
    return y.join(new_pwd)
    
def rand_pick(event):
    n = random.randrange(4)
    if n == 0:
        if event["upper"] == True:
            return upper()
        else:
            return rand_pick(event)
    elif n == 1:
        if event["lower"] == True:
            return lower()
        else:
            return rand_pick(event)   
    elif n == 2:
        if event["chars"] == True:
            return chars()
        else:
            return rand_pick(event)
    else:
        if event["nums"] == True:
            return nums()
        else:
            return rand_pick(event)
    
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({"password" : gen_pwd(json.loads(event['body']))})
    }
