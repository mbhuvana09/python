import pytest
from lambda_function import lambda_handler

def test_valid_number():
    event = {'number': 4}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200
    assert response['body'] == 16

def test_input_validation_no_number():
    event = {}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 400
    assert response['body'] == 'Input validation error: "number" key is required'

def test_input_validation_invalid_type():
    event = {'number': 'four'}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 400
    assert response['body'] == 'Input validation error: "number" must be an integer or float'

def test_edge_case_zero():
    event = {'number': 0}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200
    assert response['body'] == 0

def test_edge_case_negative():
    event = {'number': -3}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200
    assert response['body'] == 9
