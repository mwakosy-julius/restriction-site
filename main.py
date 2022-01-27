from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import uvicorn

from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    
    motif_count = ''     

    return templates.TemplateResponse("index.html", 
        {"request": request, "motif_count": motif_count})

@app.post("/")
async def root(request: Request, restriction_site: str = Form(...), sequence: str = Form(...)):
    
    motif_count = sequence.count(restriction_site) or  sequence.count(reverse(restriction_site)) 

    return templates.TemplateResponse("index.html", 
        {"request": request, 
        "motif_count": motif_count, 
        "sequence": sequence, 
        "restriction_site": restriction_site})

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)