import requests
import json

def set_req(s):
    if len(s) != 2:
        return

    key, value = s[0], s[1]
    data = {'key': key, 'value': value}

    res = requests.post('http://localhost:5000/fn/set_fn', data=json.dumps(data))
    return res.text

def get_req(s):
    if len(s) != 1:
        return

    key= s[0]
    data = {'key': key}

    res = requests.post('http://localhost:5000/fn/get_fn', data=json.dumps(data))
    return res.text

def del_req(s):
    if len(s) != 1:
        return

    key= s[0]
    data = {'key': key}

    res = requests.post('http://localhost:5000/fn/del_fn', data=json.dumps(data))
    return res.text

def incr_req(s):
    if len(s) != 1:
        return

    key= s[0]
    data = {'key': key}

    res = requests.post('http://localhost:5000/fn/incr_fn', data=json.dumps(data))
    return res.text
    
