from fastapi import FastAPI, HTTPException
from typing import List
from api import crud
from api.schemas import TopProduct, ChannelActivity, MessageSearchResult

app = FastAPI()

@app.get("/api/reports/top-products", response_model=List[TopProduct])
def top_products(limit: int = 10):
    return crud.get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity", response_model=List[ChannelActivity])
def channel_activity(channel_name: str):
    data = crud.get_channel_activity(channel_name)
    if not data:
        raise HTTPException(status_code=404, detail="Channel not found")
    return data

@app.get("/api/search/messages", response_model=List[MessageSearchResult])
def search_messages(query: str):
    return crud.search_messages(query)
