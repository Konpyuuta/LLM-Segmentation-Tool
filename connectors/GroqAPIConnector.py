'''


@author Maurice Amon
'''
import requests

from connectors.LLMConnector import LLMConnector

import json


class GroqAPIConnector(LLMConnector):

    _gpt_uri = "https://api.groq.com/openai/v1/chat/completions"

    _llm_model = "llama-3.3-70b-versatile"

    _request_method = "POST"

    _request_property = "application/json"

    _request_headers = {
        "Authorization": f"Bearer ",
        "Content-Type": "application/json"
    }

    _response = None

    _connection = None

    _temperature = None

    _top_p = None

    _top_k = None

    def __init__(self, _temperature, _top_p, _top_k):
        super(GroqAPIConnector, self).__init__()
        self._temperature = _temperature
        self._top_p = _top_p
        self._top_k = _top_k
        self.initiate_connection()

    def initiate_connection(self):
        pass

    def send_request(self, query):
        data = {
            "model": f"{self._llm_model}",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{query}"}
            ],
            "temperature": 0.0,
            "top_p": 1
        }
        response = requests.post(self._gpt_uri, json=data, headers=self._request_headers)
        print(response.json())
        answer = response.json()["choices"][0]["message"]["content"]
        self._response = answer

    def read_response(self):
        self._response = self._response

    def extract_response(self):
        pass

    def get_response(self):
        return self._response

