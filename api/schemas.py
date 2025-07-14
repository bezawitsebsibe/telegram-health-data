from pydantic import BaseModel
from typing import List

class TopProduct(BaseModel):
    product_name: str
    mention_count: int

class ChannelActivity(BaseModel):
    channel_name: str
    post_date: str
    message_count: int

class MessageSearchResult(BaseModel):
    message_id: int
    channel_name: str
    message_text: str
