'''

@author Maurice Amon
@description
'''
from techniques.PromptingTechnique import PromptingTechnique


class MetaTechnique(PromptingTechnique):


    def __init__(self, _prompt):
        super(MetaTechnique, self).__init__(_prompt)

    def prepare_prompt(self):
        self._prepared_prompt = f'''Question: {super()._prompt} 
                                    Answer Structure:
                                    1.  Begin the response with "Let's think step by step."
                                    2.  Follow with the reasoning steps, ensuring the solution process is broken down clearly and logically.
                                    3.  End the answer with the final answer encapsulated in a JSON-formatted structure, for clarity and emphasis.
                                    4.  Finally, state "The answer is [Final answer to the question].", with the final answer presented in JSON-notation.'''


