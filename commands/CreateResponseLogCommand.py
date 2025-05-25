'''

@author Maurice Amon
'''
from commands.Command import Command


class CreateResponseLogCommand(Command):

    _results = None

    _filename = None

    def __init__(self, results, filename):
        self._results = results
        self._filename = filename

    _header = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="iso-8859-1">
                    <script src="https://code.jquery.com/jquery-3.6.1.slim.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js"
                    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

                    <link th:href="@{/css/style.css}" rel="stylesheet" type="text/css">

                    <link rel="icon" href="https://www.zhaw.ch/favicon.ico" type="image/png">
                    <title>M. Sc. Seminar in Software Engineering: Segmentations by LLama 3.3 70B/fp-16 Instruct model</title></head>
                    <body>
                    <div class="container py-5">'''

    _container_start = '''<div id="accordion">'''

    _container_end = '''</div></body></html>'''



    def execute(self):
        html_content = ""
        for result in self._results:
            html_content += result

        # Create the HTML file with the result set ..
        f = open(f'{self._filename}.html', 'w', encoding='utf-8')
        f.write(self._header)
        f.write(self._container_start)
        f.write(html_content)
        f.write(self._container_end)
        f.close()