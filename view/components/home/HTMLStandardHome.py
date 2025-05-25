'''

@author Maurice Amon
'''
from view.components.home.HTMLHome import HTMLHome


class HTMLStandardHome(HTMLHome):

    def __init__(self):
        super(HTMLHome, self).__init__()
        self.init_controls()


    def init_controls(self):
        self._home = '''<div class=\"container py-5 bg-light\" style=\"border-radius: 15px;\"><h1>LLM-Parametrization</h1><form action="/start" method="post">
<label for="temperature" class="form-label">LLM Parameter: Temperature</label><br>
0.0 <input type="range" class="form-range" min="0" max="1" step="0.1" name="temperature" id="temperature"> 1.0
<br><label for="top_p" class="form-label">LLM Parameter: Top P</label><br>
0.0 <input type="range" class="form-range" min="0" max="1" step="0.1" name="top_p" id="top_p"> 1.0<br><br>
<button type="submit" class="btn btn-primary">Execute Tests</button></form></div>'''