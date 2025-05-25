'''

@author Maurice Amon
'''
import CoTPart
import FewshotPart
import RealMetaPart
from commands.Command import Command
import json

from commands.CreateResponseLogCommand import CreateResponseLogCommand
from connectors.InferenceAPIConnector import InferenceAPIConnector
from techniques.PromptType import PromptType
from view.Webpage import Webpage


class SegmentationCommand(Command):

    _source_code = None

    _segments = list()

    _zeroshot_prompt = "\n Prompt: Take a look at the java-code under SOURCE-CODE above and build semantically coherent code-fragments by dividing the code with ### as a delimiter. Make sure to always include ### at the end of a code-fragment. Only give the code-fragments as a response, omit everything else."

    _meta_prompt = ("1. As a first step, analyze the source code by determining it's functionality."
                    "2. After that build semantically coherent fragments of the source code.")

    _real_meta_prompting = None

    _prompt_types = None

    def __init__(self, source_code, prompt_types: PromptType):
        self._source_code = source_code
        self._real_meta_prompting = RealMetaPart.real_meta_part
        self._prompt_types = prompt_types


    def compose_prompt(self, technique):
        comp = self.fetch_prompting_technique(technique)
        return comp

    def fetch_prompting_technique(self, technique):
        prompt = None
        match technique:
            case PromptType.ZERO_SHOT:
                prompt = f"SOURCE-CODE: {self._source_code[1]}"
                prompt += self._zeroshot_prompt
            case PromptType.FEW_SHOT:
                prompt = FewshotPart.fewshot_part
                prompt += f"SOURCE-CODE: {self._source_code[1]}"
            case PromptType.CoT:
                prompt = CoTPart.cot_part
                prompt += f"SOURCE-CODE: {self._source_code[1]}"
            case PromptType.META:
                prompt = f"SOURCE-CODE: {self._source_code[1]}"
                prompt += self._meta_prompt
            case PromptType.GEN_META:
                prompt = self._real_meta_prompting
                prompt += f"\n SOURCE-CODE: {self._source_code[1]}"

            case _:
                prompt = f"SOURCE-CODE: {self._source_code[1]}"
                prompt += self._zeroshot_prompt

        return prompt

    def execute(self):
        results = list()
        for technique in self._prompt_types:
            connector = InferenceAPIConnector(0, 1, 1, self._source_code[0], technique)
            connector.send_request(self.compose_prompt(technique))
            response = connector.get_response().encode('utf-8')
            results.append('<pre>' + response.decode('utf-8') + '</pre>')
            for segment in response.decode('utf-8').split('###'):
                self._segments.append(segment)
                print(segment)
        command = CreateResponseLogCommand(results, self._source_code[0])
        command.execute()
        results.clear()