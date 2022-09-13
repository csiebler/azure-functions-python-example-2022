import logging
import requests
import json 

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # get IP of function host
    ip_address = requests.get("https://httpbin.org/ip").json()['origin']

    # Try to get JSON body in request
    try:
        json_body = req.get_json()
    except ValueError:
        json_body = None
        pass

    response = {
        'function_ip_address': ip_address,
        'invoked_method': req.method,
        'json_body': json_body
    }

    return func.HttpResponse(json.dumps(response), status_code=200, mimetype="application/json")
