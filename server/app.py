from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse


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

    Sequence = sequence.replace(restriction_site, restriction_site)

    return templates.TemplateResponse("index.html", 
        {"request": request, "motif_count": motif_count, "Sequence": Sequence})


#print(text.replace(search_word, '\033[44;33m{}\033[m'.format(search_word)))
#print("\033[44;33mHello World!\033[m")

@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
