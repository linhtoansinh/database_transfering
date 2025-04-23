import os
import requests

from backend.exceptions.exceptions import ApiErrorCodeException
from backend.models.connector import Connector

class KafkaConnect:
    KAFKA_CONNECT_TIMEOUT = 15

    @staticmethod
    def call_kafka_api(
        url,
        method,
        headers,
        json,
        success_lower_bound: int = 200,
        success_upper_bound: int = 299,
    ):

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            timeout=KafkaConnect.KAFKA_CONNECT_TIMEOUT,
        )
        if response.status_code >= success_lower_bound and response.status_code <= success_upper_bound:
            # request was successful, no need to try again
            return response
        else:
            message = "Kafka Connect API call failed with status code %s and response %s " % (
                response.status_code,
                response.json().get("message", ""),
            )

            raise ApiErrorCodeException(message, response.status_code, {})

    @staticmethod    
    def post_kafka_connector(connector: Connector):
        try:
            url = os.environ["KAFKA_CONNECT"] + "/connectors/"

            KafkaConnect.call_kafka_api(
                url=url,
                method="POST",
                headers={},
                json=connector.model_dump()
            )

        except Exception as e:
            raise
