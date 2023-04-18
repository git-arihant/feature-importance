import uvicorn
import test
import model
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import AwesomeForm
import aiofiles
import sendmail

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("awesome-form.html", {"request": request})

@app.post('/', response_class=HTMLResponse)
async def post_form(request: Request, form_data: AwesomeForm = Depends(AwesomeForm.as_form)):
    async with aiofiles.open('small.csv', 'wb') as out_file:
        content = await form_data.file.read()  # async read
        await out_file.write(content)  # async write
    nf = form_data.features
    model.data('small.csv',nf)
    print('sending mail')
    sendmail.send_mail(form_data.email)
    print('mail sent')
    return templates.TemplateResponse("awesome-form.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app)