# tests/test_app.py

from todo-web.app import app

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert b'To-Do List' in response.data

def test_add_task():
    client = app.test_client()
    response = client.post('/add', data={'task': 'Test task'})
    assert b'Test task' in response.data
