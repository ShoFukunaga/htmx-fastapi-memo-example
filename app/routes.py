from fastapi import APIRouter, Request, Form, Header
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Annotated, Union

from .crud import get_memos, add_memo, update_memo, delete_memo

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/memos", response_class=HTMLResponse)
async def list_memos(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):
    memos = get_memos()
    if hx_request:
        return templates.TemplateResponse(request=request, name="memos.html", context={"memos": memos})
    return JSONResponse(content=jsonable_encoder(memos))

@router.post("/memos", response_class=HTMLResponse)
async def create_memo(request: Request, memo: Annotated[str, Form()]):
    add_memo(memo)
    return templates.TemplateResponse(request=request, name="memos.html", context={"memos": get_memos()})

@router.put("/memos/{memo_id}", response_class=HTMLResponse)
async def update_memo_handler(request: Request, memo_id: str, text: Annotated[str, Form()]):
    update_memo(memo_id, text)
    return templates.TemplateResponse(request=request, name="memos.html", context={"memos": get_memos()})

@router.post("/memos/{memo_id}/delete", response_class=HTMLResponse)
async def delete_memo_handler(request: Request, memo_id: str):
    delete_memo(memo_id)
    return templates.TemplateResponse(request=request, name="memos.html", context={"memos": get_memos()})
