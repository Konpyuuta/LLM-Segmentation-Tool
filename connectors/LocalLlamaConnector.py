'''

@author Maurice Amon
'''
from datetime import time

import requests

import json
from simplejson import JSONDecodeError, dumps, loads

import os

from connectors.LLMConnector import LLMConnector


class LocalLlamaConnector(LLMConnector):

    _gpt_uri = "http://160.85.252.174:50052/completion"

    _llm_model = "qwen"

    _request_method = "POST"

    _request_property = "application/json"

    _response = None

    _connection = None

    _temperature = None

    _top_p = None

    _top_k = None

    def __init__(self, _temperature, _top_p, _top_k):
        super(LocalLlamaConnector, self).__init__()
        self._temperature = _temperature
        self._top_p = _top_p
        self._top_k = _top_k
        self.initiate_connection()

    def initiate_connection(self):
        pass


    def send_request(self, query):
        # Set environment variables
        os.environ['CMAKE_ARGS'] = '-DLLAMA_CUBLAS=on'
        os.environ['CUDACXX'] = r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin\nvcc.exe'

        j = dumps({"prompt": f"{query}", "top_p": self._top_p,
                        "top_k": self._top_k, "temperature": self._temperature, "repeat_penalty": 1.4, "seed": 100, "max_tokens": 400})
        response = requests.post(self._gpt_uri,
                                 data=j,
                                 headers={"Content-Type": "application/json"})
        self._response = f'''<div class="card">
    <div class="card-header" id="{self._temperature}{self._top_p}{self._top_k}">
      <h5 class="mb-0">
        <button class="btn btn-link" data-toggle="collapse" data-target="#collapse{self._temperature}{self._top_p}{self._top_k}" aria-expanded="true" aria-controls="collapse{self._temperature}{self._top_p}{self._top_k}">
          Konfiguration - Temperature: {self._temperature}, Top P: {self._top_p}, Top K: {self._top_k}
        </button>
      </h5>
    </div>

    <div id="collapse{self._temperature}{self._top_p}{self._top_k}" class="collapse show" aria-labelledby="{self._temperature}{self._top_p}{self._top_k}" data-parent="#accordion">
      <div class="card-body">
        <p>Prompt: {query}</p>
        <p>Response: {loads(response.content)['content']}</p>
      </div>
    </div>
  </div>'''



    def read_response(self):
        self._response = self._response

    def extract_response(self):
        pass

    def get_response(self):
        return self._response

