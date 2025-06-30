def lambda_handler(event, context):
    intent = event['currentIntent']['name']
    if intent == 'GetCourseInfo':
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "We offer courses in AI, ML, Cloud Computing, and Cybersecurity."
                }
            }
        }
