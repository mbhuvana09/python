def lambda_handler(event, context):
    # Input validation
    if 'number' not in event:
        return {
            'statusCode': 400,
            'body': 'Input validation error: "number" key is required'
        }

    number = event['number']
    
    # Check if the input is a valid number
    if not isinstance(number, (int, float)):
        return {
            'statusCode': 400,
            'body': 'Input validation error: "number" must be an integer or float'
        }

    # Calculate square
    square = number ** 2
    
    return {
        'statusCode': 200,
        'body': square
    }
