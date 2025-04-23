from bson import json_util

class ApiErrorCodeException(Exception):
    def __init__(self, request_description, status_code, json_response):
        message = (
            f"Error executing request for {request_description}. Status code {status_code} returned for with message"
            + json_util.dumps(json_response)
        )
        super().__init__(message)