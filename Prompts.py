'''

@author Maurice Amon
'''
from abc import ABC


class Prompts(ABC):

    first_prompt = "Who exactly are you?"

    second_prompt = "Please write a playbook/incident-response for an employee in the following situation: The employee works as an assistant in a hospital where he's responsible for administrating the patients data. While he was going to the office, he lost his laptop in the train. The data of the patients were stored on this laptop together with other highly private data."

    third_prompt = ""

    fourth_prompt = ""

    fifth_prompt = ""

    prompt_list = [first_prompt, second_prompt, third_prompt, fourth_prompt, fifth_prompt]
