import json
from Assignment2.part2.src.jsonapi import jsonapi
test = jsonapi

my_data_c = { "hey": complex(1, 2) }
my_data_r = { "there": range(1, 10, 3) }
my_data_d = { 73: False }

json_data_c = test.dumps(my_data_c, cls=test.MyEncoder)
json_data_r = test.dumps(my_data_r, cls=test.MyEncoder)
json_data_d = test.dumps(my_data_d, cls=test.MyEncoder)

decoded_c = test.loads(json_data_c, cls=test.MyDecoder)
decoded_r = test.loads(json_data_r, cls=test.MyDecoder)
decoded_d = test.loads(json_data_d, cls=test.MyDecoder)


def test_dumps():
    if ((json_data_c == "{\"hey\": {\"real\": 1.0, \"imag\": 2.0, \"__extended_json_type__\": \"complex\"}}") and
       (json_data_r == "{\"there\": {\"start\": 1, \"stop\": 10, \"step\": 3, \"__extended_json_type__\": \"range\"}}") and
       (json_data_d == "{\"73\": false}")):
        return True
    else:
        return False

def test_loads():
    if ((decoded_c == my_data_c) and
       (decoded_r == my_data_r) and
       (decoded_d == my_data_d)):
        return True
    else:
        return False
    


test_dumps()
test_loads()
