from db_cla import set_req, get_req, del_req

while True:
    qs = input('== ')
    qqs = qs.split()

    fn_map = {'set': set_req, 'get': get_req, 'del': del_req}
    
    req_fn = fn_map[qqs[0]]

    print(req_fn(qqs[1:]))

