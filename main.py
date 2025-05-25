from fastapi import FastAPI, Form
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from Configurations import Configurations
from commands.InitializeTestdataCommand import InitializeTestdataCommand
from commands.SegmentationCommand import SegmentationCommand
from model import CurrentWebpage
from techniques.PromptType import PromptType
from view.ViewClient import ViewClient
from view.Webpage import Webpage
import os

'''

@author Maurice Amon
'''

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def root():
    CurrentWebpage.current_webpage = Webpage.HOME_PAGE
    viewClient = ViewClient()
    htmlSite = viewClient.create_webpage(Webpage.HOME_PAGE, None).get_view_content()
    return HTMLResponse(htmlSite)


@app.post("/start")
async def start(temperature: str = Form(...), top_p: str = Form(...)):
    Configurations().set_temperature(temperature)
    Configurations().set_top_p_fixed(top_p)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(os.path.join(current_dir, "material"), "cli")
    fetch_data_command = InitializeTestdataCommand(test_dir)
    fetch_data_command.execute()
    for source_code in fetch_data_command.get_source_files():
        segment_command = SegmentationCommand(source_code, Configurations().get_prompt_scenarios())
        segment_command.execute()



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
