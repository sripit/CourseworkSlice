#By default, pytest will autodiscover test files that
# start or end with test -- i.e., test_*.py or *_test.py.
# Test functions must begin with test_, and if you want
# to use classes they must also begin with Test.

import json

def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get('/ping')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']