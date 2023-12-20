# test_app.py

from app import app  # This line is added to import the Flask app instance

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert b'To-Do List' in response.data

def test_add_task():
    client = app.test_client()
    # Set follow_redirects=True to follow the redirect after the post request
    response = client.post('/add', data={'task': 'Test task'}, follow_redirects=True)
    # The assertion should now check the final page after the redirect
    assert b'Test task' in response.data

