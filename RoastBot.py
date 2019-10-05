#!/usr/bin/python3
import json
from random import randint

INSULT_LIST = 'insults.json'
__version__ = '0.1'


# with open('insults.json', 'w') as file:
#     json.dump(insults, file)

def load(json_file=INSULT_LIST):
    with open(json_file, 'r') as fp:
        data = json.load(fp)
    return data

def roast_me(data,chosen=None,random=True):
    maxim = len(data)
    if chosen is None or chosen < 0 or chosen >maxim:
        chosen = randint(0, maxim)
    return data[chosen]


if __name__=='__main__':
    print("Welcome to RoastBot")
    data = load()
    print(roast_me(data))
