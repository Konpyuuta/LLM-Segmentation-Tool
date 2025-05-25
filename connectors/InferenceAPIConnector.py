'''

@author Maurice Amon
'''
from connectors.LLMConnector import LLMConnector
import re
from openai import OpenAI


class InferenceAPIConnector(LLMConnector):

    _base_url = "https://api.inference.net/v1"

    _api_key = "inference-"

    _llm_model = "meta-llama/llama-3.3-70b-instruct/fp-16"

    _request_method = "POST"

    _request_property = "application/json"

    _request_headers = {
        "Authorization": f"Bearer ",
        "Content-Type": "application/json"
    }

    _response = ""

    _filename = None

    _technique = None

    _connection = None

    _temperature = None

    _top_p = None

    _top_k = None

    def __init__(self, _temperature, _top_p, _top_k, filename, technique):
        super(InferenceAPIConnector, self).__init__()
        self._filename = filename
        self._technique = technique
        self._temperature = _temperature
        self._top_p = _top_p
        self._top_k = _top_k
        self.initiate_connection()

    def initiate_connection(self):
        pass

    def send_request(self, query):

        client = OpenAI(
            base_url=self._base_url,
            api_key=self._api_key,
        )

        response = client.chat.completions.create(
            model=self._llm_model,
            messages=[
                {
                    "role": "user",
                    "content": f"{query}"
                }
            ],
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                self._response += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end='', flush=True)

        self.create_html(query)


    def create_html(self, query):
        self._response = f'''<div class="card">
          <div class="card-header" id="{self._filename}: {self._technique} with temperature = {self._temperature} and top P = {self._top_p}">
            <h5 class="mb-0">
              <button class="btn btn-link" data-toggle="collapse" data-target="#collapse{self._filename}:{self._technique}" aria-expanded="true" aria-controls="collapse{self._filename}:{self._technique}">
                Konfiguration - Temperature: {self._filename}, Technique: {self._technique}
              </button>
            </h5>
          </div>

          <div id="collapse{self._filename}:{self._technique}" class="collapse show" aria-labelledby="{self._filename}:{self._technique}" data-parent="#accordion">
            <div class="card-body">
              <p>Prompt: {query}</p>
              <p>Response: {self.wrap_quotes(self._response)}</p>
            </div>
          </div>
        </div>'''

    def wrap_quotes(self, text):
        # Replace ###text### with <q class="blockquote">text</q>
        quote_template = r'<span class="p-2 rounded bg-light text-muted small d-block mb-2">\1</span>'

        # Use re.DOTALL for multiline support
        return re.sub(r'(.*?)###', quote_template, text, flags=re.DOTALL)

    def read_response(self):
        self._response = self._response

    def extract_response(self):
        pass

    def get_response(self):
        return self._response